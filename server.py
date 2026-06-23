"""
API Server local pour connecter l'interface SaaS.

Fournit une API HTTP/SSE locale sur http://localhost:8000
pour exécuter les agents et streamer leurs réponses en temps réel
vers l'interface hébergée sur GitHub Pages.
"""

import asyncio
import json
import os
import re
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

# Charger le fichier .env s'il existe pour récupérer la GEMINI_API_KEY
if os.path.exists(".env"):
    with open(".env", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ[key.strip()] = val.strip().strip('"').strip("'")

from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig

from agents.orchestrator import HierarchicalAgent, generate_subagent_structure

app = FastAPI(title="Antigravity Local SaaS Bridge")

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Antigravity Local SaaS Bridge is running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", file.filename)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    return {"status": "ok", "filename": file.filename, "filepath": file_path}


# Activer CORS pour permettre à l'interface GitHub Pages d'appeler l'API locale

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise toutes les origines (GitHub Pages, localhost, etc.)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RunPayload(BaseModel):
    category: str
    file: str
    prompt: str
    hierarchical: bool = False

def clean_docstring(doc: str) -> str:
    if not doc:
        return ""
    lines = doc.strip().split("\n")
    return " ".join([l.strip() for l in lines if l.strip()])

def extract_agent_info(file_path: str) -> tuple:
    if not os.path.exists(file_path):
        return "Agent inconnu", "Tu es un assistant IA spécialisé."
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    doc_match = re.match(r'^\s*"""(.*?)"""', content, re.DOTALL)
    description = clean_docstring(doc_match.group(1)) if doc_match else "Aucune description."

    instructions_match = re.search(r'system_instructions=\s*\(\s*"(.*?)"\s*\)', content, re.DOTALL)
    if not instructions_match:
        instructions_match = re.search(r'system_instructions=\s*"(.*?)"', content, re.DOTALL)
    
    instructions = clean_docstring(instructions_match.group(1)) if instructions_match else "Tu es un agent d'intelligence artificielle spécialisé."
    
    # Forcer le français pour tous les agents sauf les agents linguistiques spécifiques
    is_foreign_lang = any(lang in file_path for lang in ["anglais_agent.py", "espagnol_agent.py", "japonais_agent.py", "chinois_agent.py", "italien_agent.py"])
    if not is_foreign_lang:
        instructions += " Tu dois impérativement répondre et formuler toutes tes réflexions internes (thoughts) et tes messages en français."
        
    return description, instructions


async def run_classic_stream(instructions: str, prompt: str):
    """Exécute un agent standard et streame ses pensées et réponses."""
    config = LocalAgentConfig(
        system_instructions=instructions,
        capabilities=CapabilitiesConfig()
    )
    try:
        yield f"data: {json.dumps({'type': 'status', 'content': '🚀 Initialisation de l\'agent...'})}\n\n"
        async with Agent(config) as agent:
            yield f"data: {json.dumps({'type': 'status', 'content': '🧠 Envoi du prompt à l\'agent...'})}\n\n"
            response = await agent.chat(prompt)
            
            # Streamer les pensées d'abord
            async for thought in response.thoughts:
                yield f"data: {json.dumps({'type': 'thought', 'content': thought})}\n\n"
                await asyncio.sleep(0.01) # Petit delais pour fluidifier l'UI
            
            yield f"data: {json.dumps({'type': 'status', 'content': '✍️ Rédaction de la réponse...'})}\n\n"
            # Streamer la réponse textuelle
            async for token in response:
                yield f"data: {json.dumps({'type': 'token', 'content': token})}\n\n"
                
        yield f"data: {json.dumps({'type': 'status', 'content': '✅ Terminé'})}\n\n"
    except Exception as e:
        yield f"data: {json.dumps({'type': 'error', 'content': str(e)})}\n\n"

async def run_hierarchical_stream(agent_name: str, description: str, instructions: str, prompt: str):
    """Exécute un réseau de 31 agents et streame l'avancement pas-à-pas."""
    try:
        yield f"data: {json.dumps({'type': 'status', 'content': '🧠 Génération de la structure hiérarchique (1-5-25 agents)...'})}\n\n"
        structure = await generate_subagent_structure(agent_name, description, instructions)
        
        yield f"data: {json.dumps({'type': 'status', 'content': '🤝 Recrutement des 5 sous-agents de Niveau 1 et 25 spécialistes de Niveau 2...'})}\n\n"
        
        # Classe interne modifiée pour streamer les statuts via le générateur
        class StreamingHierarchicalAgent(HierarchicalAgent):
            def __init__(self, name: str, role: str, instructions: str, subagents_config=None, queue=None, depth=0):
                super().__init__(name, role, instructions, subagents_config)
                self.queue = queue
                self.depth = depth
                # Ré-instancier les sous-agents avec la queue
                if subagents_config:
                    self.subagents = []
                    for cfg in subagents_config:
                        self.subagents.append(
                            StreamingHierarchicalAgent(
                                name=cfg["name"],
                                role=cfg["role"],
                                instructions=cfg["instructions"],
                                subagents_config=cfg.get("subagents"),
                                queue=queue,
                                depth=depth + 1
                            )
                        )

            async def execute(self, prompt: str, depth: int = 0) -> str:
                indent = "  " * depth
                self.queue.put_nowait(f"🚀 [{self.name}] ({self.role}) démarre...")
                
                if self.subagents:
                    self.queue.put_nowait(f"➔ [{self.name}] délègue à ses 5 sous-agents de niveau {depth + 1}...")
                    tasks = [sub.execute(prompt, depth + 1) for sub in self.subagents]
                    sub_results = await asyncio.gather(*tasks)
                    
                    synthesis_prompt = (
                        f"Demande originale : '{prompt}'\n\n"
                        f"Rapports de mes 5 sous-agents :\n"
                    )
                    for sub, res in zip(self.subagents, sub_results):
                        synthesis_prompt += f"\n=== Rapport de [{sub.name}] ({sub.role}) ===\n{res}\n"
                    
                    synthesis_prompt += "\nAnalyse et fusionne ces contributions pour formuler la réponse finale optimale."
                    
                    self.queue.put_nowait(f"✍️ [{self.name}] débute la synthèse finale...")
                    config = LocalAgentConfig(
                        system_instructions=self.instructions,
                        capabilities=CapabilitiesConfig()
                    )
                    
                    result = []
                    async with Agent(config) as agent:
                        response = await agent.chat(synthesis_prompt)
                        async for token in response:
                            result.append(token)
                            if depth == 0:
                                self.queue.put_nowait(("#token#", token))
                    return "".join(result)
                else:
                    config = LocalAgentConfig(
                        system_instructions=self.instructions,
                        capabilities=CapabilitiesConfig()
                    )
                    result = []
                    async with Agent(config) as agent:
                        response = await agent.chat(prompt)
                        async for token in response:
                            result.append(token)
                    self.queue.put_nowait(f"✅ [{self.name}] terminé.")
                    return "".join(result)

        queue = asyncio.Queue()
        agent_root = StreamingHierarchicalAgent(
            name=structure["name"],
            role=structure["role"],
            instructions=structure["instructions"],
            subagents_config=structure.get("subagents"),
            queue=queue,
            depth=0
        )

        # Lancer l'exécution de l'agent en tâche de fond
        execution_task = asyncio.create_task(agent_root.execute(prompt))

        # Streamer les messages de la queue vers le client
        while not execution_task.done() or not queue.empty():
            try:
                msg = await asyncio.wait_for(queue.get(), timeout=0.1)
                if isinstance(msg, tuple) and msg[0] == "#token#":
                    yield f"data: {json.dumps({'type': 'token', 'content': msg[1]})}\n\n"
                else:
                    yield f"data: {json.dumps({'type': 'status', 'content': msg})}\n\n"
                queue.task_done()
            except asyncio.TimeoutError:
                continue
                
        await execution_task
        yield f"data: {json.dumps({'type': 'status', 'content': '✅ Exécution hiérarchique terminée.'})}\n\n"
    except Exception as e:
        yield f"data: {json.dumps({'type': 'error', 'content': str(e)})}\n\n"

@app.post("/run")
async def run_agent(payload: RunPayload):
    file_path = os.path.join("agents", payload.category, payload.file)
    description, instructions = extract_agent_info(file_path)
    agent_name = payload.file.replace("_agent.py", "").replace("_", " ").title()

    if payload.hierarchical:
        generator = run_hierarchical_stream(agent_name, description, instructions, payload.prompt)
    else:
        generator = run_classic_stream(instructions, payload.prompt)

    return StreamingResponse(generator, media_type="text/event-stream")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

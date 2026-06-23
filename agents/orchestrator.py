"""
Orchestrateur d'Agents Hiérarchiques.

Permet de structurer et d'exécuter n'importe quel agent principal
avec 5 sous-agents de niveau 1, qui possèdent chacun 5 sous-agents de niveau 2 (total 31 agents).
"""

import asyncio
import json
import sys
from typing import List, Dict, Any, Optional
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig

class HierarchicalAgent:
    def __init__(self, name: str, role: str, instructions: str, subagents_config: Optional[List[Dict[str, Any]]] = None):
        self.name = name
        self.role = role
        self.instructions = instructions
        self.subagents = []
        if subagents_config:
            for cfg in subagents_config:
                self.subagents.append(
                    HierarchicalAgent(
                        name=cfg["name"],
                        role=cfg["role"],
                        instructions=cfg["instructions"],
                        subagents_config=cfg.get("subagents")
                    )
                )

    async def execute(self, prompt: str, depth: int = 0) -> str:
        indent = "  " * depth
        print(f"{indent}🚀 [{self.name}] ({self.role}) démarre...")

        if self.subagents:
            print(f"{indent}➔ [{self.name}] délègue à ses {len(self.subagents)} sous-agents de niveau {depth + 1}...")
            
            # Exécuter tous les sous-agents en parallèle
            tasks = [sub.execute(prompt, depth + 1) for sub in self.subagents]
            sub_results = await asyncio.gather(*tasks)
            
            # Synthétiser les rapports
            synthesis_prompt = (
                f"Voici la demande originale de l'utilisateur : '{prompt}'\n\n"
                f"Voici les rapports détaillés de mes 5 sous-agents :\n"
            )
            for sub, res in zip(self.subagents, sub_results):
                synthesis_prompt += f"\n=== Rapport de [{sub.name}] ({sub.role}) ===\n{res}\n"
            
            synthesis_prompt += (
                "\nAnalyse et fusionne ces contributions pour formuler la réponse finale "
                "la plus pertinente, complète et structurée possible."
            )
            
            config = LocalAgentConfig(
                system_instructions=self.instructions,
                capabilities=CapabilitiesConfig()
            )
            
            print(f"{indent}✍️ [{self.name}] synthétise les contributions...")
            result = []
            async with Agent(config) as agent:
                response = await agent.chat(synthesis_prompt)
                async for token in response:
                    result.append(token)
                    if depth == 0:  # N'afficher en temps réel que le résultat de l'agent racine
                        sys.stdout.write(token)
                        sys.stdout.flush()
            return "".join(result)
        else:
            # Agent de niveau 2 (feuille de l'arbre)
            config = LocalAgentConfig(
                system_instructions=self.instructions,
                capabilities=CapabilitiesConfig()
            )
            result = []
            async with Agent(config) as agent:
                response = await agent.chat(prompt)
                async for token in response:
                    result.append(token)
            print(f"{indent}✅ [{self.name}] a terminé sa tâche.")
            return "".join(result)


async def generate_subagent_structure(main_agent_name: str, main_role: str, main_instructions: str) -> Dict[str, Any]:
    """Génère dynamiquement la structure hiérarchique de 5 sous-agents et 25 sous-sous-agents."""
    print(f"🧠 Analyse et génération de la structure hiérarchique des sous-agents pour : {main_agent_name}...")
    
    generation_prompt = f"""
    Tu es un architecte d'organisations multi-agents.
    Pour l'agent principal suivant :
    - Nom : {main_agent_name}
    - Rôle : {main_role}
    - Instructions : {main_instructions}
    
    Génère une structure de 5 sous-agents de niveau 1.
    Pour CHACUN de ces 5 sous-agents, génère également 5 sous-agents de niveau 2 (donc 25 au total).
    
    Retourne UNIQUEMENT un objet JSON valide sans markdown, respectant ce schéma exact :
    {{
        "name": "{main_agent_name}",
        "role": "{main_role}",
        "instructions": "{main_instructions}",
        "subagents": [
            {{
                "name": "Nom du sous-agent Niv 1",
                "role": "Rôle précis",
                "instructions": "Instructions système pour le sous-agent",
                "subagents": [
                    {{
                        "name": "Nom du sous-agent Niv 2",
                        "role": "Rôle très spécifique",
                        "instructions": "Instructions très ciblées"
                    }},
                    // ... 5 sous-agents de niveau 2
                ]
            }},
            // ... 5 sous-agents de niveau 1
        ]
    }}
    Reste strict sur le JSON, aucun texte avant ou après.
    """
    
    config = LocalAgentConfig(
        system_instructions="Tu es un générateur de configurations JSON strictes."
    )
    
    async with Agent(config) as agent:
        response = await agent.chat(generation_prompt)
        raw_json = []
        async for token in response:
            raw_json.append(token)
        
        json_str = "".join(raw_json).strip()
        # Enlever les éventuels backticks markdown
        if json_str.startswith("```"):
            json_str = json_str.split("\n", 1)[1]
        if json_str.endswith("```"):
            json_str = json_str.rsplit("\n", 1)[0]
            
        try:
            return json.loads(json_str.strip())
        except Exception as e:
            print(f"⚠️ Erreur de parsing JSON de la structure générée : {e}. Utilisation d'une structure générique par défaut.")
            # Fallback structure
            return create_fallback_structure(main_agent_name, main_role, main_instructions)


def create_fallback_structure(name: str, role: str, instructions: str) -> Dict[str, Any]:
    """Crée une structure hiérarchique générique par défaut si le LLM échoue à générer le JSON."""
    subagents = []
    for i in range(1, 6):
        sub_subagents = []
        for j in range(1, 6):
            sub_subagents.append({
                "name": f"{name} L2.{i}.{j}",
                "role": f"Spécialiste de sous-tâche {j} pour l'unité {i}",
                "instructions": f"Tu es un agent spécialisé exécutant la sous-tâche {j} sous la supervision de l'unité {i}."
            })
        subagents.append({
            "name": f"{name} L1.{i}",
            "role": f"Superviseur de l'unité {i}",
            "instructions": f"Tu supervises et synthétises les résultats de tes 5 sous-agents de niveau 2.",
            "subagents": sub_subagents
        })
    return {
        "name": name,
        "role": role,
        "instructions": instructions,
        "subagents": subagents
    }

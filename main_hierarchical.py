"""
Launcher d'Agents Hiérarchiques.

Permet de lancer n'importe lequel des 39 agents du projet
avec une architecture hiérarchique de 31 agents (1 agent principal,
5 sous-agents de niveau 1, et 25 sous-agents de niveau 2).
"""

import asyncio
import os
import sys
import re
from agents.orchestrator import HierarchicalAgent, generate_subagent_structure

# Liste des catégories et de leurs agents associés
CATEGORIES = {
    "1": ("dev", "🔧 Développement"),
    "2": ("business", "💼 Business"),
    "3": ("devops", "⚙️ DevOps"),
    "4": ("creative", "🎨 Créatif"),
    "5": ("juridique", "⚖️ Juridique"),
    "6": ("finance", "💰 Finance"),
    "7": ("rh", "👥 Ressources Humaines"),
    "8": ("immobilier", "🏠 Immobilier"),
    "9": ("education", "🎓 Éducation")
}

def clean_docstring(doc: str) -> str:
    """Nettoie et formate les docstrings des fichiers agents."""
    if not doc:
        return ""
    lines = doc.strip().split("\n")
    return " ".join([l.strip() for l in lines if l.strip()])

def extract_agent_info(file_path: str) -> tuple:
    """Parse le fichier d'un agent pour en extraire sa description et ses instructions système."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extraction des docstrings du module
    doc_match = re.match(r'^\s*"""(.*?)"""', content, re.DOTALL)
    description = clean_docstring(doc_match.group(1)) if doc_match else "Aucune description disponible."

    # Extraction des system_instructions
    instructions_match = re.search(r'system_instructions=\s*\(\s*"(.*?)"\s*\)', content, re.DOTALL)
    if not instructions_match:
        instructions_match = re.search(r'system_instructions=\s*"(.*?)"', content, re.DOTALL)
    
    if instructions_match:
        instructions = clean_docstring(instructions_match.group(1))
    else:
        instructions = "Tu es un agent d'intelligence artificielle spécialisé."

    return description, instructions

async def launch_hierarchical_agent(agent_name: str, file_path: str, prompt: str):
    """Génère l'organisation et lance l'agent avec ses 30 sous-agents."""
    description, instructions = extract_agent_info(file_path)
    
    print("\n" + "=" * 60)
    print(f"🤖 AGENT PRINCIPAL : {agent_name}")
    print(f"📝 DESCRIPTION     : {description}")
    print(f"⚙️  INSTRUCTIONS   : {instructions}")
    print("=" * 60 + "\n")
    
    # 1. Génération de la structure hiérarchique (1-5-25)
    structure = await generate_subagent_structure(agent_name, description, instructions)
    
    # 2. Instanciation de l'agent hiérarchique
    hierarchical_root = HierarchicalAgent(
        name=structure["name"],
        role=structure["role"],
        instructions=structure["instructions"],
        subagents_config=structure.get("subagents")
    )
    
    # 3. Exécution
    print("\n" + "=" * 60)
    print("🎬 DÉBUT DE L'EXÉCUTION DU RÉSEAU DE 31 AGENTS")
    print("=" * 60 + "\n")
    
    await hierarchical_root.execute(prompt)
    
    print("\n" + "=" * 60)
    print("🏁 FIN DE L'EXÉCUTION")
    print("=" * 60 + "\n")

def main():
    print("🚀 ==================================================== 🚀")
    print("🚀    LAUNCHEUR D'AGENTS HIÉRARCHIQUES ANTIGRAVITY    🚀")
    print("🚀  (1 Agent principal + 5 Niv-1 + 25 Niv-2 = 31 agents) 🚀")
    print("🚀 ==================================================== 🚀\n")

    # Sélection de la catégorie
    print("Sélectionnez une catégorie :")
    for key, (folder, label) in CATEGORIES.items():
        print(f"  {key}. {label}")
    
    cat_choice = input("\nVotre choix (1-9) : ").strip()
    if cat_choice not in CATEGORIES:
        print("❌ Choix invalide.")
        return

    folder, cat_label = CATEGORIES[cat_choice]
    agents_dir = os.path.join("agents", folder)

    if not os.path.exists(agents_dir):
        print(f"❌ Le dossier {agents_dir} n'existe pas.")
        return

    # Liste des agents dans la catégorie sélectionnée
    agent_files = [f for f in os.listdir(agents_dir) if f.endswith("_agent.py")]
    if not agent_files:
        print("❌ Aucun agent trouvé dans cette catégorie.")
        return

    print(f"\nAgents disponibles dans {cat_label} :")
    for idx, filename in enumerate(agent_files, 1):
        agent_name = filename.replace("_agent.py", "").replace("_", " ").title()
        print(f"  {idx}. {agent_name} ({filename})")

    agent_choice = input(f"\nSélectionnez l'agent (1-{len(agent_files)}) : ").strip()
    try:
        agent_idx = int(agent_choice) - 1
        if agent_idx < 0 or agent_idx >= len(agent_files):
            raise ValueError
    except ValueError:
        print("❌ Choix invalide.")
        return

    selected_file = agent_files[agent_idx]
    file_path = os.path.join(agents_dir, selected_file)
    agent_name = selected_file.replace("_agent.py", "").replace("_", " ").title()

    prompt = input("\nSaisissez votre demande / prompt : ").strip()
    if not prompt:
        prompt = "Fais un audit complet ou une démonstration de tes compétences."

    asyncio.run(launch_hierarchical_agent(agent_name, file_path, prompt))

if __name__ == "__main__":
    main()

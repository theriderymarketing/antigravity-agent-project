"""
Exemple 3 : Multi-agents — Orchestration de plusieurs agents.

Spawne plusieurs agents spécialisés pour travailler
sur différentes parties d'un projet en parallèle.
"""

import asyncio
import sys

from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig


async def spawn_agent(role: str, instructions: str, prompt: str) -> str:
    """Spawne un agent spécialisé et retourne sa réponse complète."""
    config = LocalAgentConfig(
        system_instructions=instructions,
        capabilities=CapabilitiesConfig(),
    )

    result = []
    async with Agent(config) as agent:
        response = await agent.chat(prompt)
        async for token in response:
            result.append(token)

    return "".join(result)


async def main():
    print("🚀 Lancement de 3 agents spécialisés en parallèle...\n")

    # Définition des agents spécialisés
    agents = [
        {
            "role": "🔍 Auditeur Sécurité",
            "instructions": (
                "Tu es un expert en sécurité informatique. "
                "Analyse le code pour identifier les vulnérabilités, "
                "les failles potentielles et les bonnes pratiques manquantes."
            ),
            "prompt": "Fais un audit de sécurité complet de ce projet.",
        },
        {
            "role": "📊 Analyste Performance",
            "instructions": (
                "Tu es un expert en performance et optimisation. "
                "Identifie les goulots d'étranglement, les fuites mémoire "
                "potentielles et les optimisations possibles."
            ),
            "prompt": "Analyse les performances de ce projet et suggère des optimisations.",
        },
        {
            "role": "📝 Rédacteur Documentation",
            "instructions": (
                "Tu es un technical writer expert. "
                "Génère une documentation claire et complète pour le projet."
            ),
            "prompt": "Génère un README.md complet pour ce projet avec installation, usage et API.",
        },
    ]

    # Exécution parallèle de tous les agents
    tasks = [
        spawn_agent(a["role"], a["instructions"], a["prompt"])
        for a in agents
    ]
    results = await asyncio.gather(*tasks)

    # Affichage des résultats
    for agent_def, result in zip(agents, results):
        print(f"\n{'=' * 60}")
        print(f"{agent_def['role']}")
        print(f"{'=' * 60}")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())

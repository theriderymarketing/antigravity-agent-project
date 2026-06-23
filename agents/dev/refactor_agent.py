"""
Agent de refactoring expert.

Analyse le codebase pour détecter les code smells et applique
les principes SOLID pour améliorer la qualité et la maintenabilité
du code. Dispose d'un accès en écriture pour effectuer les
modifications directement.
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent de refactoring."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert en refactoring et en architecture logicielle. "
            "Tu analyses le codebase pour détecter les code smells, "
            "les violations des principes SOLID, le code dupliqué, "
            "les fonctions trop longues et les dépendances mal gérées. "
            "Tu proposes et appliques des refactorisations concrètes "
            "en expliquant le principe SOLID ou le pattern de conception "
            "qui justifie chaque modification."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Analyse le codebase actuel pour identifier les code smells "
            "et les violations des principes SOLID. Propose et applique "
            "les refactorisations nécessaires."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

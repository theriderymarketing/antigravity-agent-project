"""
Agent de génération de tests unitaires.

Analyse le codebase pour générer automatiquement des tests
unitaires pytest couvrant les cas nominaux, les cas limites
et les cas d'erreur. Dispose d'un accès en écriture pour
créer les fichiers de tests.
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent de génération de tests."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert en tests logiciels spécialisé en pytest. "
            "Tu analyses le codebase pour identifier les fonctions, "
            "classes et modules à tester. Pour chacun, tu génères "
            "des tests unitaires couvrant les cas nominaux, les cas "
            "limites et les cas d'erreur. Tu utilises les fixtures "
            "pytest, le paramétrage et les mocks quand nécessaire. "
            "Tu crées les fichiers de tests dans le répertoire approprié "
            "en respectant la convention de nommage test_*.py."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Analyse le codebase actuel et génère des tests unitaires "
            "pytest complets pour les modules identifiés. Couvre les cas "
            "nominaux, les cas limites et les cas d'erreur."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

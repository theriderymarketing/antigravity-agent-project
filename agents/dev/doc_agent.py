"""
Agent de génération de documentation.

Analyse le codebase pour produire automatiquement des docstrings,
des fichiers README et de la documentation d'API. Dispose d'un
accès en écriture pour créer et mettre à jour les fichiers
de documentation.
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent de documentation."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert en documentation technique. "
            "Tu analyses le codebase pour générer une documentation "
            "complète et de qualité professionnelle. Cela inclut : "
            "les docstrings pour chaque module, classe et fonction, "
            "un fichier README.md structuré avec description du projet, "
            "instructions d'installation et d'utilisation, ainsi que "
            "la documentation d'API au format standard. "
            "Tu rédiges en français sauf si le code existant est "
            "documenté en anglais."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Analyse le codebase actuel et génère la documentation "
            "complète : docstrings, README.md et documentation d'API. "
            "Crée ou mets à jour les fichiers nécessaires."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

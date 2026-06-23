"""
Agent de débogage expert.

Analyse le codebase pour identifier et corriger les bugs à partir
de messages d'erreur fournis par l'utilisateur. Dispose d'un accès
en écriture pour appliquer directement les corrections.
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent de débogage."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert en débogage logiciel. "
            "Lorsqu'on te fournit un message d'erreur ou un traceback, "
            "tu analyses le codebase pour identifier la cause racine du bug. "
            "Tu proposes un diagnostic détaillé, puis tu appliques "
            "les corrections nécessaires directement dans le code. "
            "Tu expliques chaque modification effectuée."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Analyse le codebase actuel et identifie les bugs potentiels "
            "ou les erreurs courantes. Fournis un rapport détaillé."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

"""
Exemple 1 : Analyse de codebase.

Demande à l'agent d'analyser la structure d'un projet
et de fournir un rapport détaillé.
"""

import asyncio
import sys

from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig


async def main():
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un architecte logiciel senior. "
            "Analyse en profondeur la structure du codebase, "
            "identifie les patterns utilisés, les dépendances, "
            "et fournis un rapport structuré avec des recommandations."
        ),
        # Pas de CapabilitiesConfig() → mode lecture seule (plus sûr pour l'analyse)
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Analyse ce projet : structure des fichiers, technologies utilisées, "
            "architecture, et donne-moi un rapport complet avec des suggestions "
            "d'amélioration."
        )

        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

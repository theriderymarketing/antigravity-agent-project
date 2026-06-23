"""
Agent de revue de code.

Effectue une revue de code approfondie en analysant la qualité,
les conventions de nommage et les vulnérabilités de sécurité.
Fonctionne en lecture seule sans modifier le codebase.
"""

import asyncio
import sys

from google.antigravity import Agent, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent de revue de code."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert en revue de code. "
            "Tu analyses le codebase en évaluant la qualité générale, "
            "les conventions de nommage, la lisibilité, la cohérence "
            "du style et les potentielles vulnérabilités de sécurité. "
            "Tu fournis un rapport structuré avec des recommandations "
            "classées par niveau de sévérité (critique, majeur, mineur). "
            "Tu ne modifies jamais le code, tu te contentes d'observer "
            "et de rapporter."
        ),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Effectue une revue de code complète du codebase actuel. "
            "Évalue la qualité, le nommage, le style et la sécurité. "
            "Fournis un rapport structuré avec tes recommandations."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

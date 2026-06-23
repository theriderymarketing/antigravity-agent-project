"""
Agent d'audit de sécurité.

Analyse le code source à la recherche de vulnérabilités, secrets codés en dur,
failles d'injection et mauvaises pratiques de sécurité. Fonctionne en lecture seule
pour garantir qu'aucune modification n'est apportée au code analysé.
"""

import asyncio
import sys

from google.antigravity import Agent, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent d'audit de sécurité."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un auditeur de sécurité expert. Ton rôle est d'analyser le code source "
            "pour identifier les vulnérabilités potentielles, les secrets codés en dur "
            "(clés API, mots de passe, tokens), les failles d'injection (SQL, XSS, commande), "
            "les problèmes de gestion des dépendances, et les mauvaises pratiques de sécurité. "
            "Tu fournis un rapport structuré avec le niveau de sévérité (critique, élevé, moyen, faible), "
            "la localisation précise du problème, une explication claire, et une recommandation "
            "de remédiation. Tu ne modifies jamais le code, tu analyses uniquement."
        ),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Effectue un audit de sécurité complet du projet courant. "
            "Recherche les vulnérabilités, les secrets codés en dur, "
            "les failles d'injection et les mauvaises pratiques de sécurité. "
            "Produis un rapport détaillé avec les recommandations de remédiation."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

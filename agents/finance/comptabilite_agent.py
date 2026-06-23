"""
Agent comptable expert utilisant le SDK Google Antigravity.

Maîtrise le Plan Comptable Général (PCG), les écritures comptables,
le bilan, le compte de résultat, la TVA et les liasses fiscales.
Analyse des documents financiers et propose des optimisations comptables.

Accès en écriture activé via CapabilitiesConfig pour la génération
de documents et écritures comptables.
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent comptable."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert-comptable français hautement qualifié. "
            "Tu maîtrises parfaitement le Plan Comptable Général (PCG) et ses classes de comptes "
            "(classe 1 à 7). Tu sais rédiger des écritures comptables en partie double, "
            "établir un bilan (actif/passif), un compte de résultat (charges/produits), "
            "et préparer les liasses fiscales (formulaires 2050 à 2059). "
            "Tu connais les règles de TVA (collectée, déductible, à décaisser) et les différents "
            "taux applicables en France (20%, 10%, 5.5%, 2.1%). "
            "Tu analyses les documents financiers, détectes les anomalies et proposes des "
            "optimisations comptables dans le respect de la réglementation en vigueur. "
            "Tu rédiges toujours tes réponses en français avec rigueur et précision."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Analyse la structure type d'un bilan comptable selon le PCG français. "
            "Présente les grandes masses de l'actif et du passif, les principaux comptes "
            "impliqués, et propose des points de vigilance pour la clôture annuelle."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

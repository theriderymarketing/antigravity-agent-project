"""
Agent business plan utilisant le SDK Google Antigravity.

Génère des business plans complets incluant : executive summary, étude de
marché, prévisions financières, plan de financement et calcul du seuil de
rentabilité.

Accès en écriture activé via CapabilitiesConfig pour la génération
de documents structurés.
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent business plan."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un consultant senior en stratégie d'entreprise, spécialisé dans la rédaction "
            "de business plans professionnels et complets. "
            "Tu structures chaque business plan avec les sections suivantes : "
            "1) Executive Summary (résumé exécutif percutant), "
            "2) Présentation de l'entreprise et de l'équipe fondatrice, "
            "3) Étude de marché (taille du marché, tendances, analyse concurrentielle, SWOT, "
            "segmentation, positionnement), "
            "4) Stratégie commerciale et marketing (mix marketing, canaux d'acquisition, pricing), "
            "5) Prévisions financières sur 3 à 5 ans (compte de résultat prévisionnel, "
            "plan de trésorerie, bilan prévisionnel), "
            "6) Plan de financement (besoins, sources, tableau emplois-ressources), "
            "7) Seuil de rentabilité (point mort en volume et en valeur), "
            "8) Analyse des risques et plan de contingence. "
            "Tu utilises des données de marché réalistes et tu justifies toutes tes hypothèses. "
            "Tu rédiges en français avec un style professionnel adapté aux investisseurs et banquiers."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Génère la structure complète d'un business plan pour une startup SaaS B2B "
            "spécialisée dans l'automatisation comptable par intelligence artificielle. "
            "Inclus l'executive summary, l'étude de marché, les prévisions financières "
            "sur 3 ans et le calcul du seuil de rentabilité."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

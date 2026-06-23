"""
Agent fiscaliste expert utilisant le SDK Google Antigravity.

Expert en fiscalité française et internationale : Impôt sur les Sociétés (IS),
Impôt sur le Revenu (IR), TVA, Crédit d'Impôt Recherche (CIR), statut Jeune
Entreprise Innovante (JEI), conventions fiscales internationales, prix de
transfert et optimisation fiscale légale.

Mode lecture seule — analyse et conseil uniquement, sans génération de documents.
"""

import asyncio
import sys

from google.antigravity import Agent, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent fiscaliste."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un fiscaliste expert spécialisé en droit fiscal français et international. "
            "Tu maîtrises l'Impôt sur les Sociétés (IS, taux normal et réduit PME), "
            "l'Impôt sur le Revenu (IR, barème progressif, prélèvement à la source), "
            "la TVA (régimes réel normal, simplifié, franchise en base), "
            "le Crédit d'Impôt Recherche (CIR, dépenses éligibles, calcul, déclaration 2069-A), "
            "et le statut Jeune Entreprise Innovante (JEI, exonérations sociales et fiscales). "
            "Tu connais les conventions fiscales bilatérales de la France, les règles de prix "
            "de transfert (principes OCDE, documentation, méthodes de détermination), "
            "et les stratégies d'optimisation fiscale légale (holding, intégration fiscale, "
            "régime mère-fille, patent box). "
            "Tu fournis des analyses détaillées et des conseils stratégiques en français, "
            "toujours dans le cadre légal et réglementaire en vigueur."
        ),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Présente une analyse comparative des dispositifs CIR et JEI pour une startup "
            "technologique française. Détaille les conditions d'éligibilité, les avantages "
            "fiscaux et sociaux, ainsi que les points de vigilance pour le cumul des deux dispositifs."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

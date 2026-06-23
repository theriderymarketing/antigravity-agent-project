"""
Agent Estimateur Immobilier
===========================

Analyse la valeur d'un bien immobilier en se basant sur les comparables,
le prix au mètre carré, les tendances du marché local, ainsi que les
facteurs de valorisation et de dévalorisation.

Agent en lecture seule (pas de CapabilitiesConfig).
"""

import asyncio
import sys

from google.antigravity import Agent, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent estimateur immobilier."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert estimateur immobilier français hautement qualifié. "
            "Ton rôle est d'analyser la valeur d'un bien immobilier avec précision et rigueur.\n\n"
            "Pour chaque estimation, tu dois :\n"
            "1. **Analyse des comparables** : Identifier des biens similaires vendus récemment "
            "dans le même secteur géographique (même quartier, même type de bien, surface comparable).\n"
            "2. **Prix au m²** : Calculer et comparer le prix au mètre carré par rapport aux "
            "moyennes du quartier, de la ville et du département.\n"
            "3. **Tendances du marché local** : Analyser l'évolution des prix sur 1, 3 et 5 ans, "
            "le volume de transactions, le délai moyen de vente, et la tension locative.\n"
            "4. **Facteurs de valorisation** : Proximité transports, commerces, écoles ; "
            "état général du bien ; prestations (parking, balcon, terrasse, cave) ; "
            "performance énergétique (DPE) ; luminosité et orientation ; étage et vue.\n"
            "5. **Facteurs de dévalorisation** : Nuisances sonores, vis-à-vis, travaux à prévoir, "
            "copropriété en difficulté, servitudes, zone inondable, pollution.\n"
            "6. **Fourchette d'estimation** : Fournir une estimation basse, médiane et haute "
            "avec justification de chaque valeur.\n\n"
            "Présente tes résultats de manière structurée avec des tableaux comparatifs "
            "lorsque c'est pertinent. Utilise des données chiffrées et sourcées autant que possible. "
            "Réponds toujours en français."
        ),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Estime la valeur d'un appartement T3 de 65m² situé dans le 7ème arrondissement "
            "de Lyon, au 4ème étage avec ascenseur, balcon de 8m², cave, rénové en 2022, "
            "DPE classé C. L'immeuble est de style haussmannien, situé à 200m du métro. "
            "Fournis une analyse complète avec comparables, tendances du marché et fourchette d'estimation."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

"""
Agent Diagnostics Immobiliers
==============================

Expert en diagnostics immobiliers obligatoires en France :
DPE, amiante, plomb (CREP), termites, électricité, gaz, ERP (État des
Risques et Pollutions). Génère des rapports de conformité détaillés.

Agent avec accès en écriture (CapabilitiesConfig activé).
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent diagnostics immobiliers."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert en diagnostics immobiliers obligatoires en France. "
            "Tu maîtrises parfaitement la réglementation en vigueur et les normes applicables.\n\n"
            "**Diagnostics que tu couvres :**\n\n"
            "1. **DPE (Diagnostic de Performance Énergétique)** :\n"
            "   - Méthode 3CL-2021 (arrêté du 31 mars 2021).\n"
            "   - Classes énergie (A à G) et climat (A à G).\n"
            "   - Estimation des consommations et émissions de GES.\n"
            "   - Recommandations de travaux d'amélioration énergétique.\n"
            "   - Impact sur l'interdiction de location (classes F et G).\n\n"
            "2. **Amiante (DTA / DAPP)** :\n"
            "   - Repérage selon les listes A, B et C (décret du 3 juin 2011).\n"
            "   - Matériaux et produits contenant de l'amiante (MCA).\n"
            "   - Évaluation de l'état de conservation (N=1, N=2, N=3).\n"
            "   - Préconisations : surveillance, mesures d'empoussièrement, travaux.\n\n"
            "3. **Plomb (CREP - Constat de Risque d'Exposition au Plomb)** :\n"
            "   - Obligatoire pour les logements construits avant le 1er janvier 1949.\n"
            "   - Mesures par appareil à fluorescence X (concentration en mg/cm²).\n"
            "   - Seuil réglementaire : 1 mg/cm².\n\n"
            "4. **Termites** :\n"
            "   - Zones délimitées par arrêté préfectoral.\n"
            "   - Indices d'infestation et espèces identifiées.\n"
            "   - Validité : 6 mois.\n\n"
            "5. **Électricité** :\n"
            "   - Installations de plus de 15 ans.\n"
            "   - Points de contrôle selon la norme FD C 16-600.\n"
            "   - Anomalies classées (B1 à B11).\n\n"
            "6. **Gaz** :\n"
            "   - Installations de plus de 15 ans.\n"
            "   - Points de contrôle : tuyauteries, raccordements, ventilation, combustion.\n"
            "   - Anomalies : A1 (à risque), A2 (à corriger), DGI (Danger Grave Immédiat).\n\n"
            "7. **ERP (État des Risques et Pollutions)** :\n"
            "   - Risques naturels, miniers, technologiques, sismiques, radon.\n"
            "   - Basé sur les arrêtés préfectoraux et le plan de prévention.\n\n"
            "**Format des rapports :**\n"
            "Génère des rapports structurés avec : identification du bien, résultats par diagnostic, "
            "conclusions, recommandations et obligations du propriétaire. "
            "Indique systématiquement la durée de validité de chaque diagnostic. "
            "Réponds toujours en français."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Génère un rapport de conformité complet des diagnostics immobiliers pour un appartement "
            "T4 de 85m² construit en 1965, situé au 28 avenue Berthelot, 69007 Lyon. "
            "Le bien est destiné à la vente. L'installation électrique date de 1985, "
            "l'installation gaz de 1990. Le bien est situé en zone d'exposition au plomb "
            "et en zone termites. Fournis le rapport avec tous les diagnostics obligatoires, "
            "leur validité et les recommandations associées."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

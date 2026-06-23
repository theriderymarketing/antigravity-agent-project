"""
Agent Évaluation de Performance.

Cet agent est spécialisé dans la gestion de la performance et le
développement des collaborateurs. Il est capable de :
- Rédiger des grilles d'évaluation annuelle et semestrielle
- Définir des OKR (Objectives and Key Results) alignés sur la stratégie
- Identifier et structurer des KPI pertinents par fonction
- Concevoir des processus de feedback 360°
- Élaborer des plans de développement individuel (PDI)

L'agent dispose de capacités d'écriture pour générer des documents
d'évaluation directement exploitables.
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent évaluation de performance."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un agent expert en gestion de la performance et développement "
            "des talents. Tu maîtrises parfaitement :\n\n"
            "1. **Grilles d'évaluation** : Tu rédiges des grilles d'évaluation "
            "annuelle et semestrielle avec des critères pondérés, des échelles de "
            "notation (1 à 5 ou lettres A-E), des descripteurs comportementaux par "
            "niveau, et des sections pour l'auto-évaluation et l'évaluation manager.\n\n"
            "2. **OKR (Objectives and Key Results)** : Tu définis des OKR selon la "
            "méthodologie de John Doerr, alignés en cascade (entreprise → département "
            "→ équipe → individu). Chaque objectif est ambitieux et chaque key result "
            "est mesurable avec une cible chiffrée et un scoring 0.0-1.0.\n\n"
            "3. **KPI (Key Performance Indicators)** : Tu identifies les KPI pertinents "
            "par fonction (tech, commercial, marketing, RH, finance, opérations). Tu "
            "précises la formule de calcul, la fréquence de mesure, la source de données, "
            "et les seuils d'alerte (vert/orange/rouge).\n\n"
            "4. **Feedback 360°** : Tu conçois des processus de feedback 360° complets "
            "avec questionnaires par catégorie d'évaluateur (manager, pairs, N-1, "
            "parties prenantes), échelles de Likert, questions ouvertes, garantie "
            "d'anonymat, et restitution structurée.\n\n"
            "5. **Plans de développement individuel (PDI)** : Tu élabores des PDI avec "
            "diagnostic des compétences actuelles vs requises, objectifs de développement "
            "SMART, actions concrètes (formation, mentorat, projets transverses, lectures), "
            "calendrier, et indicateurs de progression.\n\n"
            "Tu réponds toujours en français. Tu favorises une culture du feedback "
            "continu et de la performance durable, pas uniquement l'évaluation annuelle. "
            "Tu connais les biais d'évaluation courants (halo, récence, tendance centrale) "
            "et proposes des mécanismes pour les atténuer."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Présente-toi brièvement en tant qu'agent évaluation de performance, puis "
            "crée un dispositif complet de gestion de la performance pour une équipe "
            "Engineering de 20 personnes dans une entreprise SaaS B2B. Inclus : "
            "3 OKR trimestriels pour l'équipe, 5 KPI clés avec formules de calcul, "
            "une grille d'évaluation semestrielle pour un Software Engineer, et un "
            "exemple de plan de développement individuel pour un développeur souhaitant "
            "évoluer vers un rôle de Tech Lead."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

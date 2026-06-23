"""
Agent Onboarding RH.

Cet agent est spécialisé dans la conception de parcours d'intégration
pour les nouveaux collaborateurs. Il est capable de :
- Créer des plans d'intégration complets et personnalisés
- Générer des check-lists d'onboarding par étape
- Construire des parcours 30-60-90 jours avec objectifs mesurables
- Rédiger de la documentation d'accueil (livret, guides)
- Mettre en place un système de buddy/parrainage structuré

L'agent dispose de capacités d'écriture pour générer tous les
documents d'intégration nécessaires.
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent onboarding."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un agent expert en onboarding et intégration des nouveaux "
            "collaborateurs. Tu maîtrises parfaitement :\n\n"
            "1. **Plans d'intégration** : Tu crées des plans d'intégration complets, "
            "personnalisés selon le poste, le niveau d'expérience et le département. "
            "Chaque plan inclut les acteurs impliqués (manager, RH, buddy, équipe), "
            "les étapes clés, et les livrables attendus.\n\n"
            "2. **Check-lists d'onboarding** : Tu génères des check-lists détaillées "
            "couvrant toutes les phases : pré-boarding (J-15 à J-1), premier jour (J1), "
            "première semaine (S1), premier mois (M1). Chaque item précise le responsable "
            "et le délai.\n\n"
            "3. **Parcours 30-60-90 jours** : Tu construis des parcours structurés avec "
            "des objectifs SMART pour chaque phase :\n"
            "   - J1-J30 : Découverte (culture, outils, processus, relations)\n"
            "   - J31-J60 : Montée en compétences (premiers livrables, autonomie)\n"
            "   - J61-J90 : Performance (contribution active, objectifs métier)\n\n"
            "4. **Documentation d'accueil** : Tu rédiges des livrets d'accueil, guides "
            "pratiques (outils internes, organigramme, valeurs, rituels d'équipe), et "
            "FAQ pour nouveaux arrivants.\n\n"
            "5. **Buddy system** : Tu structures un programme de parrainage avec profil "
            "idéal du buddy, guide du buddy, fréquence des points, grille de suivi, "
            "et indicateurs de réussite de l'intégration.\n\n"
            "Tu réponds toujours en français. Tu vises un onboarding qui maximise "
            "l'engagement et réduit le turnover en période d'essai. Tu t'appuies sur "
            "les meilleures pratiques (Google, GitLab, Buffer) adaptées au contexte "
            "français."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Présente-toi brièvement en tant qu'agent onboarding, puis crée un plan "
            "d'intégration complet pour un nouveau Chef de Projet Digital rejoignant "
            "une scale-up tech de 150 personnes à Lyon. Inclus : check-list pré-boarding, "
            "programme du jour J, parcours 30-60-90 jours avec objectifs SMART, et un "
            "guide pour le buddy assigné."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

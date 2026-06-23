"""
Agent Ingénieur Pédagogique.

Cet agent est spécialisé dans la conception de dispositifs de formation
professionnelle. Il est capable de :
- Créer des programmes de formation complets et structurés
- Concevoir des modules e-learning interactifs
- Élaborer des quiz d'évaluation et des tests de positionnement
- Construire des parcours de montée en compétences individualisés
- Définir des objectifs pédagogiques selon la taxonomie de Bloom

L'agent dispose de capacités d'écriture pour générer des contenus
pédagogiques directement exploitables.
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent ingénieur pédagogique."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un agent ingénieur pédagogique expert en formation professionnelle "
            "continue. Tu maîtrises parfaitement :\n\n"
            "1. **Programmes de formation** : Tu conçois des programmes de formation "
            "complets avec objectifs pédagogiques (taxonomie de Bloom), prérequis, "
            "durée, modalités (présentiel, distanciel, blended), contenu détaillé par "
            "module, et méthodes d'évaluation.\n\n"
            "2. **Modules e-learning** : Tu structures des modules e-learning avec "
            "découpage en séquences, activités interactives, ressources multimédia "
            "suggérées, et mécaniques de gamification (badges, progression).\n\n"
            "3. **Quiz d'évaluation** : Tu crées des quiz variés (QCM, QCU, vrai/faux, "
            "questions ouvertes, mises en situation) avec barèmes de notation, feedback "
            "correctif, et seuils de validation.\n\n"
            "4. **Parcours de montée en compétences** : Tu élabores des parcours "
            "individualisés de montée en compétences sur 3, 6 ou 12 mois, avec jalons, "
            "indicateurs de progression, et recommandations d'apprentissage.\n\n"
            "Tu respectes le cadre légal français de la formation professionnelle "
            "(CPF, plan de développement des compétences, VAE). Tu utilises les "
            "référentiels de compétences RNCP et France Compétences quand c'est pertinent. "
            "Tu réponds toujours en français avec des livrables structurés."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Présente-toi brièvement en tant qu'agent ingénieur pédagogique, puis "
            "conçois un programme de formation complet sur le thème 'Leadership et "
            "Management d'Équipe' pour des managers de proximité. Inclus : objectifs "
            "pédagogiques, découpage en modules (5 modules minimum), un exemple de "
            "quiz d'évaluation pour le premier module, et un parcours de montée en "
            "compétences sur 6 mois."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

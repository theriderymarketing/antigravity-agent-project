"""
Agent Créateur de Cours
========================

Conçoit des cours structurés avec objectifs pédagogiques alignés sur la
taxonomie de Bloom, activités d'apprentissage, évaluations formatives
et sommatives, et supports visuels.

Agent avec accès en écriture (CapabilitiesConfig activé).
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent créateur de cours."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un ingénieur pédagogique expert, spécialisé dans la conception de cours "
            "structurés et engageants. Tu appliques les meilleures pratiques en sciences de l'éducation.\n\n"
            "**Cadre pédagogique :**\n"
            "Tu utilises systématiquement la **taxonomie de Bloom révisée** (Anderson & Krathwohl, 2001) "
            "pour définir les objectifs d'apprentissage :\n"
            "1. **Mémoriser** : Reconnaître, lister, définir, identifier.\n"
            "2. **Comprendre** : Expliquer, résumer, interpréter, classifier.\n"
            "3. **Appliquer** : Utiliser, exécuter, implémenter, résoudre.\n"
            "4. **Analyser** : Différencier, organiser, attribuer, déconstruire.\n"
            "5. **Évaluer** : Vérifier, critiquer, juger, argumenter.\n"
            "6. **Créer** : Concevoir, planifier, produire, inventer.\n\n"
            "**Structure de chaque cours :**\n"
            "1. **En-tête** : Titre, niveau, prérequis, durée estimée.\n"
            "2. **Objectifs pédagogiques** : Formulés avec des verbes d'action mesurables, "
            "classés par niveau de Bloom.\n"
            "3. **Plan du cours** : Séquençage des contenus avec progression logique.\n"
            "4. **Contenu détaillé** : Explications claires, exemples concrets, "
            "cas pratiques, analogies.\n"
            "5. **Activités d'apprentissage** :\n"
            "   - Activités individuelles et collaboratives.\n"
            "   - Études de cas, mises en situation, projets.\n"
            "   - Exercices de difficulté progressive.\n"
            "6. **Évaluations** :\n"
            "   - Formatives : quiz de vérification, auto-évaluation.\n"
            "   - Sommatives : examen, projet final, présentation.\n"
            "   - Critères d'évaluation et grilles de notation.\n"
            "7. **Supports visuels** : Description de schémas, diagrammes, infographies "
            "à créer pour illustrer les concepts clés.\n"
            "8. **Ressources complémentaires** : Bibliographie, liens, lectures recommandées.\n\n"
            "**Principes de conception :**\n"
            "- Alignement constructif (Biggs) : cohérence objectifs-activités-évaluations.\n"
            "- Charge cognitive optimisée (Sweller) : segmentation, élimination du superflu.\n"
            "- Apprentissage actif : engagement de l'apprenant à chaque étape.\n"
            "- Différenciation pédagogique : adaptations pour différents niveaux.\n\n"
            "Réponds toujours en français."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Conçois un cours complet sur 'Introduction à Python pour la Data Science' "
            "destiné à des étudiants de niveau L3 en sciences. Durée totale : 30 heures "
            "(10 séances de 3 heures). Prérequis : bases en mathématiques et statistiques. "
            "Le cours doit couvrir : les fondamentaux Python, NumPy, Pandas, Matplotlib/Seaborn, "
            "et un projet final d'analyse de données. Inclus les objectifs de Bloom pour chaque séance, "
            "les activités, les évaluations et les supports visuels à préparer."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

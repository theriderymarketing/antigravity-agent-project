"""
Agent Générateur de Quiz
=========================

Crée des QCM (Questions à Choix Multiples), questions ouvertes et
exercices pratiques avec corrections détaillées, explications
pédagogiques et barème de notation.

Agent avec accès en écriture (CapabilitiesConfig activé).
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent générateur de quiz."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert en évaluation pédagogique, spécialisé dans la création "
            "de quiz et d'exercices de qualité professionnelle.\n\n"
            "**Types de questions que tu maîtrises :**\n\n"
            "1. **QCM (Questions à Choix Multiples)** :\n"
            "   - Réponse unique ou réponses multiples.\n"
            "   - Distracteurs plausibles et bien calibrés.\n"
            "   - Justification de la bonne réponse et explication de pourquoi "
            "   chaque distracteur est incorrect.\n\n"
            "2. **Questions ouvertes** :\n"
            "   - Questions courtes (réponse en quelques lignes).\n"
            "   - Questions de développement (réponse structurée).\n"
            "   - Corrigé type avec éléments de réponse attendus.\n\n"
            "3. **Exercices pratiques** :\n"
            "   - Exercices d'application directe.\n"
            "   - Études de cas.\n"
            "   - Problèmes à résoudre étape par étape.\n"
            "   - Correction détaillée avec méthodologie.\n\n"
            "4. **Vrai/Faux avec justification** :\n"
            "   - Affirmations précises, sans ambiguïté.\n"
            "   - Justification obligatoire pour chaque réponse.\n\n"
            "**Règles de conception :**\n"
            "- Chaque question est classée selon le niveau de la taxonomie de Bloom visé.\n"
            "- Les questions sont de difficulté progressive (facile → moyen → difficile).\n"
            "- Le barème est clairement indiqué pour chaque question.\n"
            "- Les corrections incluent des explications pédagogiques détaillées, "
            "pas uniquement la bonne réponse.\n"
            "- Les QCM respectent les bonnes pratiques : pas de double négation, "
            "pas d'indices involontaires, options de longueur similaire.\n"
            "- Indiquer le temps estimé pour chaque section.\n\n"
            "**Format de sortie :**\n"
            "Pour chaque quiz, fournis :\n"
            "1. L'énoncé complet (version étudiant, sans corrections).\n"
            "2. Le corrigé détaillé (version enseignant, avec barème et explications).\n\n"
            "Réponds toujours en français."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Crée un quiz complet sur le chapitre 'Les structures de données en Python' "
            "pour des étudiants de niveau L2 informatique. Le quiz doit contenir :\n"
            "- 10 QCM (3 faciles, 4 moyens, 3 difficiles)\n"
            "- 3 questions ouvertes\n"
            "- 2 exercices pratiques de code\n"
            "- 5 Vrai/Faux avec justification\n"
            "Durée totale : 1h30. Barème sur 40 points.\n"
            "Couvre : listes, tuples, dictionnaires, sets, compréhensions de listes, "
            "et complexité algorithmique des opérations. "
            "Fournis l'énoncé étudiant ET le corrigé enseignant."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

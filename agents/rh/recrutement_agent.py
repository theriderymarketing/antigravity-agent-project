"""
Agent Recruteur Expert RH.

Cet agent est spécialisé dans le recrutement et l'acquisition de talents.
Il est capable de :
- Rédiger des fiches de poste optimisées pour attirer les meilleurs candidats
- Analyser des CV et les évaluer selon des critères objectifs
- Préparer des grilles d'entretien structurées avec scoring
- Établir un scoring multicritère des candidats
- Proposer des stratégies de sourcing adaptées au marché

L'agent dispose de capacités d'écriture pour générer des documents
directement exploitables par les équipes RH.
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent recruteur."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un agent recruteur expert en ressources humaines, spécialisé dans "
            "l'acquisition de talents en France. Tu maîtrises parfaitement :\n\n"
            "1. **Rédaction de fiches de poste** : Tu rédiges des fiches de poste "
            "optimisées SEO pour les jobboards, incluant intitulé, missions, compétences "
            "requises (hard skills et soft skills), avantages, fourchette salariale, et "
            "éléments de marque employeur.\n\n"
            "2. **Analyse de CV** : Tu analyses les CV de manière structurée en évaluant "
            "l'adéquation avec le poste (formation, expérience, compétences techniques, "
            "compétences comportementales, mobilité). Tu attribues un score sur 100.\n\n"
            "3. **Grilles d'entretien structurées** : Tu prépares des grilles d'entretien "
            "avec des questions comportementales (méthode STAR), des mises en situation, "
            "et des critères d'évaluation pondérés.\n\n"
            "4. **Scoring de candidats** : Tu établis des tableaux comparatifs multicritères "
            "avec pondération configurable pour aider à la décision finale.\n\n"
            "Tu réponds toujours en français. Tu structures tes réponses avec des tableaux "
            "Markdown quand c'est pertinent. Tu respectes les principes de non-discrimination "
            "à l'embauche conformément au Code du travail français."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Présente-toi brièvement en tant qu'agent recruteur expert, puis donne un "
            "exemple de fiche de poste optimisée pour un poste de Développeur Full Stack "
            "Senior (Python/React) en CDI à Paris, incluant : intitulé, missions clés, "
            "compétences requises, avantages, et une grille de scoring candidat associée."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

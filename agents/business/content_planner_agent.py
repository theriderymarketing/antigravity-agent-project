"""
Agent Planification de Contenu — Stratège éditorial.

Crée des calendriers éditoriaux, des stratégies de contenu et des plans
de publication multi-canaux. CapabilitiesConfig activé pour l'écriture
de fichiers (export de calendriers, plans, etc.).
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


SYSTEM_INSTRUCTIONS = """\
Tu es un stratège de contenu expert francophone. Tu aides les équipes marketing
à planifier et structurer leur production de contenu. Tes compétences couvrent :

1. **Calendrier éditorial** — Crée des plannings de publication détaillés
   (hebdomadaires, mensuels, trimestriels) avec dates, sujets, formats
   et canaux de diffusion.
2. **Stratégie de contenu** — Définis les piliers de contenu, les personas cibles,
   le tone of voice et les objectifs mesurables (KPIs).
3. **Idéation** — Propose des idées de contenu originales et pertinentes
   en fonction du secteur d'activité et des tendances actuelles.
4. **Distribution multi-canal** — Recommande les canaux adaptés (blog, réseaux
   sociaux, newsletter, podcast, vidéo) et les formats optimaux pour chacun.
5. **Mesure et optimisation** — Suggère des métriques de suivi et des ajustements
   basés sur les performances passées.

Structure tes réponses sous forme de plans actionnables avec des tableaux
quand c'est pertinent. Réponds toujours en français.
"""

DEFAULT_PROMPT = (
    "Crée un calendrier éditorial pour le mois de juillet 2026 pour une startup "
    "SaaS B2B spécialisée dans les outils de productivité. La cible principale "
    "est constituée de responsables d'équipes tech (CTO, VP Engineering, Tech Leads). "
    "Les canaux à couvrir sont : blog, LinkedIn, newsletter hebdomadaire et Twitter/X. "
    "Inclus les thèmes, formats, dates de publication et objectifs pour chaque contenu."
)


async def main():
    """Point d'entrée principal de l'agent Planification de Contenu."""
    config = LocalAgentConfig(
        system_instructions=SYSTEM_INSTRUCTIONS,
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(DEFAULT_PROMPT)
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

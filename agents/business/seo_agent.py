"""
Agent SEO — Expert en optimisation pour les moteurs de recherche.

Analyse le contenu fourni pour évaluer les balises meta, la structure
des titres (h1-h6), la densité des mots-clés et les bonnes pratiques
SEO. Fonctionne en lecture seule (pas de CapabilitiesConfig).
"""

import asyncio
import sys

from google.antigravity import Agent, LocalAgentConfig


SYSTEM_INSTRUCTIONS = """\
Tu es un expert SEO francophone. Ton rôle est d'analyser le contenu qu'on te soumet
et de fournir un audit détaillé couvrant les points suivants :

1. **Balises meta** — Vérifie la présence et la qualité du title, de la meta description
   et des balises Open Graph.
2. **Structure des titres** — Analyse la hiérarchie des headings (h1 → h6) et signale
   les incohérences.
3. **Mots-clés** — Évalue la densité, le placement et la pertinence des mots-clés
   principaux et secondaires.
4. **Contenu** — Longueur, lisibilité, maillage interne et appels à l'action.
5. **Recommandations** — Propose des améliorations concrètes classées par priorité.

Réponds toujours en français et structure ta réponse avec des sections claires.
"""

DEFAULT_PROMPT = (
    "Analyse le contenu SEO suivant et fournis un audit complet avec "
    "des recommandations d'amélioration :\n\n"
    "Titre : Guide complet du référencement naturel en 2026\n"
    "Meta description : Découvrez les meilleures pratiques SEO pour "
    "améliorer votre visibilité en ligne.\n"
    "Contenu : Le référencement naturel est essentiel pour toute "
    "stratégie digitale. Dans cet article, nous abordons les techniques "
    "on-page, off-page et techniques pour optimiser votre site web."
)


async def main():
    """Point d'entrée principal de l'agent SEO."""
    config = LocalAgentConfig(
        system_instructions=SYSTEM_INSTRUCTIONS,
    )

    async with Agent(config) as agent:
        response = await agent.chat(DEFAULT_PROMPT)
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

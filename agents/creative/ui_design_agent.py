"""
Agent d'analyse UI/UX.

Cet agent est un designer UI/UX spécialisé dans l'analyse de code frontend.
Il examine les fichiers HTML, CSS et JavaScript pour proposer des améliorations
en matière de design, d'accessibilité (WCAG), de responsive design et
d'expérience utilisateur.

Fonctionne en mode lecture seule — il analyse le code sans le modifier.
"""

import asyncio
import sys

from google.antigravity import Agent, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent d'analyse UI/UX."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert en design UI/UX spécialisé dans l'analyse "
            "de code frontend. Ton rôle est d'examiner les fichiers du projet "
            "(HTML, CSS, JavaScript, frameworks frontend) et de fournir des "
            "recommandations détaillées.\n\n"
            "Tes domaines d'expertise :\n"
            "1. **Design visuel** : hiérarchie visuelle, typographie, palette "
            "de couleurs, espacement, cohérence des composants.\n"
            "2. **Accessibilité (WCAG 2.1)** : attributs ARIA, contraste des "
            "couleurs, navigation au clavier, lecteurs d'écran, textes "
            "alternatifs.\n"
            "3. **Responsive design** : media queries, layouts flexibles, "
            "approche mobile-first, points de rupture.\n"
            "4. **Expérience utilisateur** : flux de navigation, micro-"
            "interactions, temps de chargement perçu, feedback utilisateur.\n"
            "5. **Bonnes pratiques** : sémantique HTML5, organisation CSS, "
            "performance du rendu, animations fluides.\n\n"
            "Pour chaque analyse :\n"
            "- Identifie les problèmes par ordre de priorité (critique, "
            "important, mineur).\n"
            "- Propose des solutions concrètes avec des exemples de code.\n"
            "- Cite les standards et guidelines pertinents.\n\n"
            "Tu travailles en lecture seule : tu analyses et recommandes, "
            "mais tu ne modifies pas les fichiers.\n"
            "Réponds toujours en français."
        ),
    )

    async with Agent(config) as agent:
        print("🎨 Agent d'Analyse UI/UX")
        print("=" * 40)
        print("Analyse du projet en cours...\n")

        response = await agent.chat(
            "Analyse les fichiers frontend du projet actuel. "
            "Examine le HTML, le CSS et le JavaScript pour identifier "
            "les améliorations possibles en matière de :\n"
            "1. Design visuel et cohérence\n"
            "2. Accessibilité (WCAG 2.1)\n"
            "3. Responsive design\n"
            "4. Expérience utilisateur générale\n\n"
            "Fournis un rapport structuré avec des recommandations "
            "priorisées et des exemples de code correctif."
        )

        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

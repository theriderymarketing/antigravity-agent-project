"""
Agent Copywriting — Rédacteur marketing spécialisé.

Génère du contenu marketing (emails, posts réseaux sociaux, pages de vente)
à partir d'un brief et d'un ton spécifiés via argparse.
CapabilitiesConfig activé pour l'écriture de fichiers.
"""

import argparse
import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


SYSTEM_INSTRUCTIONS = """\
Tu es un copywriter professionnel francophone. Tu maîtrises les techniques
de rédaction persuasive (AIDA, PAS, storytelling) et tu adaptes ton style
au ton demandé.

Selon le type de contenu demandé, tu produis :
- **Email marketing** — Objet accrocheur, corps engageant, CTA clair.
- **Post réseaux sociaux** — Texte optimisé pour la plateforme cible avec
  hashtags pertinents et emojis dosés.
- **Page de vente** — Titre percutant, bénéfices client, preuve sociale,
  appel à l'action.
- **Slogan / Accroche** — Court, mémorable et aligné avec le positionnement
  de la marque.

Respecte toujours le brief fourni. Réponds en français sauf demande contraire.
"""


def parse_arguments():
    """Analyse les arguments de la ligne de commande."""
    parser = argparse.ArgumentParser(
        description="Agent Copywriting — Génère du contenu marketing personnalisé.",
    )
    parser.add_argument(
        "--brief",
        type=str,
        default="Rédige un email promotionnel pour le lancement d'une nouvelle "
        "application de productivité destinée aux freelances.",
        help="Le brief décrivant le contenu à produire (défaut : email promo app).",
    )
    parser.add_argument(
        "--tone",
        type=str,
        default="professionnel et enthousiaste",
        choices=[
            "professionnel et enthousiaste",
            "décontracté et amical",
            "luxe et exclusif",
            "urgent et direct",
            "inspirant et motivant",
        ],
        help="Le ton à adopter pour la rédaction (défaut : professionnel et enthousiaste).",
    )
    return parser.parse_args()


async def main():
    """Point d'entrée principal de l'agent Copywriting."""
    args = parse_arguments()

    config = LocalAgentConfig(
        system_instructions=SYSTEM_INSTRUCTIONS,
        capabilities=CapabilitiesConfig(),
    )

    prompt = (
        f"Brief : {args.brief}\n"
        f"Ton souhaité : {args.tone}\n\n"
        "Génère le contenu demandé en respectant le brief et le ton indiqués."
    )

    async with Agent(config) as agent:
        response = await agent.chat(prompt)
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

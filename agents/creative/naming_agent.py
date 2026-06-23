"""
Agent expert en naming.

Cet agent est spécialisé dans la génération de noms pour des projets,
des marques, des variables, des fonctions ou tout autre élément nécessitant
un nom pertinent et mémorable.

Accepte une description en argument via la ligne de commande (argparse).
Fonctionne en mode lecture seule.
"""

import argparse
import asyncio
import sys

from google.antigravity import Agent, LocalAgentConfig


def parse_args():
    """Analyse les arguments de la ligne de commande."""
    parser = argparse.ArgumentParser(
        description="Agent expert en naming — génère des noms créatifs "
        "et pertinents à partir d'une description.",
    )
    parser.add_argument(
        "description",
        type=str,
        help="Description de ce qui doit être nommé (projet, marque, "
        "variable, fonction, etc.).",
    )
    parser.add_argument(
        "-n",
        "--nombre",
        type=int,
        default=10,
        help="Nombre de propositions de noms à générer (défaut : 10).",
    )
    parser.add_argument(
        "-t",
        "--type",
        choices=["projet", "marque", "variable", "fonction", "classe", "autre"],
        default="projet",
        help="Type d'élément à nommer (défaut : projet).",
    )
    return parser.parse_args()


async def main():
    """Point d'entrée principal de l'agent de naming."""
    args = parse_args()

    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert en naming et en création de noms. "
            "Tu maîtrises les techniques suivantes :\n"
            "- Portmanteau : fusion de mots pour créer un néologisme.\n"
            "- Acronymes : construction de sigles mémorables.\n"
            "- Métaphores : noms évocateurs basés sur des images.\n"
            "- Étymologie : racines grecques, latines ou d'autres langues.\n"
            "- Sonorité : noms agréables à prononcer et mémorables.\n\n"
            "Pour chaque proposition de nom :\n"
            "1. Indique le nom proposé.\n"
            "2. Explique brièvement son origine ou sa logique.\n"
            "3. Évalue sa mémorabilité et sa pertinence.\n"
            "4. Vérifie qu'il est facile à prononcer et à écrire.\n\n"
            "Si le type est 'variable', 'fonction' ou 'classe', respecte "
            "les conventions de nommage du code (snake_case pour Python, "
            "camelCase pour JavaScript, PascalCase pour les classes).\n\n"
            "Réponds toujours en français."
        ),
    )

    async with Agent(config) as agent:
        print("✏️  Agent Expert en Naming")
        print("=" * 40)
        print(f"Type : {args.type}")
        print(f"Nombre de propositions : {args.nombre}")
        print(f"Description : {args.description}\n")

        prompt = (
            f"Génère exactement {args.nombre} propositions de noms "
            f"pour un élément de type '{args.type}' décrit comme suit :\n\n"
            f"« {args.description} »\n\n"
            "Pour chaque nom, fournis :\n"
            "- Le nom proposé\n"
            "- L'explication de son origine\n"
            "- Un score de mémorabilité (1 à 5)\n"
            "Classe les propositions de la plus pertinente à la moins pertinente."
        )

        response = await agent.chat(prompt)

        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

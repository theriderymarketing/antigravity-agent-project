"""
Agent de brainstorming créatif.

Cet agent est un expert en génération d'idées qui utilise des techniques
éprouvées comme SCAMPER (Substituer, Combiner, Adapter, Modifier, Proposer
d'autres usages, Éliminer, Réorganiser) et le mind mapping pour aider
l'utilisateur à explorer des pistes créatives.

Fonctionne en mode interactif pour un dialogue continu avec l'utilisateur.
"""

import asyncio
import sys

from google.antigravity import Agent, LocalAgentConfig
from google.antigravity.utils.interactive import run_interactive_loop


async def main():
    """Point d'entrée principal de l'agent de brainstorming."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert en brainstorming et en créativité. "
            "Tu maîtrises les techniques suivantes :\n"
            "- SCAMPER : Substituer, Combiner, Adapter, Modifier, Proposer "
            "d'autres usages, Éliminer, Réorganiser.\n"
            "- Mind mapping : organisation visuelle des idées en arborescence.\n"
            "- Pensée latérale : approches non conventionnelles.\n"
            "- Brainwriting : génération structurée d'idées.\n\n"
            "Pour chaque session de brainstorming :\n"
            "1. Commence par clarifier le sujet ou le problème.\n"
            "2. Propose une technique adaptée au contexte.\n"
            "3. Génère un maximum d'idées variées et originales.\n"
            "4. Organise les idées par thème ou priorité.\n"
            "5. Suggère des combinaisons et des pistes d'approfondissement.\n\n"
            "Réponds toujours en français. Sois enthousiaste, encourage "
            "la créativité et évite de juger les idées prématurément."
        ),
    )

    async with Agent(config) as agent:
        print("🧠 Agent de Brainstorming Créatif")
        print("=" * 40)
        print("Techniques disponibles : SCAMPER, Mind Mapping, Pensée latérale")
        print("Tapez 'quit' ou 'exit' pour quitter.\n")
        await run_interactive_loop(agent)


if __name__ == "__main__":
    asyncio.run(main())

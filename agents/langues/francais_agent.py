"""
Agent Expert en Langue & Culture Française.

Fournit des conseils de rédaction avancée, traduction, localisation
et analyse stylistique pour la langue française.
"""

import asyncio
import sys
from google.antigravity import Agent, LocalAgentConfig


async def main():
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert d'élite de la Langue et de la Culture Française. "
            "Ton but est d'accompagner l'utilisateur dans la rédaction de textes littéraires ou professionnels "
            "impeccables, d'effectuer des traductions précises et idiomatiques, de corriger la grammaire "
            "et de conseiller sur les registres de langue (soutenu, familier) et les subtilités régionales (France, Québec, Belgique, Suisse)."
            "Réponds toujours en français impeccable."
        )
    )

    prompt = (
        "Réécris ce paragraphe dans un style professionnel et percutant : 'Salut, on veut vous proposer notre appli "
        "parce qu'elle est super rapide et qu'elle va vous faire gagner plein de temps. Dites-nous si ça vous intéresse.'"
    )

    async with Agent(config) as agent:
        print(f"❓ Prompt: {prompt}\n")
        print("🧠 Réponse :")
        response = await agent.chat(prompt)
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

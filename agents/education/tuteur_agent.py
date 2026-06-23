"""
Agent Tuteur — Script interactif.

Un tuteur personnalisé et interactif utilisant la méthode socratique
pour enseigner divers concepts de manière interactive.
"""

import asyncio
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig
from google.antigravity.utils.interactive import run_interactive_loop


async def main():
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un tuteur personnalisé et extrêmement pédagogue. "
            "Ton but est d'accompagner l'étudiant dans son apprentissage. "
            "N'explique pas directement la réponse : utilise la méthode socratique, "
            "pose des questions guidantes, propose des analogies simples et encourage "
            "l'étudiant. Reste toujours patient, bienveillant et instructif."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        print("🎓 Bienvenue dans votre session de tutorat interactif. Que souhaitez-vous apprendre aujourd'hui ?")
        await run_interactive_loop(agent)


if __name__ == "__main__":
    asyncio.run(main())

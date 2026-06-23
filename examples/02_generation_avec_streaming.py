"""
Exemple 2 : Génération de code avec streaming du raisonnement.

Montre comment streamer les pensées de l'agent ET les appels d'outils
pendant qu'il génère du code.
"""

import asyncio
import sys

from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig


async def main():
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un développeur Python expert. "
            "Tu écris du code propre, bien documenté et testé."
        ),
        capabilities=CapabilitiesConfig(),  # Autorise l'écriture de fichiers
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Crée un script Python qui implémente un serveur HTTP simple "
            "avec un endpoint /health qui retourne un JSON avec le status "
            "et le timestamp actuel."
        )

        # Stream les pensées de l'agent (raisonnement interne)
        print("=" * 60)
        print("🧠 RAISONNEMENT DE L'AGENT")
        print("=" * 60)
        async for thought in response.thoughts:
            print(f"  💭 {thought}")

        # Stream les appels d'outils
        print("\n" + "=" * 60)
        print("🔧 APPELS D'OUTILS")
        print("=" * 60)
        async for call in response.tool_calls:
            print(f"  ⚙️  {call.name}({call.args})")

        # Stream la réponse finale
        print("\n" + "=" * 60)
        print("📝 RÉPONSE")
        print("=" * 60)
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

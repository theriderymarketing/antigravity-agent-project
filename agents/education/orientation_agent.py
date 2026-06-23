"""
Agent Conseiller d'Orientation.

Analyse le profil de l'utilisateur (compétences, intérêts, valeurs)
et lui propose des parcours d'études et des carrières adaptées.
"""

import asyncio
import sys
from google.antigravity import Agent, LocalAgentConfig


async def main():
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un conseiller d'orientation académique et professionnelle expert. "
            "Analyse le profil fourni (passions, compétences, contraintes, intérêts) "
            "et propose des parcours de formation détaillés (études supérieures, bootcamps, "
            "auto-formation) ainsi que des débouchés professionnels pertinents."
        )
    )

    prompt = (
        "Voici mon profil : J'adore le développement web (surtout le frontend), j'ai du mal avec "
        "les mathématiques pures, je préfère l'apprentissage par la pratique et je souhaite "
        "trouver un emploi rapidement (idéalement en moins de 2 ans). Quelles sont mes options ?"
    )

    async with Agent(config) as agent:
        print(f"👤 Profil de test : {prompt}\n")
        print("💡 Propositions de l'agent d'orientation :")
        response = await agent.chat(prompt)
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

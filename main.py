"""
Agent Antigravity — Script principal.

Lance un agent Antigravity en mode interactif ou en one-shot
pour analyser, modifier ou naviguer dans un codebase.
"""

import asyncio
import argparse
import sys

from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig


async def one_shot(prompt: str) -> None:
    """Envoie un prompt unique à l'agent et affiche la réponse en streaming."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un assistant expert en développement logiciel. "
            "Tu analyses le code, proposes des améliorations et réponds "
            "de manière claire et concise en français."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(prompt)

        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


async def interactive() -> None:
    """Lance une boucle interactive de chat avec l'agent."""
    from google.antigravity.utils.interactive import run_interactive_loop

    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un assistant expert en développement logiciel. "
            "Tu analyses le code, proposes des améliorations et réponds "
            "de manière claire et concise en français."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        await run_interactive_loop(agent)


def main():
    parser = argparse.ArgumentParser(
        description="Agent Antigravity — Assistant IA pour codebase",
    )
    parser.add_argument(
        "-p", "--prompt",
        type=str,
        help="Prompt one-shot à envoyer à l'agent (sinon mode interactif)",
    )
    args = parser.parse_args()

    if args.prompt:
        asyncio.run(one_shot(args.prompt))
    else:
        asyncio.run(interactive())


if __name__ == "__main__":
    main()

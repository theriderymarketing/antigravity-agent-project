"""
Agente Experto en Lengua y Cultura Española.

Proporciona traducción avanzada, corrección de textos, localización
y análisis de matices culturales en el mundo hispanohablante.
"""

import asyncio
import sys
from google.antigravity import Agent, LocalAgentConfig


async def main():
    config = LocalAgentConfig(
        system_instructions=(
            "Eres un experto de élite en Lengua y Cultura Española. "
            "Tu propósito es ayudar al usuario con traducción precisa hacia y desde el español, "
            "redacción de textos profesionales, corrección gramatical y localización para "
            "diferentes países hispanohablantes (España, México, Argentina, Colombia, etc.). "
            "Responde siempre en un español claro y natural."
        )
    )

    prompt = (
        "Traduce esta frase al español de manera natural y formal: 'We look forward to collaborating with you on this project'. "
        "Luego, explica cómo cambiaría el tono si fuera para España o para México."
    )

    async with Agent(config) as agent:
        print(f"❓ Prompt: {prompt}\n")
        print("🧠 Respuesta:")
        response = await agent.chat(prompt)
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

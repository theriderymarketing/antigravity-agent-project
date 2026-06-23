"""
Agente Esperto in Lingua e Cultura Italiana.

Fornisce traduzione avanzata, revisione dei testi, localizzazione
e analisi delle sfumature culturali in Italia.
"""

import asyncio
import sys
from google.antigravity import Agent, LocalAgentConfig


async def main():
    config = LocalAgentConfig(
        system_instructions=(
            "Sei un esperto d'élite di Lingua e Cultura Italiana. "
            "Il tuo scopo è assistere l'utente con copywriting di alta qualità, "
            "traduzioni impeccabili da e verso l'italiano, correzione grammaticale "
            "e spiegazione delle sfumature culturali o espressioni idiomatiche locali. "
            "Rispondi sempre in un italiano chiaro, elegante e professionale."
        )
    )

    prompt = (
        "Traduci in italiano colloquiale ma naturale la frase: 'Don't worry about it, it's not a big deal'. "
        "Fornisci anche una versione formale adatta a un contesto lavorativo."
    )

    async with Agent(config) as agent:
        print(f"❓ Prompt: {prompt}\n")
        print("🧠 Risposta:")
        response = await agent.chat(prompt)
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

"""
English Language & Culture Expert Agent.

Provides advanced English copy editing, translation, localization,
and cultural nuance analysis.
"""

import asyncio
import sys
from google.antigravity import Agent, LocalAgentConfig


async def main():
    config = LocalAgentConfig(
        system_instructions=(
            "You are an elite English Language and Culture Expert. "
            "Your purpose is to assist the user with high-end copywriting, "
            "flawless translations to and from English, grammar refinement, "
            "and explaining complex cultural idioms or local nuances (US, UK, CA, AU). "
            "Always respond in clear, professional English."
        )
    )

    prompt = (
        "Translate this French idiom to natural English: 'Il ne faut pas vendre la peau de l'ours avant de l'avoir tué'. "
        "Also, explain its meaning and provide 3 common English equivalents."
    )

    async with Agent(config) as agent:
        print(f"❓ Prompt: {prompt}\n")
        print("🧠 Response:")
        response = await agent.chat(prompt)
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

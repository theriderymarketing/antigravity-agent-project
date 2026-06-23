"""
日本語と言葉の文化専門エージェント (Japanese Language & Culture Expert Agent).

高度な日本語の推敲、翻訳、ローカライズ、およびビジネスマナーや敬語の指導を提供します。
"""

import asyncio
import sys
from google.antigravity import Agent, LocalAgentConfig


async def main():
    config = LocalAgentConfig(
        system_instructions=(
            "You are an elite Japanese Language and Culture Expert. "
            "Your purpose is to assist the user with natural and professional Japanese writing, "
            "flawless translations (especially English/French to Japanese), Keigo (honorific speech) advice, "
            "and business etiquette localization. "
            "Always respond in clear, grammatically perfect, and polite Japanese."
        )
    )

    prompt = (
        "Translate this email opener to polite Japanese business Keigo: 'Hello, I'm writing to follow up on our meeting last week.'"
    )

    async with Agent(config) as agent:
        print(f"❓ Prompt: {prompt}\n")
        print("🧠 回答:")
        response = await agent.chat(prompt)
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

"""
中文语言与文化专家智能体 (Chinese Language & Culture Expert Agent).

提供高级中文文案润色、翻译、本地化、以及跨文化交流建议。
"""

import asyncio
import sys
from google.antigravity import Agent, LocalAgentConfig


async def main():
    config = LocalAgentConfig(
        system_instructions=(
            "You are an elite Chinese Language and Culture Expert. "
            "Your purpose is to assist the user with high-quality Chinese copywriting (Simplified and Traditional), "
            "idiomatic translations, grammar polishing, and explaining cultural nuances. "
            "Always respond in fluent, professional, and natural Chinese."
        )
    )

    prompt = (
        "将这句话翻译成得体、专业的中文商务表达：'We value your partnership and look forward to mutual growth.' "
        "并提供简体中文与繁体中文版本。"
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

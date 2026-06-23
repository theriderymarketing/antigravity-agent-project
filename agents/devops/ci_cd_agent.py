"""
Agent CI/CD.

Génère et optimise les pipelines d'intégration continue et de déploiement continu.
Crée des workflows GitHub Actions, des Dockerfiles, et des configurations de pipeline
adaptées aux besoins du projet.
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent CI/CD."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert en intégration continue et déploiement continu (CI/CD). "
            "Ton rôle est de concevoir et générer des pipelines CI/CD robustes et optimisés. "
            "Tu maîtrises GitHub Actions, GitLab CI, Docker, et les bonnes pratiques DevOps. "
            "Tu génères des workflows GitHub Actions complets (.github/workflows/), "
            "des Dockerfiles multi-étapes optimisés, des configurations de cache, "
            "des stratégies de tests parallèles, et des pipelines de déploiement "
            "avec gestion des environnements (staging, production). "
            "Tu suis les meilleures pratiques : images minimales, builds reproductibles, "
            "gestion des secrets via variables d'environnement, et notifications d'état."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Analyse le projet courant et génère une configuration CI/CD complète : "
            "workflow GitHub Actions pour les tests, le linting et le déploiement, "
            "ainsi qu'un Dockerfile multi-étapes optimisé pour la production."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

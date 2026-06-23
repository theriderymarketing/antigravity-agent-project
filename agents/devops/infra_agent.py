"""
Agent d'infrastructure.

Génère et gère les configurations d'infrastructure as code.
Produit des fichiers Terraform, Docker Compose et manifestes Kubernetes
adaptés aux besoins du projet.
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent d'infrastructure."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert en infrastructure as code (IaC). "
            "Ton rôle est de concevoir et générer des configurations d'infrastructure "
            "robustes, sécurisées et scalables. Tu maîtrises Terraform, Docker Compose, "
            "Kubernetes, et les principaux fournisseurs cloud (AWS, GCP, Azure). "
            "Tu génères des modules Terraform avec gestion d'état et verrouillage, "
            "des fichiers Docker Compose pour les environnements de développement "
            "et de production, des manifestes Kubernetes (Deployments, Services, "
            "ConfigMaps, Secrets, Ingress, HPA). Tu appliques les bonnes pratiques : "
            "principe du moindre privilège, isolation réseau, haute disponibilité, "
            "gestion des ressources, et étiquetage cohérent."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Analyse le projet courant et génère l'infrastructure nécessaire : "
            "fichiers Terraform pour le provisionnement cloud, "
            "Docker Compose pour l'environnement de développement local, "
            "et manifestes Kubernetes pour le déploiement en production."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

"""
Agent de monitoring.

Configure les systèmes de surveillance, de journalisation, d'alerting
et de vérification de santé pour les applications et l'infrastructure.
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent de monitoring."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert en observabilité et monitoring. "
            "Ton rôle est de mettre en place des systèmes complets de surveillance "
            "pour les applications et l'infrastructure. Tu maîtrises Prometheus, "
            "Grafana, ELK Stack, Loki, Datadog, et les outils d'alerting. "
            "Tu configures la collecte de métriques applicatives et système, "
            "la centralisation des logs avec rotation et rétention, "
            "les tableaux de bord Grafana avec les indicateurs clés (latence, erreurs, "
            "saturation, trafic — méthode RED/USE), les règles d'alerte avec escalade, "
            "et les health checks HTTP/TCP avec sondes de vivacité et de disponibilité. "
            "Tu suis les meilleures pratiques : alertes actionnables, réduction du bruit, "
            "corrélation logs-métriques-traces, et documentation des runbooks."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Analyse le projet courant et mets en place une configuration de monitoring "
            "complète : collecte de métriques, centralisation des logs, "
            "tableaux de bord, règles d'alerting et health checks."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

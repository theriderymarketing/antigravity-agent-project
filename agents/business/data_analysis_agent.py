"""
Agent Analyse de Données — Analyste data spécialisé.

Analyse des jeux de données au format CSV ou JSON pour en extraire
des insights, tendances et anomalies. Fonctionne en lecture seule
(pas de CapabilitiesConfig).
"""

import asyncio
import sys

from google.antigravity import Agent, LocalAgentConfig


SYSTEM_INSTRUCTIONS = """\
Tu es un analyste de données expert francophone. Tu analyses les jeux de données
(CSV, JSON) qu'on te soumet et tu fournis :

1. **Résumé statistique** — Nombre d'enregistrements, colonnes, types de données,
   valeurs manquantes et doublons.
2. **Analyse descriptive** — Moyennes, médianes, écarts-types, distributions
   et corrélations clés.
3. **Tendances et patterns** — Identifie les tendances temporelles, saisonnalités
   et regroupements significatifs.
4. **Anomalies** — Signale les valeurs aberrantes et les incohérences dans les données.
5. **Recommandations** — Propose des actions concrètes basées sur les insights
   découverts et suggère des visualisations pertinentes.

Structure ta réponse avec des sections claires. Utilise des tableaux quand c'est
pertinent. Réponds toujours en français.
"""

DEFAULT_PROMPT = """\
Analyse le jeu de données suivant (format CSV) et fournis un rapport complet :

mois,ventes,visiteurs,taux_conversion,panier_moyen
2026-01,12500,45000,2.8,85.50
2026-02,13200,47500,2.78,88.00
2026-03,15800,52000,3.04,92.30
2026-04,14100,49000,2.88,87.60
2026-05,16500,55000,3.0,95.10
2026-06,18200,61000,2.98,99.40

Identifie les tendances, anomalies éventuelles et propose des recommandations
pour optimiser les performances commerciales.
"""


async def main():
    """Point d'entrée principal de l'agent Analyse de Données."""
    config = LocalAgentConfig(
        system_instructions=SYSTEM_INSTRUCTIONS,
    )

    async with Agent(config) as agent:
        response = await agent.chat(DEFAULT_PROMPT)
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

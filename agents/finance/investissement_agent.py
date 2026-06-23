"""
Agent d'analyse d'investissement utilisant le SDK Google Antigravity.

Réalise des analyses financières avancées : ratios financiers (ROI, ROE,
EBITDA, marge nette), valorisation d'entreprise (DCF, méthode des multiples),
due diligence financière et analyse de risques.

Mode lecture seule — analyse et recommandations uniquement.
"""

import asyncio
import sys

from google.antigravity import Agent, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent analyse d'investissement."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un analyste financier senior spécialisé en analyse d'investissement "
            "et évaluation d'entreprise. "
            "Tu maîtrises les principaux ratios financiers : "
            "ROI (Return on Investment), ROE (Return on Equity), ROA (Return on Assets), "
            "EBITDA et marge d'EBITDA, marge nette, ratio d'endettement (Gearing, Debt/Equity), "
            "ratio de liquidité (current ratio, quick ratio), BFR (Besoin en Fonds de Roulement). "
            "Tu es expert en méthodes de valorisation d'entreprise : "
            "DCF (Discounted Cash Flow) avec calcul du WACC et de la valeur terminale, "
            "méthode des multiples (EV/EBITDA, P/E, EV/Sales) avec sélection de comparables, "
            "méthode patrimoniale (Actif Net Réévalué). "
            "Tu réalises des due diligences financières rigoureuses : analyse des états financiers "
            "historiques, normalisation des résultats, identification des risques (concentration "
            "clients, dépendance fournisseurs, litiges), qualité des revenus récurrents. "
            "Tu évalues les risques d'investissement (risque de marché, risque opérationnel, "
            "risque de crédit, risque de liquidité) et tu proposes des recommandations argumentées. "
            "Tu rédiges en français avec la rigueur attendue par des investisseurs institutionnels."
        ),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Réalise une analyse financière type pour évaluer une entreprise SaaS "
            "en phase de croissance. Détaille les ratios clés à examiner, propose une "
            "valorisation par DCF et par multiples (EV/EBITDA, EV/Revenue), "
            "et identifie les principaux facteurs de risque à surveiller."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

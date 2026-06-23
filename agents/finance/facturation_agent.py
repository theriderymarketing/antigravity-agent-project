"""
Agent facturation utilisant le SDK Google Antigravity.

Génère des factures conformes à la réglementation française (mentions
obligatoires), des devis et des avoirs. Gère la numérotation séquentielle,
les calculs de TVA, les conditions de paiement et les pénalités de retard.

Accès en écriture activé via CapabilitiesConfig pour la génération
de documents de facturation.
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent facturation."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert en facturation et gestion commerciale, parfaitement au fait "
            "de la réglementation française en matière de facturation. "
            "Tu génères des factures conformes avec toutes les mentions obligatoires : "
            "numéro de facture (séquence chronologique sans rupture), date d'émission, "
            "identité du vendeur (SIRET, adresse, forme juridique, capital social), "
            "identité de l'acheteur, numéros de TVA intracommunautaire, "
            "désignation détaillée des biens ou services, quantités, prix unitaire HT, "
            "taux de TVA applicables, montant HT, montant de TVA, montant TTC, "
            "conditions de paiement (délai, mode, escompte), "
            "mention des pénalités de retard et indemnité forfaitaire de recouvrement (40€). "
            "Tu sais aussi produire des devis (avec durée de validité et conditions) "
            "et des avoirs (référence à la facture d'origine, motif). "
            "Tu respectes les obligations liées à la facturation électronique "
            "(réforme e-invoicing en France). "
            "Tu rédiges tout en français avec une mise en forme professionnelle."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Génère un modèle de facture conforme pour une prestation de conseil en "
            "transformation digitale. Inclus toutes les mentions obligatoires, "
            "un calcul détaillé de la TVA à 20%, les conditions de paiement à 30 jours "
            "et les mentions légales relatives aux pénalités de retard."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

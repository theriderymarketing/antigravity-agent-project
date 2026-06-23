"""
Agent Rédacteur de Baux Immobiliers
====================================

Expert en droit immobilier français (loi ALUR, loi Pinel, loi Elan).
Rédige et analyse des baux d'habitation, commerciaux et professionnels,
ainsi que des états des lieux d'entrée et de sortie.

Agent avec accès en écriture (CapabilitiesConfig activé).
"""

import asyncio
import sys

from google.antigravity import Agent, CapabilitiesConfig, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent rédacteur de baux."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un expert en droit immobilier français, spécialisé dans la rédaction "
            "et l'analyse de baux. Tu maîtrises parfaitement :\n\n"
            "**Cadre juridique :**\n"
            "- Loi ALUR (24 mars 2014) : encadrement des loyers, garantie universelle, "
            "documents obligatoires, notice d'information.\n"
            "- Loi Pinel (18 juin 2014) : baux commerciaux, déplafonnement, état des lieux obligatoire.\n"
            "- Loi ELAN (23 novembre 2018) : bail mobilité, colocation, caution.\n"
            "- Code civil (articles 1713 à 1778) et loi du 6 juillet 1989.\n\n"
            "**Types de baux que tu maîtrises :**\n"
            "1. **Bail d'habitation** (vide ou meublé) : durée, loyer, charges, dépôt de garantie, "
            "clause résolutoire, congé, renouvellement.\n"
            "2. **Bail commercial (3-6-9)** : destination, loyer, révision triennale, droit au renouvellement, "
            "indemnité d'éviction, cession, sous-location.\n"
            "3. **Bail professionnel** : durée minimale 6 ans, résiliation, charges.\n"
            "4. **Bail mobilité** : durée 1-10 mois, conditions, interdiction de dépôt de garantie.\n\n"
            "**États des lieux :**\n"
            "- Rédaction conforme au décret du 30 mars 2016.\n"
            "- Description pièce par pièce : sols, murs, plafonds, menuiseries, équipements.\n"
            "- Grille de vétusté applicable.\n\n"
            "**Clauses obligatoires et facultatives :**\n"
            "Tu connais les clauses réputées non écrites (article 4 loi 1989) et sais "
            "rédiger des clauses particulières licites.\n\n"
            "Rédige des documents juridiquement solides, clairs et conformes à la législation en vigueur. "
            "Réponds toujours en français."
        ),
        capabilities=CapabilitiesConfig(),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Rédige un bail d'habitation meublé conforme à la loi ALUR pour un appartement T2 "
            "situé au 15 rue de la République, 69001 Lyon. Bailleur : Jean Dupont. "
            "Locataire : Marie Martin. Loyer : 750€/mois charges comprises (dont 50€ de provisions "
            "sur charges). Dépôt de garantie : 750€. Durée : 1 an renouvelable. "
            "Date d'entrée : 1er septembre 2025. Inclus toutes les clauses obligatoires "
            "et les annexes requises."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

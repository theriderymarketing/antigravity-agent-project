"""
Agent Droit du Travail.

Cet agent est spécialisé en droit social français. Il fonctionne en mode
lecture seule (read-only) et fournit des analyses juridiques sur :
- Les différents types de contrats de travail (CDI, CDD, intérim, freelance)
- Les procédures de licenciement et leurs motifs
- La rupture conventionnelle individuelle et collective
- Les conventions collectives et accords de branche
- Les obligations légales de l'employeur

⚠️ Cet agent fournit des informations à visée pédagogique et ne constitue
pas un conseil juridique personnalisé. Il est recommandé de consulter un
avocat spécialisé pour toute situation concrète.
"""

import asyncio
import sys

from google.antigravity import Agent, LocalAgentConfig


async def main():
    """Point d'entrée principal de l'agent droit du travail."""
    config = LocalAgentConfig(
        system_instructions=(
            "Tu es un agent expert en droit du travail français. Tu fonctionnes en "
            "mode consultation uniquement (read-only). Tu maîtrises parfaitement :\n\n"
            "1. **Contrats de travail** : CDI, CDD (motifs de recours, durée maximale, "
            "renouvellement, délai de carence), contrat d'intérim, contrat de freelance "
            "(auto-entrepreneur, portage salarial), contrat d'apprentissage et de "
            "professionnalisation. Tu cites les articles du Code du travail pertinents.\n\n"
            "2. **Licenciement** : Tu détailles les procédures de licenciement pour motif "
            "personnel (faute simple, grave, lourde, insuffisance professionnelle) et pour "
            "motif économique (individuel et collectif, PSE). Tu précises les délais, "
            "indemnités légales et conventionnelles, et les obligations de l'employeur.\n\n"
            "3. **Rupture conventionnelle** : Tu expliques la procédure complète "
            "(entretiens, convention, homologation DREETS), le calcul de l'indemnité "
            "spécifique, les délais de rétractation, et les cas particuliers (salariés "
            "protégés).\n\n"
            "4. **Conventions collectives** : Tu connais les principales conventions "
            "collectives (Syntec, métallurgie, commerce, BTP, HCR) et sais identifier "
            "les dispositions plus favorables que le Code du travail.\n\n"
            "5. **Obligations employeur** : DUERP, affichages obligatoires, registre du "
            "personnel, médecine du travail, CSE, égalité professionnelle, index égalité "
            "F/H, RGPD RH, télétravail.\n\n"
            "Tu cites systématiquement les articles de loi applicables (Code du travail, "
            "jurisprudence Cour de cassation). Tu précises toujours que tes réponses ont "
            "une valeur informative et ne constituent pas un conseil juridique personnalisé. "
            "Tu réponds toujours en français."
        ),
    )

    async with Agent(config) as agent:
        response = await agent.chat(
            "Présente-toi brièvement en tant qu'agent droit du travail, puis explique "
            "en détail la procédure de rupture conventionnelle individuelle en France : "
            "étapes, délais, calcul de l'indemnité, cas particuliers des salariés "
            "protégés, et les erreurs fréquentes à éviter. Cite les articles du Code "
            "du travail applicables."
        )
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


if __name__ == "__main__":
    asyncio.run(main())

# 🚀 Antigravity Agent Project

Projet Python qui utilise le **SDK Antigravity** pour piloter des agents IA programmatiquement — analyse de code, génération, multi-agents, et plus.

## 📦 Installation

```bash
# Cloner le repo
git clone https://github.com/<ton-user>/antigravity-agent-project.git
cd antigravity-agent-project

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

## 🎯 Utilisation

### Mode interactif (chat)

```bash
python main.py
```

Lance une boucle de chat interactive avec l'agent. Tape tes questions directement dans le terminal.

### Mode one-shot (prompt unique)

```bash
python main.py -p "Explique-moi l'architecture de ce projet"
```

Envoie un prompt unique et affiche la réponse en streaming.

## 📚 Exemples

| Script | Description |
|--------|-------------|
| `examples/01_analyse_codebase.py` | Analyse complète d'un codebase (mode lecture seule) |
| `examples/02_generation_avec_streaming.py` | Génération de code avec streaming des pensées et outils |
| `examples/03_multi_agents.py` | Orchestration de 3 agents spécialisés en parallèle |

### Lancer un exemple

```bash
python examples/01_analyse_codebase.py
```

## 🏗️ Structure du projet

```
antigravity-agent-project/
├── main.py                # Point d'entrée principal (interactif / one-shot)
├── requirements.txt       # Dépendances Python
├── .gitignore
├── README.md
└── examples/
    ├── 01_analyse_codebase.py            # Analyse read-only
    ├── 02_generation_avec_streaming.py   # Streaming pensées + outils
    └── 03_multi_agents.py               # Multi-agents parallèles
```

## ⚙️ Configuration

L'agent utilise par défaut le workspace courant (le dossier où tu lances le script). Pour modifier le comportement :

- **`system_instructions`** — Change les instructions système de l'agent
- **`CapabilitiesConfig()`** — Active les outils d'écriture (fichiers, commandes). Sans ce paramètre, l'agent est en **lecture seule**

## 📖 Documentation

- [SDK Antigravity (GitHub)](https://github.com/google-antigravity/antigravity-sdk-python)
- [Documentation Antigravity](https://antigravity.google/docs)

## 📄 Licence

MIT

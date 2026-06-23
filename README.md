# 🚀 Antigravity Agent Project

**Boîte à outils complète d'agents IA spécialisés**, propulsée par le [SDK Antigravity](https://github.com/google-antigravity/antigravity-sdk-python). 16 agents organisés en 4 catégories, prêts à l'emploi.

---

## 📦 Installation

```bash
# Cloner le repo
git clone https://github.com/theriderymarketing/antigravity-agent-project.git
cd antigravity-agent-project

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

---

## 🎯 Utilisation rapide

### Mode interactif (chat libre)

```bash
python main.py
```

### Mode one-shot (prompt unique)

```bash
python main.py -p "Explique-moi l'architecture de ce projet"
```

### Lancer un agent spécialisé

```bash
python agents/dev/debug_agent.py
python agents/business/seo_agent.py
python agents/devops/security_audit_agent.py
python agents/creative/brainstorm_agent.py
```

---

## 🤖 Catalogue des Agents

### 🔧 Dev — `agents/dev/`

| Agent | Fichier | Mode | Description |
|-------|---------|------|-------------|
| 🐛 Debugger | `debug_agent.py` | Read/Write | Analyse les bugs, identifie la cause racine, propose un fix |
| ♻️ Refactoring | `refactor_agent.py` | Read/Write | Détecte les code smells, applique SOLID |
| 🔍 Code Review | `code_review_agent.py` | Read-only | Revue qualité, naming, sécurité, performance |
| 🧪 Test Generator | `test_generator_agent.py` | Read/Write | Génère des tests pytest complets |
| 📝 Documentation | `doc_agent.py` | Read/Write | Génère docstrings, README, docs API |

### 💼 Business — `agents/business/`

| Agent | Fichier | Mode | Description |
|-------|---------|------|-------------|
| 🔎 SEO | `seo_agent.py` | Read-only | Analyse meta tags, headings, mots-clés |
| ✍️ Copywriting | `copywriting_agent.py` | Read/Write | Marketing copy, emails, posts sociaux |
| 📊 Data Analysis | `data_analysis_agent.py` | Read-only | Analyse CSV/JSON, stats, tendances |
| 📅 Content Planner | `content_planner_agent.py` | Read/Write | Calendriers éditoriaux, stratégies |

### ⚙️ DevOps — `agents/devops/`

| Agent | Fichier | Mode | Description |
|-------|---------|------|-------------|
| 🛡️ Sécurité | `security_audit_agent.py` | Read-only | Vulnérabilités, secrets, injections |
| 🔄 CI/CD | `ci_cd_agent.py` | Read/Write | GitHub Actions, Dockerfiles |
| 🏗️ Infrastructure | `infra_agent.py` | Read/Write | Terraform, Docker Compose, K8s |
| 📡 Monitoring | `monitoring_agent.py` | Read/Write | Logging, alerting, health checks |

### 🎨 Creative — `agents/creative/`

| Agent | Fichier | Mode | Description |
|-------|---------|------|-------------|
| 💡 Brainstorming | `brainstorm_agent.py` | Interactif | SCAMPER, mind mapping, idéation |
| 🎨 UI/UX Design | `ui_design_agent.py` | Read-only | Audit UI, accessibilité, responsive |
| 🏷️ Naming | `naming_agent.py` | Read-only | Noms de projets, marques, variables |

---

## 🏗️ Structure du projet

```
antigravity-agent-project/
├── main.py                     # Point d'entrée (interactif / one-shot)
├── requirements.txt            # Dépendances Python
├── README.md
├── .gitignore
├── examples/                   # Exemples d'utilisation du SDK
│   ├── 01_analyse_codebase.py
│   ├── 02_generation_avec_streaming.py
│   └── 03_multi_agents.py
└── agents/                     # 🤖 Agents spécialisés
    ├── dev/                    # Agents développement
    │   ├── debug_agent.py
    │   ├── refactor_agent.py
    │   ├── code_review_agent.py
    │   ├── test_generator_agent.py
    │   └── doc_agent.py
    ├── business/               # Agents business
    │   ├── seo_agent.py
    │   ├── copywriting_agent.py
    │   ├── data_analysis_agent.py
    │   └── content_planner_agent.py
    ├── devops/                 # Agents DevOps
    │   ├── security_audit_agent.py
    │   ├── ci_cd_agent.py
    │   ├── infra_agent.py
    │   └── monitoring_agent.py
    └── creative/               # Agents créatifs
        ├── brainstorm_agent.py
        ├── ui_design_agent.py
        └── naming_agent.py
```

---

## ⚙️ Configuration

| Paramètre | Description |
|-----------|-------------|
| `system_instructions` | Instructions système définissant l'expertise de l'agent |
| `CapabilitiesConfig()` | Active les outils d'écriture (fichiers, commandes). Sans = lecture seule |

### Modes d'exécution

- **Read-only** : L'agent analyse sans modifier le code (plus sûr)
- **Read/Write** : L'agent peut créer et modifier des fichiers
- **Interactif** : Boucle de chat continue avec l'agent

---

## 📖 Documentation

- [SDK Antigravity (GitHub)](https://github.com/google-antigravity/antigravity-sdk-python)
- [Documentation Antigravity](https://antigravity.google/docs)

## 📄 Licence

MIT

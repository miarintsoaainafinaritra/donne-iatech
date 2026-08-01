# Dashboard Qualité de l'Air - IA1

## Description

Dashboard interactif pour l'analyse de la qualité de l'air (AQI) à Madagascar.  
Projet réalisé dans le cadre du programme **IA1 - Databridge**.

---

## Structure du projet

```text
dashbord/
│
├── notebook/
│   └── analysis.ipynb
│
├── venv/
│   ├── bin/
│   ├── lib/
│   └── ...
│
├── .env.example
├── .gitignore
├── clean_data.csv
├── config.json
├── dashboard.py
├── README.md
└── requirements.txt
```

---

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- Python **3.12.3**
- pip
- Git

---

# Installation

## 1. Cloner le dépôt

```bash
git clone https://github.com/miarintsoaainafinaritra/donne-iatech.git
cd dashbord
```

## 2. Créer l'environnement virtuel

```bash
python3.12 -m venv venv

# ou
python3 -m venv venv
```

## 3. Activer l'environnement virtuel

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

## 4. Vérifier la version de Python

```bash
python --version
```

Résultat attendu :

```text
Python 3.12.3
```

## 5. Installer les dépendances

```bash
pip install -r requirements.txt
```

Si le fichier `requirements.txt` est absent :

```bash
pip install pandas matplotlib seaborn jupyter ipykernel streamlit numpy
```

---

# Dépendances

| Paquet | Version |
|---------|----------|
| pandas | >=1.5.0 |
| matplotlib | >=3.5.0 |
| seaborn | >=0.12.0 |
| numpy | >=1.23.0 |
| jupyter | >=1.0.0 |
| ipykernel | >=6.0.0 |
| streamlit | >=1.25.0 |

---

# Environnement Python

| Élément | Valeur |
|---------|--------|
| Python | 3.12.3 |
| Environnement | venv |
| Noyau Jupyter | Python 3.12.3 (venv) |

---

# Utilisation

## Lancer le Dashboard

```bash
streamlit run dashboard.py
```

Puis ouvrir :

```
http://localhost:8501
```

---

## Lancer Jupyter Notebook

### 1. Activer l'environnement virtuel

```bash
source venv/bin/activate
```

### 2. Ouvrir le notebook

```bash
jupyter notebook notebook/analysis.ipynb
```

ou

```bash
cd notebook
jupyter notebook analysis.ipynb
```

---

## Utilisation avec VS Code

1. Ouvrir `notebook/analysis.ipynb`
2. Cliquer sur le noyau en haut à droite.
3. Sélectionner :

```text
Python 3.12.3 ('venv': venv)
```

ou

```text
venv (3.12.3) ./venv/bin/python
```

Puis cliquer sur **Run All**.

---

# Données

| Élément | Valeur |
|---------|--------|
| Villes | Antananarivo, Beijing, Nairobi, New Delhi, Paris |
| Nombre de lignes | 42 539 |
| Période | 2025-07-31 → 2026-07-30 |

---

# Résultats attendus

## Chargement

```text
42539 lignes chargées
5 villes
```

## Statistiques

| Ville | AQI Moyen | AQI Min | AQI Max |
|-------|-----------:|---------:|---------:|
| Beijing | 4.27 | 1 | 5 |
| New Delhi | 3.55 | 1 | 5 |
| Paris | 1.74 | 1 | 4 |
| Nairobi | 1.19 | 1 | 5 |
| Antananarivo | 1.14 | 1 | 3 |

---

# Graphiques

- Évolution de l'AQI par ville
- Distribution de l'AQI (Boxplot)
- Corrélation des polluants (Heatmap)
- AQI moyen par heure

---

# Insights

| Métrique | Résultat |
|----------|----------|
| Plus polluée | Beijing (AQI : 4.3) |
| Moins polluée | Antananarivo (AQI : 1.1) |
| Meilleure heure | 08 h |
| Pire heure | 15 h |

---

# Commandes utiles

| Commande | Description |
|----------|-------------|
| `python --version` | Vérifier Python |
| `source venv/bin/activate` | Activer le venv |
| `deactivate` | Désactiver le venv |
| `pip freeze > requirements.txt` | Générer requirements.txt |
| `jupyter notebook` | Lancer Jupyter |
| `jupyter lab` | Lancer JupyterLab |
| `jupyter server list` | Voir les serveurs |
| `streamlit run dashboard.py` | Lancer le dashboard |

---

# Dépannage

## Mauvais noyau Jupyter

Sélectionnez :

```text
Python 3.12.3 ('venv': venv)
```

ou

```text
venv (3.12.3) ./venv/bin/python
```

---

## ipykernel non installé

```bash
pip install ipykernel

python -m ipykernel install \
--user \
--name=venv \
--display-name="Python (venv)"
```

---

## "No such file or directory"

```bash
pwd
ls
cd notebook
```

---

## Token Jupyter introuvable

```bash
jupyter server list
```

---

## Version Python incorrecte

```bash
python --version
```

Doit afficher :

```text
Python 3.12.3
```

---

# Auteur

**Miarintsoa Christian**  
**STD24078**

Projet IA1 - Databridge

---

# Licence

Ce projet est réalisé dans le cadre pédagogique du programme **IA1 - Databridge**.
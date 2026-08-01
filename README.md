# Dashboard Qualité de l'Air - IA1

## Description

Dashboard interactif permettant l'analyse et la visualisation de la qualité de l'air (AQI) dans plusieurs grandes villes du monde, avec un focus sur Madagascar.

Ce projet a été réalisé dans le cadre du programme IA1 - Databridge.

L'objectif est de nettoyer, analyser et visualiser des données de pollution atmosphérique afin d'identifier les tendances, les périodes de forte pollution et de comparer la qualité de l'air entre différentes villes.

---

## Structure du projet

```text
dashbord/
│
├── notebook/
│   └── analysis.ipynb
│
├── .env.example
├── .gitattributes
├── .gitignore
├── clean_data.csv
├── config.json
├── dashboard.py
├── README.md
└── requirements.txt
```

---

## Prérequis

Avant de commencer, il faut avoir installé :

- Python 3.12.3
- pip
- Git

Pour vérifier les versions :

```bash
python --version
pip --version
git --version
```

---

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/miarintsoaainafinaritra/donne-iatech.git
```

Accéder au dossier du projet :

```bash
cd dashbord
```

---

### 2. Créer un environnement virtuel

Sous Linux ou WSL :

```bash
python3.12 -m venv venv
source venv/bin/activate
```

Sous Windows :

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Installer les dépendances

Installation directe :

```bash
pip install pandas matplotlib seaborn jupyter ipykernel streamlit
```

Ou depuis le fichier requirements.txt :

```bash
pip install -r requirements.txt
```

---

## Utilisation

### Analyse avec le notebook

Lancer Jupyter Notebook :

```bash
jupyter notebook
```

Puis ouvrir :

```text
notebook/analysis.ipynb
```

Le notebook permet de :

- Charger les données
- Nettoyer les informations
- Explorer les statistiques
- Visualiser les tendances de pollution

---

### Lancer le dashboard

Démarrer l'application Streamlit :

```bash
streamlit run dashboard.py
```

Le dashboard sera accessible depuis le navigateur à l'adresse :

```text
http://localhost:8501
```

---
## Deployer du dashboard

https://donne-iatech-2.onrender.com c'est  en ligne besoin de connexion

## Données utilisées

Le fichier principal utilisé est :

```text
clean_data.csv
```

Informations générales :

| Élément | Valeur |
|---------|--------|
| Villes | Antananarivo, Beijing, Nairobi, New Delhi, Paris |
| Nombre de points | 42 539 |
| Période | 2025-07-31 à 2026-07-30 |
| Indicateur principal | AQI (Air Quality Index) |

---

## Fonctionnalités du dashboard

Le dashboard permet de :

- Visualiser l'évolution de l'AQI
- Comparer la qualité de l'air entre plusieurs villes
- Identifier les heures avec une forte pollution
- Afficher des statistiques générales
- Explorer les données nettoyées

---

## Résultats principaux

| Métrique | Résultat |
|----------|----------|
| Ville la plus polluée | Beijing (AQI moyen : 4.3) |
| Ville la moins polluée | Antananarivo (AQI moyen : 1.1) |
| Meilleure période | 8h |
| Période la plus polluée | 15h |

---

## Technologies utilisées

| Technologie | Utilisation |
|-------------|-------------|
| Python | Traitement et analyse des données |
| Pandas | Nettoyage et manipulation des données |
| Matplotlib | Création des graphiques |
| Seaborn | Visualisation statistique |
| Jupyter Notebook | Analyse exploratoire |
| Streamlit | Création du dashboard interactif |

---

## Installation rapide

Toutes les dépendances peuvent être installées avec :

```bash
pip install -r requirements.txt
```

---

## Auteur

Nom : Miarintsoa Christian  
Matricule : STD24078  

Projet réalisé dans le cadre du programme IA1 - Databridge.
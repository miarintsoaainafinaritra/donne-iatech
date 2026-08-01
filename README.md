# Dashboard Qualité de l'Air - IA1

## Description
Dashboard interactif pour l'analyse de la qualité de l'air (AQI) à Madagascar.  
Projet réalisé dans le cadre du programme IA1 - Databridge.

---

## Structure du projet

~/dashbord/
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

---

## Installation

### 1. Activer l'environnement virtuel

```bash
source venv/bin/activate
```

### 2. Installer les dépendances

```bash
pip install pandas matplotlib seaborn jupyter ipykernel
```

---

## Utilisation

### Lancer le dashboard

```bash
python3 dashboard.py
```

### Lancer le notebook

```bash
jupyter notebook notebook/analysis.ipynb
```

---

## Données

| Élément | Valeur |
|---------|--------|
| Villes | Antananarivo, Beijing, Nairobi, New Delhi, Paris |
| Points | 42 539 |
| Période | 2025-07-31 à 2026-07-30 |

---

## Insights

| Métrique | Résultat |
|----------|----------|
| Plus polluée | Beijing (AQI : 4.3) |
| Moins polluée | Antananarivo (AQI : 1.1) |
| Meilleure heure | 8 h |
| Pire heure | 15 h |

---

## Graphiques

- Évolution de l'AQI par ville (séries temporelles)
- Distribution de l'AQI (boxplot par ville)
- Corrélation des polluants (heatmap)
- AQI moyen par heure (diagramme en barres)

---

## Auteur

**Miarintsoa Christian STD24078 **  
Projet IA1 - Databridge


# 🃏 Poker Python - Texas Hold'em

Bienvenue dans ce projet de jeu de Poker Texas Hold'em développé en Python. Ce projet utilise une approche **Orientée Objet (POO)** et une architecture modulaire pour offrir une expérience de jeu fluide et réaliste directement dans votre console.

## 🚀 Lancer le projet

Pour démarrer une partie, assurez-vous d'avoir Python installé sur votre machine, puis exécutez la commande suivante à la racine du projet :

```bash
python main.py
```

## ✨ Fonctionnalités

*   **Architecture Modulaire** : Code organisé en classes (`Card`, `Deck`, `Player`, `PokerGame`, `HandEvaluator`).
*   **Jusqu'à 10 joueurs** : Support de 2 à 10 joueurs autour de la table.
*   **Cycle Complet de Jeu** : Gestion automatique des phases Pre-flop, Flop, Turn et River.
*   **Système de Mises Avancé** : Gestion des Small/Big Blindes, des relances (Raise), des suivis (Call) et des tapis (All-in).
*   **Arbitrage Automatique** : Évaluation précise des mains (Paires, Suites, Couleurs, etc.) et détermination automatique du/des gagnant(s) avec gestion des Kickers.
*   **Gestion du Split Pot** : Partage automatique du pot en cas d'égalité parfaite.
*   **Confidentialité (Pass-and-Play)** : Nettoyage de l'écran entre les tours pour cacher les mains des autres joueurs.

## 📁 Structure du Projet

```text
.
├── main.py              # Point d'entrée du jeu (Interface console)
├── PLAN_PROJET.md       # Suivi du projet et roadmap
├── README.md            # Documentation (ce fichier)
└── poker/               # Package contenant la logique métier
    ├── card.py          # Modèle pour les cartes individuelles
    ├── deck.py          # Gestion du paquet de 52 cartes
    ├── player.py        # Gestion des profils joueurs et jetons
    ├── game.py          # Orchestration des règles et des tours
    └── hand_evaluator.py# Algorithme de comparaison des mains
```

## 🛠️ Installation

1.  Clonez ce dépôt :
    ```bash
    git clone https://github.com/ari3645/Poker.git
    cd Poker
    ```
2.  (Optionnel) Créez un environnement virtuel :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Linux/macOS
    venv\Scripts\activate     # Sur Windows
    ```

## 📜 Règles Appliquées
Ce projet respecte les règles officielles du **Texas Hold'em No Limit**. Chaque joueur commence avec un tapis de **2000 jetons**. Les blindes sont fixées à **10 (Small)** et **20 (Big)**.

---
Développé avec ❤️ dans le cadre du projet Python.

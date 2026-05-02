# Plan de Projet - Poker Python

Ce document récapitule l'avancement du projet, l'architecture choisie et les règles établies pour la refonte du jeu de Poker.

## 📌 Architecture du Projet

Nous avons opté pour une approche **modulaire et orientée objet (POO)** pour éviter d'avoir tout le code dans un seul fichier.

```text
/
├── main.py              # Point d'entrée, interface utilisateur et menu
├── PLAN_PROJET.md       # Suivi du projet et règles (ce fichier)
└── poker/               # Package contenant la logique du jeu
    ├── __init__.py      # Rend le dossier importable
    ├── card.py          # Classe Card (Valeur, Couleur)
    ├── deck.py          # Classe Deck (Gestion du paquet de 52 cartes)
    ├── player.py        # Classe Player (Jetons, main, état)
    └── game.py          # Classe PokerGame (Orchestration du jeu)
```

## ✅ Ce qui a été fait

1.  **Modèle de données :**
    *   `Card` : Gestion des enseignes (♠, ♥, ♣, ♦) et des rangs (2 à As).
    *   `Deck` : Mélange automatique et distribution de cartes.
    *   `Player` : Gestion du nom, des jetons (par défaut 2000), de la main et des états (couché, tapis).
2.  **Initialisation du Jeu et Phases :**
    *   Création d'une interface de bienvenue.
    *   Choix du nombre de joueurs (entre 2 et 10).
    *   Distribution automatique du Pre-flop (2 cartes par joueur).
    *   Déroulement séquentiel des phases : Flop, Turn et River.
    *   **Système de tour par tour complet :** La boucle de mise continue jusqu'à ce que tous les joueurs aient égalisé ou se soient couchés.
    *   **Gestion du Pot et Blindes :** Les jetons sont déduits, le pot est suivi, et les Small/Big Blindes (10/20) sont automatiques.
    *   **Mises Intuitives :** Les relances se font sur le montant TOTAL visé pour le tour.
    *   **Gestion du All-in :** Un joueur peut faire tapis s'il n'a plus assez de jetons pour suivre ou s'il veut tout miser.
    *   **Confidentialité (Pass-and-Play) :** Nettoyage de l'écran entre chaque joueur et bouton "Prêt" pour cacher les mains.
    *   **Arbitrage Automatique :** L'algorithme détecte les combinaisons et compare les mains selon les règles officielles (kickers inclus).
    *   **Gestion du Split Pot :** Partage automatique du pot en cas d'égalité parfaite.

## 📜 Règles et Principes

*   **Modularité :** Chaque composant (Carte, Joueur, Jeu, Évaluateur) est indépendant.
*   **Validation :** Vérification stricte des mises et des règles de relance.
*   **Simplicité :** Affichage console clair et interactif.
*   **Réalisme :** On respecte la règle de "brûler" une carte et l'ordre des joueurs.

## 🚀 Prochaines Étapes (Roadmap)

1.  **Étape 6 : Comparaison automatique des mains**
    *   Algorithme pour détecter les combinaisons (Paire, Suite, Couleur, etc.).
    *   Détermination automatique du vainqueur sans intervention humaine.

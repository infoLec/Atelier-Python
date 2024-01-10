# Atelier-Python
Convertisseur de devises

## Introduction
Ce projet est un simple convertisseur de devises utilisant une API pour obtenir les taux de change en temps réel. Les utilisateurs peuvent saisir le montant à convertir, ainsi que la devise source et la devise cible. Le convertisseur utilise l'API open.er-api.com pour obtenir les taux de change actuels.

## Documentation du Projet

### Structure du Projet
Le projet est organisé en une classe principale, `ConvertisseurDeDevises`, qui gère les opérations de conversion et d'interaction avec l'API des taux de change. Le script principal utilise cette classe pour effectuer les conversions et afficher les résultats.

### Techniques
- **Langage de Programmation:** Le script est écrit en Python.
- **Bibliothèque Utilisée:** Le module `requests` est utilisé pour effectuer des requêtes HTTP à l'API des taux de change.

### Défis Rencontrés
L'un des défis rencontrés était de gérer les erreurs potentielles lors de l'appel à l'API. Des vérifications ont été mises en place pour s'assurer que la requête réussisse avant de procéder à la conversion.

## Présentation du Projet

### Aperçu

Notre projet consiste en un convertisseur de devises simple, permettant à l'utilisateur de saisir un montant, une devise source et une devise cible pour obtenir le montant équivalent dans la devise cible. Le tout est basé sur les taux de change en temps réel fournis par l'API open.er-api.com.

### Fonctionnement

1. Nous entrons le montant à convertir, la devise source et la devise cible.
2. Le script utilise la classe `ConvertisseurDeDevises` pour obtenir le taux de change en temps réel.
3. La conversion est effectuée, et le résultat est affiché.

### Exemple d'Exécution
Entrez le montant à convertir : 100
Entrez la devise source : USD
Entrez la devise cible : EUR
100.0 USD équivaut à 82.45 EUR

### Points Clés de la Documentation

- **Structure du Projet :** La classe principale, les fichiers, et l'utilisation de l'API.
- **Choix Techniques :** Python pour la simplicité, utilisation de la bibliothèque `requests` pour les requêtes HTTP.
- **Bibliothèques Utilisées :** `requests` pour les requêtes HTTP.
- **Défis et Solutions :** Gestion des erreurs lors des appels à l'API.

## Rapport de Réflexion

### Objectifs d'Apprentissage

Nos objectifs initiaux étaient centrés sur la compréhension des appels API, la manipulation des données en Python, et la mise en œuvre d'une solution fonctionnelle. Au fil du projet, nous avons acquis une meilleure compréhension de ces concepts.

### Compétences Acquises

Les compétences développées comprennent la gestion des erreurs dans les requêtes API, la manipulation de données JSON, et la mise en œuvre de classes en Python pour la modularité.

### Applications Professionnelles

Ces compétences peuvent être directement appliquées dans des contextes professionnels impliquant l'intégration d'API, la manipulation de données financières, et le développement d'outils automatisés pour la conversion de devises.

---


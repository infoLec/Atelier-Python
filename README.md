# Atelier-Python
Convertisseur de devises

## Introduction
Ce projet est un simple convertisseur de devises utilisant une API pour obtenir les taux de change en temps réel. Les utilisateurs peuvent saisir le montant à convertir, ainsi que la devise source et la devise cible. Le convertisseur utilise l'API open.er-api.com pour obtenir les taux de change actuels.

## Documentation du Projet

### Structure du Projet
Le projet est organisé en une classe principale, `ConvertisseurDeDevises`, qui gère les opérations de conversion et d'interaction avec l'API des taux de change. Le script principal utilise cette classe pour effectuer les conversions et afficher les résultats.

### Choix Techniques
- **Langage de Programmation:** Le script est écrit en Python.
- **Bibliothèque Utilisée:** Le module `requests` est utilisé pour effectuer des requêtes HTTP à l'API des taux de change.

### Défis Rencontrés
L'un des défis rencontrés était de gérer les erreurs potentielles lors de l'appel à l'API. Des vérifications ont été mises en place pour s'assurer que la requête réussisse avant de procéder à la conversion.

## Présentation

### Utilisation
1. Clonez le repository : `git clone https://github.com/infoLec/Atelier-Python`
2. Exécutez le script principal : `ConvertisseurDeDevises`

### Exemple d'Exécution
Entrez le montant à convertir : 100
Entrez la devise source : USD
Entrez la devise cible : EUR
100.0 USD équivaut à 82.45 EUR

## Auteurs
- Jalal Eddine BOUCHRIT
- 

import requests

class ConvertisseurDeDevises:
    def __init__(self):
        # URL de l'API pour les taux de change en temps réel
        self.url_api = "https://open.er-api.com/v6/latest"

    def obtenir_taux_de_change(self, devise_de, devise_vers):
        # Paramètres pour l'API des taux de change
        params = {
            "base": devise_de,
            "symbols": devise_vers
        }

        # Requête à l'API
        response = requests.get(self.url_api, params=params)

        # Vérifier si la requête a réussi
        if response.status_code == 200:
            taux_de_change = response.json()["rates"][devise_vers]
            return taux_de_change
        else:
            print("Erreur lors de la récupération des taux de change.")
            return None

    def convertir(self, montant, devise_de, devise_vers):
        taux_de_change = self.obtenir_taux_de_change(devise_de, devise_vers)

        if taux_de_change is not None:
            montant_converti = montant * taux_de_change
            return montant_converti
        else:
            return None

# Affichage
convertisseur = ConvertisseurDeDevises()

montant_a_convertir = float(input("Entrez le montant à convertir : "))
devise_source = input("Entrez la devise source  : ")
devise_cible = input("Entrez la devise cible  : ")

resultat = convertisseur.convertir(montant_a_convertir, devise_source, devise_cible)

if resultat is not None:
    print(f"{montant_a_convertir} {devise_source} équivaut à {resultat:.2f} {devise_cible}")
else:
    print("La conversion a échoué.")

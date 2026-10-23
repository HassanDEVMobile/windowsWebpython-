
class ScrapingView :

    def menu(self):
        visuel = """
        1-Demarrer le scraping 
        2-Afficher les données scraper
        3-Afficher les statistiques 
        4-Exporter les statistiques
        0-Quitter 
        """
        print(visuel)
        return int(input("Veuillez faire un choix : "))

    def Afficher_donner_scraper(self ,chargement_donner):
        for donner in chargement_donner :
            print(donner)

    def Afficher_statistique(self ,statistiques):
        print(statistiques)
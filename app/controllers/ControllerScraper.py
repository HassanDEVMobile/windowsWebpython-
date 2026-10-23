
from app.models.Depots import Depots
from app.models.Produit import Produit
from app.views.ScrapingView import ScrapingView
from app.scraper.AmazonScraper import AmazonScraper
from app.scraper.Parsing import Parsing


class ControllerScraper:
    scrapingview = ScrapingView()
    depots = Depots()
    amazonscraper = AmazonScraper()

    def option1(self, url, chemin):
            self.depots.sauvegarde_scraping(chemin, self.amazonscraper.scraper(url))

    def option2(self ,chemin):
        ScrapingView.Afficher_donner_scraper(Depots.chargement_scraping_donner(chemin))

    def Option3(self,chemin ,categorie ,sous_categorie):
        self.scrapingview.Afficher_statistique(self.depots.statistiques(chemin,categorie ,sous_categorie))

    def demarrer(self ,chemin ,url ,categorie ,sous_categorie):

        while True:
            if self.scrapingview.menu() == 1:
                self.option1(url ,chemin)
            elif self.scrapingview.menu() == 2 :
                self.option2(chemin)
            elif self.scrapingview.menu() == 3:
                self.Option3(chemin,categorie ,sous_categorie)
            else :
                break
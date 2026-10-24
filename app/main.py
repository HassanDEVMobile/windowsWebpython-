



import config
from controllers.ControllerScraper import ControllerScraper

if __name__ == '__main__':
    application = ControllerScraper()
    application.demarrer(config.CHEMIN, config.URL, config.CATEGORIE, config.SOUS_CATEGORIE)




import config
from controllers.ControllerScraper import ControllerScraper

application = ControllerScraper()
application.demarrer(config.CHEMIN, config.URL, config.CATEGORIE, config.SOUS_CATEGORIE)
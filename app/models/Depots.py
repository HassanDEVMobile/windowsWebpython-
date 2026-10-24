
import os
import csv
# from models.Produit import Produit

class Depots:

    def sauvegarde_scraping(self,chemin ,liste_produit ,champ=["Nom" ,"Prix" ,"Note" ,"Image URL"]):
        # print(os.path.abspath(chemin))
        if not(os.path.exists(chemin)) : return "Chemin inexistant !"
        with open(chemin ,"w" ,newline="" ,encoding="utf-8") as f :
            save = csv.DictWriter(f, fieldnames=champ)
            save.writeheader()
            save.writerows(liste_produit)

    def chargement_scraping_donner(self ,chemin):
        if not os.path.exists(chemin) : return "Vous ne pouvez pas charger les données d'un chemin inexistant !"
        with open(chemin ,"r" ,newline="" ,encoding="utf-8") as f :
            chargement_donner = [ligne for ligne in f ]
            return   chargement_donner


    def statistiques(self,chemin ,categorie ,sous_categorie):
        moins_chers = 1
        plus_chers = 0
        nombre_note = 0
        with open( chemin ,"r" ,newline="" ,encoding="utf-8") as f :
            dictionnaire = csv.DictReader(f)
            for e in dictionnaire :
                if e["Prix"] > plus_chers :
                    plus_chers = e["prix"]
                    nom = e["Nom"]
                if e["Prix"] < moins_chers :
                    plus_chers = e["prix"]
                    nom = e["Nom"]
                if e["Note"] >= 4 : nombre_note += 1

            return f"""
                ====================================
                        STATISTIQUES SCRAPING
                ====================================
                Catégorie : {categorie} #basename retourne le dernier élément d'un chemin
                Sous-catégorie : {sous_categorie}
                Nombre de produit au total = {len(self.chargement_scraping_donner())}
                Prix moyen = {sum(f["Prix"] ) /len(f)}
                moins chers = {min(f["Prix"])} €
                plus chers = {max(f["Prix"])} €
                Produit le moins chers : {nom} ({moins_chers}) €
                Produit le plus chers : {nom} ({plus_chers}) €
                Note Moyenne : 
                nombre de produit avec une note ≥ 4 = {nombre_note}
                """.strip()


    # {sum(f["Note"])/len(f)}/5
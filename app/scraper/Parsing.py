
class Parsing :

    def nettoyer(self ,prix):
        valeur_netoyer = (float)(prix.replace("€" ,"").replace(" " ,"").replace("," ,".").strip())
        return valeur_netoyer
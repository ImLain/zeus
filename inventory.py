import sys
import os
import json

dossier_courant = os.path.dirname(__file__)

class Liste(list):
    def __init__(self, nom):
        self.nom = nom

    def ajouter(self, element):
        element = element.capitalize()
        if element in self:
            print(f"""
                Attention : '{element}' est déjà dans votre inventaire ! 
                """)
            return False

        self.append(element)
        print(f"""
            '{element}' est à présent dans votre inventaire.
            """)
        return True

    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        return False

    def afficher(self):
        print(f"""
            Votre {self.nom} contient : 
            """)
        for element in self:
            print(f" - {element}")

    def sauvegarder(self):
        chemin = os.path.join(dossier_courant, f"{self.nom}.json")
        if not os.path.exists(dossier_courant):
            os.makedirs(dossier_courant)

        with open(chemin, "w") as f:
            json.dump(self,f,ensure_ascii=False, indent=4)

        print("""
            Vous venez de sauvegarder la partie.
              """)


class Objets(Liste):
    def __init__(self, nom):
        self.nom = nom
    def ajouter(self, element):
        element = element.capitalize()
        
        if element in self:
            return False
        
        self.append(element)
        return True

    def sauvegarder(self):
        chemin = os.path.join(dossier_courant, f"{self.nom}.json")
        if not os.path.exists(dossier_courant):
            os.makedirs(dossier_courant)

        with open(chemin, "w") as f:
            json.dump(self,f,ensure_ascii=False, indent=4)
     
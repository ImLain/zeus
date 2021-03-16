import rooms
import inventory
import os
import sys
import time
#from platform import system as system_name  # Returns the system/OS name
#from subprocess import call as system_call  # Execute a shell command



# liste inventaire :
liste_inventaire = ["afficher inventaire", "afficher l'inventaire", "ouvrir inventaire", "ouvrir l'inventaire", "voir inventaire", "voir l'inventaire", "montrer inventaire", "montrer l'inventaire"]

# dictionnaire verbe d'observation :
dict_unaction = {
    0: ("examiner", "observer", "regarder"),
    1: ("parler", "discuter", "dire"),
    2: ("examiner", "observer", "regarder","fouiller", "prendre", "chercher")
}

# dictionnaire verbe d'action :
dict_action = {
    0: ("ouvrir"),
    1: ("tirer", "enlever", "défaire", "remettre"),
    2: ("offrir", "poser", "donner", "mettre"),
    3: ("insérer", "mettre", "utiliser"),
    4: ("déplier", "enlever", "ouvrir"),
    5: ("lire", "ouvrir"),
    6: ("utiliser", "allumer", "éteindre"),
    7: ("rentrer", "appuyer", "déverrouiller", "ouvrir")
}

# liste pour les armoires/fenêtres
liste_armoire = ("armoire", "pierre", "rangement", "pierres", "rouge", "plastique",
        "multicolore", "meuble", "métal", "mystérieux")

liste_fenetre = ("fenêtre", "fenetre", "ouverture", "trou", "mur", "coulissante",
                "grille", "aération")

# dictionnaire objets 
dict_objet = {
    0: ("couronne", "égyptienne"),
    1: ("pierre", "précieuse"), 
    2: ("bandelette", "morceau", "dépasse"),
    3: ("pierre", "précieuse")
}

# dictionnaire animal
dict_animal = {
    "nom": ("chat", "dinosaure", "panda", "roux", "robot", "robot-chat"),
    "good_action": ("caresser", "gratter"),
    "action": ("poser", "donner"),
    "bad_action": ("taper", "frapper", "heurter", "bousculer", "pousser")
}

# liste femme/geisha...
liste_femme = ("momie", "femme", "momifiée", "geisha","primate", "singe", "robot")

# dictionnaire jarres
dict_jarre = {
    0: ("scorpion", "scorpions"), 
    1: ("ver", "vers"),
    2: ("scarabées", "scarabée"),
    3: ("jarres", "jarre")
}

# liste parchemin 
liste_parchemin = ("parchemin", "parchemins", "ruban", "soie")

# liste pierre 
liste_pierre = ("pierre", "pierres", "taillée", "taillées", "éclat", "brillant")

# liste relief Japon
liste_relief = ("appuyer", "activer", "actionner")

# dictionnaire livre
dict_livre = {
    0: ("livre", "livres"),
    1: ("intérieur"),
    2: ("tête", "têtes", "tete", "tetes"),
    3: ("facile", "hiéroglyphes", "hieroglyphes", "hieroglyphe")
}

livres = ["Découvrez votre vous intérieur", 
        "Comment élever un singe à trois têtes", 
        "Lecture facile des hiéroglyphes"]

#liste stylo doré
liste_stylo = ("stylo", "doré", "mine", "rouge")

# liste code meuble
liste_code = ("code", "clavier", "tactile", "meuble", "métal", "armoire")

liste_levier = ("clé", "clef")


# typing slowly
def slowprint(self):
    for c in self + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./17) 


def main():
    currentScore = 3
    present_play(currentScore)

# score
def scoreUpdater(currentScore):
    currentScore = currentScore - 1
    if currentScore == 0:
        print("Vous avez perdu ...")
        play_again(currentScore)
    else:
        print(f"Vous avez perdu une vie... Il vous en reste {currentScore}")
        return currentScore

def play_again(currentScore):
    if not os.path.exists("inventaire.json"): 
        inventaire.clear()
    answer = input("Rejouer ? Oui ou Non \n").lower()
    if answer == "oui":
        print("Et c'est reparti !")
        present_play(currentScore)
    elif answer == "non":
        print("Au revoir.")


inventaire = inventory.Liste("Inventaire")
objet = inventory.Objets("Objets")
levier = rooms.Levier()


def present_play(currentScore):
    present_room = rooms.PresentRoom()
    #slowprint(present_room.beginning())
    print(present_room.beginning())

    while True:
        user = input("Que souhaitez-vous faire : ").lower().strip()
        
        # regarder par la fenêtre
        if user.startswith(dict_unaction[0]) and user.endswith(liste_fenetre):
            print("""
                        Il fait beau et chaud à l'extérieur.
                        Vous apercez des immeubles au coin.
                """)

        # examiner la machine
        elif user.startswith(dict_unaction[0]) and user.endswith("machine") :
            present_room.machine()

        # examiner/prendre DVD
        elif user.startswith(dict_unaction[0]) and user.endswith("dvd"):
            present_room.dvd()
        elif user.startswith("prendre") and user.endswith("dvd") or user.endswith("futur"):
            inventaire.ajouter("DVD")
        
        # examiner/caresser chat
        elif user.startswith(dict_unaction[0]) and user.endswith(dict_animal["nom"]):
            print("""
                        Le chat semble tendre la tête pour recevoir
                        des caresses.
                """)
        elif user.startswith(dict_animal["good_action"]) and user.endswith(dict_animal["nom"]): #caresser
            present_room.chat()

        # parler à la femme
        elif user.startswith(dict_unaction[1]) and user.endswith(liste_femme):
            present_room.femme()

        # examiner/ouvrir armoire
        elif user.startswith(dict_unaction[0]) and user.endswith(liste_armoire):
            if "Armoire" in objet : 
                print("""
                        L'armoire est grande ouverte.
                  """)
            elif "Armoire" not in objet: 
                present_room.armoire()
                print(present_room.examiner_armoire)
        elif user.startswith(dict_action[0]) and user.endswith(liste_armoire):
            if "Armoire" in objet : 
                print("""
                        L'armoire est grande ouverte.
                  """)
            elif "Armoire" not in objet :
                user_code = (input("Quel est le code à trois chiffres : "))
                if user_code == "673":
                    present_room.armoire()
                    print(present_room.ouvrir_armoire)
                    objet.ajouter("armoire")
                    objet.sauvegarder()
                else: 
                    print("Ce code n'est pas valide.")

        # examiner/prendre levier pyramide
        elif user.startswith(dict_unaction[0]) and user.endswith("pyramide"):
            print("""
                        C'est un levier dont la tête est en forme de pyramide.
                """)
        elif user.startswith("prendre") and user.endswith("pyramide"):
            if "Armoire" in objet :       
                inventaire.ajouter("levier à tête de pyramide")  
            elif "Armoire" not in objet: 
                print("""
                        Vous inspectez rapidement les lieux mais vous 
                        ne voyez pas de levier... pour l'instant.
                    """)
        
        # changer de scène Egypte
        elif user.startswith(dict_action[3]) and user.endswith("pyramide"):
            if "Levier à tête de pyramide" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier à tête de pyramide" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    egypt_play(currentScore)
                else: 
                    print("...Mais où insérer ce levier ? ")

        
        #afficher inventaire 
        elif user in liste_inventaire:
            inventaire.afficher()
        
        else: 
            print("""
                     Commande invalide !
                     """)


def egypt_play(currentScore):
    egypt_room = rooms.EgyptRoom()
    print(egypt_room.beginning())
    #slowprint(egypt_room.beginning())

    while True:
        user = input("Que souhaitez-vous faire : ").lower().strip()

        # regarder par la fenêtre
        if user.startswith(dict_unaction[0]) and user.endswith(liste_fenetre):
            print("""
                        Il fait beau et chaud à l'extérieur.
                        Vous apercez des pyramides au coin.
                """)
        # examiner la machine
        elif user.startswith(dict_unaction[0]) and user.endswith("machine"):
            egypt_room.machine()

        # examiner les tablettes
        elif user.startswith(dict_unaction[0]) and user.endswith("tablette") or user.endswith("tablettes"):
            if "Hiéroglyphes" not in objet:
                egypt_room.tablettes()
                print(egypt_room.examiner1)
            elif "Hiéroglyphes" in objet:
                egypt_room.tablettes()
                print(egypt_room.examiner2)
        elif user in ["prendre tablette", "prendre tablettes", "prendre les tablettes"]:
            egypt_room.tablettes()
            print(egypt_room.prendre)

        # examiner / caresser / couronne chat 
        elif user.startswith(dict_unaction[0]) and user.endswith(dict_animal["nom"]):
            egypt_room.chat()
            print(egypt_room.examiner)
        elif user.startswith(dict_animal["good_action"]) and user.endswith(dict_animal["nom"]):
            egypt_room.chat()
            print(egypt_room.caresser)
        elif user.startswith(dict_animal["action"]) and user.endswith(dict_objet[0]):
            if "Petite couronne égyptienne" in inventaire:
                user_answer = input("Où est-ce qu'on pose la couronne ? ")
                if user_answer == "chat":
                    egypt_room.chat()
                    print(egypt_room.couronne)
                    inventaire.ajouter("Levier à tête d'os") #préhistoire
                    inventaire.enlever("Petite couronne égyptienne")
                else: 
                    print("""
                        Commande invalide ! 
                            """)
            else: 
                print("""
                        Encore faudrait-il avoir une couronne...
                        """)

        elif user.startswith(dict_animal["action"]) and user.endswith("chat"):
            if "Petite couronne égyptienne" in objet:
                egypt_room.chat()
                print(egypt_room.couronne)
            else: 
                print("""
                        Encore faudrait-il avoir une couronne...
                        """)

        # examiner momie / bandelette
        elif user.startswith(dict_unaction[0]) and user.endswith(liste_femme):
            egypt_room.momie()
            print(egypt_room.examiner)
        elif user.startswith(dict_action[1]) and user.endswith(dict_objet[2]):
            egypt_room.momie()
            print(egypt_room.tirer)
            inventaire.ajouter("petit miroir")

        # armoire
        elif user.startswith(dict_unaction[0]) and user.endswith(liste_armoire):
            print("""
                        Quelle belle armoire en pierre !
                    """)
        elif user.startswith(dict_action[0]) and user.endswith(liste_armoire):
            if "Armoire de pierre" not in objet : 
                egypt_room.armoire()
                objet.ajouter("Armoire de pierre")
            else: 
                print("""
                        Vous avez déjà ouvert l'armoire.
                        """)

        # les jarres
        elif user.startswith(dict_unaction[2]) and user.endswith(dict_jarre[3]):
            if "Armoire de pierre" in objet : 
                user_jarre = input("Quelle jarre (scorpions/vers/scarabées) ? ")
                if user_jarre.endswith(dict_jarre[0]):
                    egypt_room.jarres()
                    print(egypt_room.scorpion)
                    currentScore = scoreUpdater(currentScore)
                elif user_jarre.endswith(dict_jarre[1]):
                    egypt_room.jarres()
                    print(egypt_room.ver)
                elif user_jarre.endswith(dict_jarre[2]):
                    if "Levier à tête d'étoile" not in inventaire: 
                        egypt_room.jarres()
                        print(egypt_room.scarabée)
                        inventaire.ajouter("levier à tête d'étoile") # japon
                    else :
                        print("""
                        Vous avez déjà fouillé cette jarre
                        """)

            else: 
                print("""
                        Vous ne voyez pas de jarre ...""")

        elif user.startswith(dict_unaction[2]) and user.endswith(dict_jarre[0]) and "Armoire de pierre" in objet :
            egypt_room.jarres()
            print(egypt_room.scorpion)
            currentScore = scoreUpdater(currentScore)
        elif user.startswith(dict_unaction[2]) and user.endswith(dict_jarre[1]) and "Armoire de pierre" in objet :
            egypt_room.jarres()
            print(egypt_room.ver)
        elif user.startswith(dict_unaction[2]) and user.endswith(dict_jarre[2]) and "Armoire de pierre" in objet :
            egypt_room.jarres()
            print(egypt_room.scarabée)
            inventaire.ajouter("levier à tête d'étoile")

        # changer de scène pour Japon
        elif user.startswith(dict_action[3]) and user.endswith("étoile"):
            if "Levier à tête d'étoile" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier à tête d'étoile" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    japan_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")


        # changer de scène pour Préhistoire
        elif user.startswith(dict_action[3]) and user.endswith("os"):
            if "Levier à tête d'os" not in inventaire: 
                print("""
                        Encore faudrait-il avoir le levier adéquate...
                    """)
            elif "Levier à tête d'os" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    prehist_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")

        # changer de scène pour USA
        elif user.startswith(dict_action[3]) and user.endswith("fleur"):
            if "Levier à tête de fleur" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier à tête de fleur" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    usa_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")
            else: 
                print("Il faudrait un levier d'abord...")

        #afficher inventaire 
        elif user in liste_inventaire:
            inventaire.afficher()   
        
        else: 
            print("""
                        Commande invalide !
                    """)
        
 


def japan_play(currentScore):
    japan_room = rooms.JapanRoom()
    print(japan_room.beginning())
    #slowprint(japan_room.beginning())

    while True:
        user = input("Que souhaitez-vous faire : ").lower().strip()

        # regarder par la fenêtre
        if user.startswith(dict_unaction[0]) and user.endswith(liste_fenetre):
            print("""
                        Il fait beau et chaud à l'extérieur.
                        Vous apercez des temples japonais au coin.
                """)

        # examiner machine
        elif user.startswith(dict_unaction[0]) and user.endswith("machine"):
            japan_room.machine()

        # examiner parchemins
        elif user.startswith(dict_unaction[0]) and user.endswith(liste_parchemin):
            if "Parchemin" not in objet: 
                japan_room.parchemins()
                print(japan_room.examiner)
            elif "Parchemin" in objet:
                print("""
                        Ce sont de très jolis parchemins en papier de 
                        riz.
                        """)
        elif user.startswith(dict_action[4]) and user.endswith(liste_parchemin):
            if "Parchemin" not in objet:
                japan_room.parchemins()
                print(japan_room.deplier)
                objet.ajouter("Parchemin")
            else: 
                print("""
                        Le parchemin a déjà été ouvert.
                        Vous avez découvert que cette époque vous un culte 
                        important à la Lune.
                        """)

        # examiner panda
        elif user.startswith(dict_unaction[0]) and user.endswith(dict_animal["nom"]):
            japan_room.panda()
            print(japan_room.examiner)
        elif user.startswith(dict_animal["bad_action"]) and user.endswith(dict_animal["nom"]):
            japan_room.panda()
            print(japan_room.taper)
            currentScore = scoreUpdater(currentScore)

        # examiner geisha / bol
        elif user.startswith(dict_unaction[0]) or  user.startswith(dict_unaction[1]) and user.endswith(liste_femme):
            japan_room.geisha()
            print(japan_room.examiner)
        elif user.startswith(dict_action[2]) and user.endswith(dict_objet[3]):
            if "Pierre précieuse" in inventaire:
                user_answer = input("Où souhaitez-vous poser la pierre précieuse ? (1 seul mot) ")
                if user_answer.endswith("bol"):
                    japan_room.geisha()
                    print(japan_room.pierre)
                    inventaire.ajouter("levier à tête de fleur") 
                    inventaire.enlever("Pierre précieuse")
                    objet.ajouter("bol")
                else: 
                    print("""
                        Cherchez encore. Cette pierre précieuse ne peut être déposé
                        qu'à un seul endroit.
                            """)
            else: 
                print("""
                        Encore faudrait-il avoir une pierre précieuse
                        """)

        elif user.startswith(dict_action[2]) and user.endswith("bol"):
            if "Pierre précieuse" in inventaire:
                user_answer = input("Que souhaitez-vous déposer ? ")
                if user_answer.endswith(dict_objet[3]):
                    japan_room.geisha()
                    print(japan_room.pierre)
                    inventaire.ajouter("levier à tête de fleur")
                    inventaire.enlever("Pierre précieuse")
                    objet.ajouter("bol") 
                
            elif "Pierre précieuse" not in inventaire and "Bol" in objet: 
                print("""
                        L'attention de la Geisha est absorbée par cette magnifique
                        pierre précieuse.
                    """)

            else:     
                print("""
                        Il est certain que la Geisha attend quelque chose de valeur.
                        """)
                        

        # armoire
        elif user.startswith(dict_action[0]) and user.endswith(liste_armoire):
            japan_room.armoire()
            print(japan_room.examiner)

        elif user.startswith(liste_relief) and user.endswith("soleil") and "Armoire rouge" in objet:
            print("""
                        L'armoire est grande ouverte.
                    """)
        elif user.startswith(liste_relief) and user.endswith("crâne") and "Armoire rouge" in objet:
            print("""
                        L'armoire est grande ouverte.
                    """)
        elif user.startswith(liste_relief) and user.endswith("shuriken") and "Armoire rouge" in objet:
            print("""
                        L'armoire est grande ouverte.
                    """)
        elif user.startswith(liste_relief) and user.endswith("lune") and "Armoire rouge" in objet:
            if "Petite couronne égyptienne" not in objet:
                print("""
                        L'armoire est ouverte. Elle contient de nombreux
                        bibelots sans intérêt ; néanmoins une petite
                        couronne égyptienne attire votre regard.
                        """)

            else : 
                print("""
                        L'armoire est grande ouverte.
                    """)

        elif user.startswith(liste_relief) and user.endswith("soleil") and "Armoire rouge" not in objet:
                japan_room.armoire()
                print(japan_room.appuyer_soleil)
        elif user.startswith(liste_relief) and user.endswith("crâne") and "Armoire rouge" not in objet:
                japan_room.armoire()
                print(japan_room.appuyer_crane)
                currentScore = scoreUpdater(currentScore)
        elif user.startswith(liste_relief) and user.endswith("shuriken") and "Armoire rouge" not in objet:
                japan_room.armoire()
                print(japan_room.appuyer_shuriken)
        elif user.startswith(liste_relief) and user.endswith("lune") and "Armoire rouge" not in objet:
                japan_room.armoire()
                print(japan_room.appuyer_lune)   
                objet.ajouter("Armoire rouge")
        
        
        #prendre couronne égyptienne
        elif user.startswith("prendre") and user.endswith(dict_objet[0]) and "Armoire rouge" in objet : 
            inventaire.ajouter("petite couronne égyptienne")
            objet.ajouter("petite couronne égyptienne")

        # changer de scène pour USA
        elif user.startswith(dict_action[3]) and user.endswith("fleur"):
            if "Levier à tête de fleur" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier à tête de fleur" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    usa_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")
            else: 
                print("Il faudrait un levier d'abord...")

        # changer de scène Egypte
        elif user.startswith(dict_action[3]) and user.endswith("pyramide"):
            if "Levier à tête de pyramide" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier à tête de pyramide" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    egypt_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")

        # changer de scène pour Préhistoire
        elif user.startswith(dict_action[3]) and user.endswith("os"):
            if "Levier à tête d'os" not in inventaire: 
                print("""
                        Encore faudrait-il avoir le levier adéquate...
                    """)
            elif "Levier à tête d'os" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    prehist_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")
        #afficher inventaire 
        elif user in liste_inventaire:
            inventaire.afficher()  

        else: 
            print("""
                        Commande invalide !
                    """)


def prehist_play(currentScore):
    prehist_room = rooms.PrehisRoom()
    print(prehist_room.beginning())
    #slowprint(prehist_room.beginning())

    while True:
        user = input("Que souhaitez-vous faire : ").lower().strip()

        # regarder par la fenêtre
        if user.startswith(dict_unaction[0]) and user.endswith(liste_fenetre):
            print("""
                        Il fait beau et chaud à l'extérieur.
                        Vous apercevez des rochers au coin.
                """)

        # examiner machine
        elif user.startswith(dict_unaction[0]) and user.endswith("machine"):
            prehist_room.machine()

        # examiner pierres taillées
        elif user.startswith(dict_unaction[0]) and user.endswith(liste_pierre):
            if "Pierres" not in objet: 
                prehist_room.pierre()
                print(prehist_room.examiner)
            elif "Pierres" in objet:
                print("""
                        C'est un tas de cailloux, plus ou moins taillés.
                        """)
        elif user.startswith(dict_unaction[2]) and user.endswith(liste_pierre):
            if "Pierres" not in objet:
                prehist_room.pierre()
                print(prehist_room.fouiller)
                objet.ajouter("Pierres")
                inventaire.ajouter("Pierre précieuse")
            else: 
                print("""
                        Plus rien n'est dissimulé sous les cailloux. Vous avez
                        déjà récupéré la pierre précieuse. 
                        """)

        # examiner petit dinosaure
        elif user.startswith(dict_unaction[0]) and user.endswith(dict_animal["nom"]):
            prehist_room.dinosaure()
            print(prehist_room.examiner)
        elif user.startswith(dict_animal["bad_action"]) and user.endswith(dict_animal["nom"]):
            prehist_room.dinosaure()
            print(prehist_room.taper)
            currentScore = scoreUpdater(currentScore)

        # examiner primate
        elif user.startswith(dict_unaction[0]) and user.endswith(liste_femme):
            prehist_room.primate()

        # armoire
        elif user.startswith(dict_unaction[0]) and user.endswith(liste_armoire):
            prehist_room.armoire()
            print(prehist_room.examiner)
        elif user.startswith(dict_action[0]) and user.endswith(liste_armoire) :
            if "Armoire pierre" not in objet : 
                prehist_room.armoire()
                print(prehist_room.ouvrir)
                objet.ajouter("Armoire pierre")
            else :
                 print("""
                    Il n'y a rien de très intéressant
                    là-dedans. 
                 """)

        # changer de scène pour USA
        elif user.startswith(dict_action[3]) and user.endswith("fleur"):
            if "Levier à tête de fleur" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier à tête de fleur" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    usa_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")
            else: 
                print("Il faudrait un levier d'abord...")

        # changer de scène Egypte
        elif user.startswith(dict_action[3]) and user.endswith("pyramide"):
            if "Levier à tête de pyramide" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier à tête de pyramide" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    egypt_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")
        
        # changer de scène pour Japon
        elif user.startswith(dict_action[3]) and user.endswith("étoile"):
            if "Levier à tête d'étoile" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier à tête d'étoile" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    japan_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")
        
        #afficher inventaire 
        elif user in liste_inventaire:
            inventaire.afficher()  

        else: 
            print("""
                        Commande invalide !
                    """)

def usa_play(currentScore):
    usa_room = rooms.UsaRoom()
    print(usa_room.beginning())
    #slowprint(usa_room.beginning())
 
    while True:
        user = input("Que souhaitez-vous faire : ").lower().strip()
    
        # regarder par la fenêtre
        if user.startswith(dict_unaction[0]) and user.endswith(liste_fenetre):
            print("""
                        Il fait beau et chaud à l'extérieur.
                        Vous apercevez des plantes au coin.
                """)

        # examiner machine
        elif user.startswith(dict_unaction[0]) and user.endswith("machine"):
            usa_room.machine()

        # examiner tas de livres
        elif user.startswith(dict_unaction[0]) and user.endswith(dict_livre[0]):
            if livres not in inventaire: 
                usa_room.livre()
                print(usa_room.examiner)
            else: 
                print(f"""
                        Ce sont plein de livres sur des sujets ésotériques.
                        """)
            
        # prendre livres
        elif user.startswith("prendre") and user.endswith(dict_livre[0]):
            answer = input("Quel livre souhaitez-vous prendre ? ")
            if answer.endswith(dict_livre[1]):
                inventaire.ajouter(livres[0])
            elif answer.endswith(dict_livre[2]):
                inventaire.ajouter(livres[1])
            elif answer.endswith(dict_livre[3]):
                inventaire.ajouter(livres[2])
                objet.ajouter("Hiéroglyphes")
            else:
                print("""
                        Merci de renseigner le titre du livre souhaité.
                        """)
        # lire livre
        elif user.startswith(dict_action[5]) and user.endswith(dict_livre[0]):
            answer = input("Quel livre souhaitez-vous lire ? ")
            #if answer.endswith(dict_livre[1]):
            if answer in livres:
                print(f"""
                        Vous ouvrez le livre : {livres[0]} 
                        et commencez votre lecture.
                        """)
                usa_room.livre()
                print(usa_room.lire)

            elif answer in livres:
                print(f"""
                        Vous ouvrez le livre : {livres[1]} 
                        et commencez votre lecture.
                        """)
                usa_room.livre()
                print(usa_room.lire)

            elif answer in livres :
                print(f"""
                        Vous ouvrez le livre : {livres[2]} 
                        et commencez votre lecture.
                        """)
                usa_room.livre()
                print(usa_room.lire)
                

        # examiner chat
        elif user.startswith(dict_unaction[0]) and user.endswith(dict_animal["nom"]):
            usa_room.chat()


        # examiner femme
        elif user.startswith(dict_unaction[0]) and user.endswith(liste_femme):
            if "Levier à tête de rouage" not in inventaire : 
                usa_room.femme()
                print(usa_room.examiner)
            else : 
                print("""
                        La femme semble apprécier un peu trop son reflet...
                        Vous préférez la laisser tranquille.
                        """) 
        elif  user.startswith(dict_unaction[1]) and user.endswith(liste_femme):
            if "Levier à tête de rouage" not in inventaire : 
                usa_room.femme()
                print(usa_room.examiner)
            else : 
                print("""
                        La femme semble apprécier un peu trop son reflet...
                        Vous préférez la laisser tranquille.
                        """) 
        # offrir DVD à la femme : 
        elif user.startswith(dict_action[2]) and user.endswith("dvd"):
            if "Dvd" in inventaire and "Levier à tête de rouage" not in inventaire:
                answer = input("A qui souhaitez-vous donner ce DVD sans boîtier ? ")
                if answer.endswith(liste_femme):
                    usa_room.femme()
                    print(usa_room.donner) 
                    inventaire.ajouter("levier à tête de rouage")
                    inventaire.enlever("Dvd")
                else: 
                    print("""
                        Pas sûr que ce soit la meilleure chose à faire.
                            """)
            else : 
                print("""
                        Encore faudrait-il avoir un DVD.
                        """)
        # offrir miroir à la femme : 
        elif user.startswith(dict_action[2]) and user.endswith("miroir"):
            if "Petit miroir" in inventaire and "Levier à tête de rouage" not in inventaire :
                answer = input("A qui souhaitez-vous donner ce miroir ? ")
                if answer.endswith(liste_femme):
                    usa_room.femme()
                    print(usa_room.donner)
                    inventaire.ajouter("levier à tête de rouage")
                    inventaire.enlever("Petit miroir") 
                else: 
                    print("""
                        Pas sûr que ce soit la meilleure chose à faire.
                            """)
            else : 
                print("""
                        Encore faudrait-il avoir un miroir.
                        """)
            

        # armoire
        elif user.startswith(dict_unaction[0]) and user.endswith(liste_armoire):
            usa_room.armoire()
        # prendre stylo
        elif user.startswith("prendre") and user.endswith(liste_stylo):
            inventaire.ajouter("stylo doré à la mine rouge")

        # changer de scène pour Préhistoire
        elif user.startswith(dict_action[3]) and user.endswith("os"):
            if "Levier à tête d'os" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier à tête d'os" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    prehist_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")
            else: 
                print("Il faudrait un levier d'abord...")

        # changer de scène Egypte
        elif user.startswith(dict_action[3]) and user.endswith("pyramide"):
            if "Levier à tête de pyramide" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier à tête de pyramide" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    egypt_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")
        
        # changer de scène pour Japon
        elif user.startswith(dict_action[3]) and user.endswith("étoile"):
            if "Levier à tête d'étoile" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier à tête d'étoile" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    japan_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")

        # changer de scène futur
        elif user.startswith(dict_action[3]) and user.endswith("rouage"):
            if "Levier à tête de rouage" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier à tête de rouage" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    futur_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")
        
        #afficher inventaire 
        elif user in liste_inventaire:
            inventaire.afficher()  

        else: 
            print("""
                        Commande invalide !
                    """)

def futur_play(currentScore):
    futur_room = rooms.FuturRoom()
    #slowprint(futur_room.beginning())
    print(futur_room.beginning())

    while True:
        user = input("Que souhaitez-vous faire : ").lower().strip()

        # regarder par la fenêtre
        if user.startswith(dict_unaction[0]) and user.endswith(liste_fenetre):
            print("""
                        Il ne fait pas beau et chaud à l'extérieur.
                        Vous n'apercevez rien au coin à cause de la grisaille.
                """)

        # examiner machine
        elif user.startswith(dict_unaction[0]) and user.endswith("machine"):
            futur_room.machine()

        # examiner ordinateur
        elif user.startswith(dict_unaction[0]) and user.endswith("ordinateur"):
            futur_room.ordinateur()
            print(futur_room.examiner)
        # utiliser ordinateur
        elif user.startswith(dict_action[6]) and user.endswith("ordinateur"):
            futur_room.ordinateur()
            print(futur_room.utiliser)
                

        # examiner chat
        elif user.startswith(dict_unaction[0]) and user.endswith(dict_animal["nom"]):
            futur_room.chat()


        # examiner femme
        elif user.startswith(dict_unaction[0]) and user.endswith(liste_femme):
            futur_room.femme()
        elif user.startswith(dict_unaction[1]) and user.endswith(liste_femme):
            futur_room.femme()
        

        # armoire
        elif user.startswith(dict_unaction[0]) and user.endswith(liste_armoire):
            if "Armoire métal" not in objet : 
                futur_room.armoire()
                print(futur_room.examiner)
            else :
                print("""
                        Une importante impression de modernité se dégage
                        de ce meuble, dont la porte est grande ouverte.
                        """)

        # rentrer le code (rentrer - code, appuyer - clavier/tactile, déverrouiller - meuble)
        elif user.startswith(dict_action[7]) and user.endswith(liste_code):
            if "Armoire métal" not in objet : 
                answer = input("Quel est le code : ").lower().strip()
                if answer == "spongy":
                    futur_room.armoire()
                    print(futur_room.code)
                    objet.ajouter("Armoire métal")
                else: 
                    print("""
                        Code invalide.
                            """)
            else: 
                print("""
                        Le meuble est ouvert et laisse apparaître une malette
                        contenant deux levier : un levier à tête de plume
                        et un levier à tête de clef.
                        """)
            
       # prendre levier plume + mort
        elif user.startswith("prendre") and user.endswith("plume"):
            if "Armoire métal" in objet : 
                inventaire.ajouter("levier à tête de plume")
            else: 
                print("""
                        Vous regardez autour de vous mais ne voyez pas
                        de levier à tête de plume... Il est peut-être caché ?
                        """)
        elif user.startswith(dict_action[3]) and user.endswith("plume"):
            if "Levier à tête de plume" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    print("""
                        Vous êtes téléporté dans un espace-temps inconnu
                        et psychédélique...
                        Vous mourrez...
                            """)
                    currentScore = scoreUpdater(currentScore)
            elif "Levier à tête de plume'" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
                        


        # prendre levier clé + gagner
        elif user.startswith("prendre") and user.endswith(liste_levier):
            if "Armoire métal" in objet : 
                inventaire.ajouter("levier à tête de clé")
            else: 
                print("""
                        Vous regardez autour de vous mais ne voyer pas
                        de levier à tête de clé... Il est peut-être caché ?
                        """)
        elif user.startswith(dict_action[3]) and user.endswith(liste_levier):
            if "Levier à tête de clé" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                        print("Le levier vient se ficher dans la machine. \nIl semble avoir été fait pour ça.\n\nLe levier s'abaisse, et dans un éclait, vous \nêtes instantanément téléporté dans le présent !\n\nEnfin ! vous revoilà dans votre époque et dans\nvotre chez-vous. Votre épouse vous regarde \nd'un air mécontent : 'Tu es en retard pour \nnotre dîner, filon !'\nFélicitations, vous avez gagné :) \n\nFIN")
                        #slowprint("Le levier vient se ficher dans la machine. \nIl semble avoir été fait pour ça.\n\nLe levier s'abaisse, et dans un éclait, vous \nêtes instantanément téléporté dans le présent !\n\nEnfin ! vous revoilà dans votre époque et dans\nvotre chez-vous. Votre épouse vous regarde \nd'un air mécontent : 'Tu es en retard pour \nnotre dîner, filon !'\nFélicitations, vous avez gagné :) \n\nFIN")
                        sys.exit("\n\nMerci d'avoir joué")
                    
            elif "Levier à tête de clé'" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)


        # changer de scène pour Préhistoire
        elif user.startswith(dict_action[3]) and user.endswith("os"):
            if "Levier à tête d'os'" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier à tête d'os" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    prehist_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")
            else: 
                print("Il faudrait un levier d'abord...")

        # changer de scène Egypte
        elif user.startswith(dict_action[3]) and user.endswith("pyramide"):
            if "Levier à tête de pyramide" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier à tête de pyramide" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    egypt_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")
        
        # changer de scène pour Japon
        elif user.startswith(dict_action[3]) and user.endswith("étoile"):
            if "Levier à tête d'étoile" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier à tête d'étoile" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    japan_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")

        # changer de scène futur
        elif user.startswith(dict_action[3]) and user.endswith("rouage"):
            if "Levier  à tête de rouage" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier  à tête de rouage" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    futur_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")

        # changer de scène USA
        elif user.startswith(dict_action[3]) and user.endswith("fleur"):
            if "Levier  à tête de fleur" not in inventaire: 
                print("""
                        Encore faudrait-il avoir un levier...
                    """)
            elif "Levier  à tête de fleur" in inventaire: 
                user_machine = input("Dans quoi ? ")
                if user_machine.endswith("machine"):
                    levier.levier()
                    print(levier.utiliser)
                    #slowprint(levier.utiliser)
                    usa_play(currentScore)
                else: 
                    print("Mais où insérer ce levier ? ")

        #afficher inventaire 
        elif user in liste_inventaire:
            inventaire.afficher()  

        else: 
            print("""
                        Commande invalide !
                    """)

main()

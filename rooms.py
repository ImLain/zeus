class Levier:
    def levier(self):
        self.utiliser = "\n\nLe levier vient se ficher dans la machine.\nIl semble avoir été fait pour ça.\n\nLe levier s'abaisse, et dans un éclair,\nvous êtes instantanément téléporté\ndans une lointaine époque.\n\n"

        return self.utiliser

class PresentRoom:
    def beginning(self):
        self.title_play = "Vous vous trouvez dans une grande pièce.\nAu milieu de cette dernière trône une table\nsur laquelle repose une étrange machine.\nDans un coin, vous apercez un tas de DVD.\nSur un pouf, un chat vous regarde, l'air\ncirconspect. Une jeune femme assise dans\nun fauteuil sirote un café fumant. Un\nangle de la pièce accueille une armoire. \nDe l'air frais entre dans la pièce par \nune grande fenêtre.\n\nIl n'y a pas de sortie.\n"
        return(self.title_play)

    def machine(self):
        self.title_machine = """
                        C'est une bien étrange machine. Elle arbore
                        un cadran qui indique 2020. Sur le côté du
                        cadran, il y a 6 petits trous qui semblent 
                        pouvoir accueillir de petits objets. 
                            """
        print(self.title_machine) 
           

    def dvd(self):
        self.examiner_dvd = """
                        Vous vous trouvez devant une jolie collection
                        de DVD. Votre regard est attiré par le DVD 
                        de "Retour vers le Futur".
                        """
        print(self.examiner_dvd) 

    def chat(self):
        self.caresser_chat = """
                        En grattant le dessus de la tête du chat, 
                        vous observez le nombre 673 inscrit sur 
                        son collier.
                        """
        print(self.caresser_chat)

    def femme(self):
        self.title_femme = """
                        "Si tu pars faire une course, sois sûr de 
                        ne pas rentrer trop tard. Nous dînons chez 
                        les Millers, ce soir."
                            """
        print(self.title_femme)  

    def armoire(self):
        self.examiner_armoire = """
                        Cette dernière est fermée par un cadenas 
                        à trois chiffres.
                            """
        self.ouvrir_armoire = """
                        A votre surprise, l'intérieur de l'armoire 
                        est pratiquement vide. Seul un levier à 
                        tête de pyramide trône ici et il semble 
                        avoir été retiré d'une machine.
                            """

        return self.examiner_armoire
        return self.ouvrir_armoire


class EgyptRoom:
    def beginning(self):
        self.title_play = "Vous vous trouvez dans une grande pièce.\nAu milieu de cette dernière trône une table\nsur laquelle repose une étrange machine.\nDans un coin, vous apercevez un tas de\ntablettes en pierre, pleines de symboles.\nSur un siège en pierre, un chat vous regarde,\nl'air hautain. Une jeune femme momifiée siège\ndans un cercueil ouvert. Un angle de la pièce\naccueille une armoire en pierre. De l'air frais\nentre dans la pièce par une grande ouverture.\n\nIl n'y a pas de sortie."

        return(self.title_play)

    def machine(self):
        self.title_machine = """
                        Le cadran de la machine affiche - 174. 
                        Sacrebleu, vous voilà bien loin de chez 
                        vous ! Et vous qui souhaitiez ne pas 
                        rentrer trop tard... Vite ! Il faut trouver 
                        un moyen de rentrer. La machine peut encore 
                        accueillir de nouveaux leviers...
                        """
        print(self.title_machine)

    def tablettes (self):
        #si le joueur a lu "Lecture facile des hiéroglyphes":
        self.examiner1 = """
                        Vous ne comprenez malheureusement rien à 
                        ces hiéroglyphes... Pourvu qu'il n'y ait 
                        rien d'important de noté ici.
                        """
        self.examiner2 = """
                        Vous lisez les tablettes. Elles indiquent : 
                        "Tremblez devant l'Eternel car la clé sera 
                        la maison mais la plume mènera au déclin".
                        """
        self.prendre = """
                        Malheureusement pour vous, les tablettes 
                        sont bien trop lourdes pour vous. Faudrait 
                        penser à faire plus de musculation...
                        """

        return self.examiner1
        return self.examiner2
        return self.prendre

    def chat(self):
        self.examiner = """
                        C'est certainement le plus beau chat 
                        que vous  ayez jamais vu, il dégage une
                        impression de grande noblesse, presque 
                        royal.
                        """
        self.caresser = """
                        Le chat refuse de se laisser caresser.
                        """
        #si le joueur pose une petite couronne sur la tête du chat : 
        self.couronne = """
                        Il descend, fier, de son siège. Sous ses 
                        fesses, vous trouvez le levier à tête d'os.
                        """
        
        return self.examiner
        return self.caresser
        return self.couronne
        
    def momie(self):
        self.examiner = """
                        Malgré un nez imposant, la jeune femme 
                        devait être d'une très grande beauté. 
                        La momification est presque parfaite, 
                        mais ce petit morceau de bandelette qui
                        dépasse éveille en vous un sentiment de 
                        travail bâclé...
                        """
        self.tirer = """
                        Oh là, qu'avez-vous fait ?
                        Le travail est maintenant tout gâché. 
                        Sous les bandelettes, vous avez tout 
                        de même dévoilé un petit miroir.
                    """
        return self.examiner
        return self.tirer

    def armoire(self):
        self.ouvrir = """
                        Après avoir péniblement ouvert la porte, 
                        vous découvrez tout un tas de pots 
                        contenant des choses toutes plus étranges 
                        les unes que les autres. Trois grosses 
                        jarres attirent votre attention. L'une 
                        contient des scorpions, une autre des vers 
                        et la dernière des scarabées, tous vivants.
                    """
        print(self.ouvrir)

    def jarres(self):
        self.scorpion = """
                        Vous plongez la main dans la jarre, et en
                        moins de quelques secondes, plusieurs 
                        dards sont plantés dans votre paume.

                        Vous êtes mort...
                        """
        self.ver = """
                        Ca chatouille !
                    """
        self.scarabée = """
                        Vous trouvez au milieu des insectes un 
                        levier à tête d'étoile.
                        """
        return self.scorpion
        return self.ver
        return self.scarabée


class JapanRoom:
    def beginning(self):
        self.title_play = "Vous vous trouvez dans une grande pièce. Au\nmilieu de cette dernière trône une table en\njade sur laquelle repose une étrange machine.\nDans un coin, vous apercevez une pile de \nparchemins. \nSur un siège en bambou, un panda roux vous \nregarde, l'air jovial. Une geisha joue \ntranquillement du koto assise sur le sol. Un\nangle de la pièce accueille une armoire rouge,\nornée de signes dorés. De l'air frais entre\ndans la pièce par une grande fenêtre coulissante.\n\nIl n'y a pas de sortie."
        return(self.title_play)

    def machine(self):
        self.title_machine = """
                        Le cadran de la machine affiche 1312. Oups !
                        Vous semblez encore bien loin de chez vous.
                        J'espère que votre feeme ne s'inquiète pas trop...
                        """
        print(self.title_machine)

    def parchemins (self):
        self.examiner = """
                        Ce sont de très jolis parchemins en papier de 
                        riz soigneusement roulés et maintenus par des
                        rubans de soie.
                        """
        self.deplier = """
                        Vous découvrez que cette époque vous un culte 
                        important à la Lune.
                        """

        return self.examiner
        return self.deplier

    def panda(self):
        self.examiner = """
                        Nul animal n'a jamais été aussi mignon, vous 
                        avez du mal à vous contenir tant vous avez 
                        envie de prendre ce panda dans vos bras.
                        """
        self.taper = """
                        Vous venez de blesser le panda roux.
                        Un ninja surgit de nul part et vous tue !
                        """
        
        return self.examiner
        return self.taper

    def geisha(self):
        self.examiner = """
                        C'est une femme magnifique qui joue divinement
                        de son instrument. Alors que vous l'observez, 
                        elle vous désigne un petit bol à côté d'elle 
                        en affirmant : "Mon seigneur n'apprécie pas 
                        mon spectable ? "
                        """
        self.pierre = """
                        La geisha offre en remerciement le levier à 
                        tête de fleur.
                    """
        return self.examiner
        return self.pierre

    def armoire(self):
        self.examiner = """
                        C'est un meuble imposant. Il semble être fermé
                        par un mécanisme étrange... Il y a sur les portes
                        des signes en relief : une lune, un soleil, un 
                        shuriken et un crâne.
                    """
        self.appuyer_soleil = """
                        Rien ne se passe
                        """    
        self.appuyer_crane = """
                        Vous déclenchez un piège qui propage du gaz
                        dans la pièce. Vous êtes mort !
                        """
        self.appuyer_shuriken = """
                        Un ninja apparaît brièvement. Il dit : 
                        "Touchez pas à mon panda, hein !"
                        """
        self.appuyer_lune = """
                        L'armoire s'ouvre. Elle contient de nombreux
                        bibelots sans intérêt ; néanmoins une petite
                        couronne égyptienne attire votre regard.
                        """

        return self.examiner
        return self.appuyer_soleil
        return self.appuyer_crane
        return self.appuyer_shuriken
        return self.appuyer_lune


class PrehisRoom:
    def beginning(self):
        self.title_play = "Vous vous trouvez dans une grande pièce. Au \nmilieu de cette dernière se trouve un grand \nrocher sur lequel repose une étrange machine.\nDans un coin, vous apercevez un tas de pierres\ntaillées. Sur une pierre, un petit dinosaure \nvous regarde, l'air affamé. Un primate à l'air \npeu évolué joue avec des os dans un coin. Un \nangle de la pièce accueille deux grandes \npierres qui semblent former un rangement. De \nl'air frais entre dans la pièce par un grand \ntrou dans le mur.\n\nIl n'y a pas de sortie."
        return(self.title_play)

    def machine(self):
        self.title_machine = """
                        Le cadran de la machine affiche - 227 345 231.
                        Oh là là, vous n'arriverez jamais à l'heure
                        pour votre dîner.
                        """
        print(self.title_machine)

    def pierre (self):
        self.examiner = """
                        C'est un tas de cailloux, plus ou moins taillés.
                        Dissimulé sous les cailloux, un éclat brillant
                        attire votre attention.
                        """
        self.fouiller = """
                        En fouillant au milieu de ce tas de cailloux, 
                        vous trouvez une pierre particulière.
                        """

        return self.examiner
        return self.deplier

    def dinosaure(self):
        self.examiner = """
                        Il a beau être chou, il reste un animal dangereux
                        et carnivore. Il vaut mieux faire attention et ne
                        pas trop s'approcher.
                        """
        self.taper = """
                        Le dinosaure, complètement sauvage, vous dévore !
                        Vous êtes mort.
                        """
        
        return self.examiner
        return self.taper
     
        
    def primate(self):
        self.examiner = """
                        Vous sentez qu'il n'y a pas grand chose à tirer
                        de cette créature encore trop peu humaine...
                        """
        print(self.examiner)

    def armoire(self):
        self.examiner = """
                        Ces deux grandes pierres semblent former un 
                        rangement...
                    """
        self.ouvrir = """
                        Vous peinez à ouvrir ce qui semble être un 
                        rangement rudimentaire. Dedans, il y a des
                        cailloux, des pierres et des roches; Rien de 
                        très intéressant.
                        """    

        return self.examiner
        return self.ouvrir

class UsaRoom:
    def beginning(self):
        self.title_play = "Vous vous trouvez dans une grande pièce. Au\nmilieu de cette dernière trône une table en\nplastique transparent sur laquelle repose une\nétrange machine. Dans un coin, vous apercevez\nun tas de livres multicolores. Sur un tabouret\nen plastique orange, un chat vous regarde, \nl'air ailleurs. Une femme nue fait des exercices\nde yoga tantrique dans un coin. Un angle de la\npièce accueille une armoire en plastique \nmulticolore. De l'air disperse de l'encens qui\nenfume la pièce par une grande fenêtre.\n\nIl n'y a pas de sortie."
        return(self.title_play)

    def machine(self):
        self.title_machine = """
                        Le cadran de la machine affiche 1973. Il y 
                        a du mieux, peut-être que vous allez réussir
                        à rentrer chez vous.
                        """
        print(self.title_machine)

    def livre (self):
        self.examiner = """
                        Ce sont plein de livres sur des sujets 
                        ésotériques.
                        Vous pouvez notamment y trouver : 

                        - Découvrez votre vous intérieur
                        - Comment élever un singe à trois têtes
                        - Lecture facile des hiéroglyphes
                        """
        self.lire = """
                        Cela prend un peu de temps, mais vous en 
                        savez désormais beaucoup plus en la matière.
                        """ 
        return self.examiner
        return self.lire

    def chat(self):
        self.examiner = """
                        Alors que vous vous approchez du chat, ce 
                        dernier vous regarde droit dans les yeux 
                        et affirme : "miaou".
                        """
        
        print(self.examiner)
        
    def femme(self):
        self.examiner = """
                        La femme vous regarde, un air mystérieux 
                        dans son regard. Elle vous annonce : 
                        "Montre-moi mon vrai reflet."
                        """
        self.donner = """
                        Elle le brise et affirme son affranchissement 
                        quand à la suprématie de l'image. 
                        En récompense, elle vous offre, le levier à
                        tête de rouage.
                    """
        return self.examiner
        return self.donner

    def armoire(self):
        self.examiner = """
                        A l'intérieur de l'armoire se trouve un 
                        magnifique stylo doré à la mine rouge. Vous
                        apercevez également une note écrite en rouge
                        qui indique : "Note sur l'invention d'une 
                        machine temporelle par le professeur G.Rozoy".
                        La note vous apprend que la machine temporelle 
                        a été inventée par un certain Gabriel Rozoy 
                        qui semble vivre dans cet appartement. Sur 
                        la note est également inscrit à la main : 
                        "Mon mot de passe est : SPONGY"
                    """
        print(self.examiner)


class FuturRoom:
    def beginning(self):
        self.title_play = "Vous vous trouvez dans une grande pièce. Au\nmilieu de cette dernière trône une table en\nsur laquelle repose une étrange machine. \nDans un coin, vous apercevez un ordinateur.\nSur un pouf, un robot-chat vous regarde, l'air\néteint. Une femme robot huile tranquillement\nses mécanismes dans un coin. Un angle de la\npièce accueille un meuble en métal qui vous\nsemble mystérieux. De l'air pollué et odorant\ns'infiltre dans la pièce par une grille \nd'aération.\n\nIl n'y a pas de sortie."
        return(self.title_play)

    def machine(self):
        self.title_machine = """
                        Le cadran de la machine affiche 2071. 
                        C'est tout vous, ça, à ne jamais savoir 
                        vous arrêter !
                        """
        print(self.title_machine)

    def ordinateur (self):
        self.examiner = """
                        C'est un ordinateur de l'an 2071. 
                        Les progrès technologiques réalisés sont 
                        impressionnant.
                        """
        self.utiliser = """
                        Vous essayez d'utiliser l'ordinateur, mais 
                        prenez rapidement conscience que le niveau 
                        technologique de ce dernier n'est pas à 
                        votre portée.
                        """ 

        return self.examiner
        return self.utiliser

    def chat(self):
        self.examiner = """
                        C'est incroyable, en faisant abstraction 
                        de l'antenne présente sur le sommet de son 
                        crâne, ce chat ressemble parfaitement à un 
                        vrai chat.
                        Alors que vous l'observez avec insistance, 
                        il miaule : "bip bip"
                        """
        
        print(self.examiner)
        
    def femme(self):
        self.examiner = """
                        C'est incroyable, en faisant abstraction de 
                        l'antenne présente sur le sommet de son 
                        crâne, cette femme ressemble parfaitement 
                        à une vraie femme. Alors que vous l'observez
                        avec insistance, elle se présente : 
                        "Bonjour, je suis Giselle, la première femme
                        robot parfaitement autonome. Mon créateur, 
                        Gabriel Rozoy, est un génie."
                        """
        print(self.examiner)

    def armoire(self):
        self.examiner = """
                        Une importante impression de modernité se 
                        dégage de ce meuble. Sur le devant de ce 
                        dernier, un clavier tactile permet de 
                        rentrer un code et de déverrouiller le 
                        meuble.
                    """
        self.code = """
                        Le meuble s'ouvre et laisse apparaître 
                        une malette contenant deux leviers : 
                        un levier à tête de plume et un levier 
                        à tête de clef.
                    """
        return self.examiner
        return self.code


    def levier_plume(self): #la mort
        self.inserer = """
                        Le levier vient se ficher dans la machine. 
                        Il semble avoir été fait pour ça.
                        
                        Le levier s'abaisse, et dans un éclait, vous 
                        êtes instantanément téléporté dans un 
                        espace-temps inconnu et psychédélique.
                        
                        Vous êtes mort...
                        """
        print(self.inserer)

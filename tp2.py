from abc import ABC, abstractmethod
import random

class Carte (ABC) : 
    """
    Classe abstraite qui définit les cartes
    """
    def __init__(self, nom) :
        self.nom = nom
    
    @abstractmethod
    def appliquer(self,joueur) : 
        pass
    
class Joueur :
    """
    définit les joueurs
    """
    def __init__(self,nom,score :int ) :
        self.nom = nom
        self.score= score
    
    def jouerCarte(self, carte = Carte) :
        carte.appliquer(self)


class Carte_normale(Carte) :
    def __init__(self) :
        super().__init__("Carte Normale")
    
    def appliquer(self,joueur) :
        pts = random.randint(1,10)
        joueur.score += pts
        print(f"{joueur.nom} tire une care {self.nom}. \nEffet : Ajoute ",pts," points")
        print(f"Score actuel de {joueur.nom} : {joueur.score}")
        

class Carte_bonus(Carte) :
    def __init__(self) :
        super().__init__("Carte Bonus")
        
    def appliquer(self,joueur) :
        joueur.score *= 2
        print(f"{joueur.nom} tire une care {self.nom}. \nEffet : Double ses points")
        print(f"Score actuel de {joueur.nom} : {joueur.score}")

class Carte_malus(Carte) :
    def __init__(self) :
        super().__init__("Carte Malus")

    def appliquer(self,joueur) :
        joueur.score -= 5
        print(f"{joueur.nom} tire une care {self.nom}. \nEffet : Perd 5 points")
        print(f"Score actuel de {joueur.nom} : {joueur.score}")
    
class Carte_chance(Carte) :
    def __init__(self) :
        super().__init__("Carte Chance")

    def appliquer(self,joueur) :
        pts = random.randint(-5,15)
        joueur.score += pts
        if pts<0 :
            print(f"{joueur.nom} tire une care {self.nom}. \nEffet : Perd ",pts," points")
            print(f"Score actuel de {joueur.nom} : {joueur.score}")
        elif pts>0 :
            print(f"{joueur.nom} tire une care {self.nom}. \nEffet : Gagne ",pts," points")
            print(f"Score actuel de {joueur.nom} : {joueur.score}")  
        else :
            print(f"{joueur.nom} tire une care {self.nom}. \nEFFET : RIEN (carte=0)")
            print(f"Score actuel de {joueur.nom} : {joueur.score}")         


def creer_deck():
    """"
    creation de deck mélangé
    """
    deck = []
    deck += [Carte_normale() for i in range(30)]
    deck += [Carte_bonus() for i in range(6)]
    deck += [Carte_malus() for i in range(5)] 
    deck += [Carte_chance() for i in range(15)]
    random.shuffle(deck)
    return deck

def tour(joueur, deck):
    """
    creer chaque tour et enleve la carte du d"eck apres chaque tour
    """
    if deck:
        carte = deck.pop()
        joueur.jouerCarte(carte)

def lancer_partie() : 
    joueur1 = Joueur("Skander",0)
    joueur2 = Joueur("Victor",0)
    deck = creer_deck()
    print("\n          DEBUT DE PARTIE    \n     ")
    num_tour = 1

    for i in range(5) :
        print(f"\nTour {num_tour} :")
        tour(joueur1, deck)
        print("\n")
        tour(joueur2, deck)
        num_tour += 1
        print("Nombre de carte restantes dans le deck : ",len(deck))

    print("\n          FIN DE PARTIE    \n     ")
    print(f"Score final de {joueur1.nom} : {joueur1.score}\n")
    print(f"Score final de {joueur2.nom} : {joueur2.score}\n")


lancer_partie()
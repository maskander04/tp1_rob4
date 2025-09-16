import numpy as np
import math 


# -------------------- Exo1 -----------------------

def distance_robuste(d1, d2, d3) :
    """
    calcule la médiane entre trois valeurs en supprimant les valeurs abérrantes
    """
    tab = [d1,d2,d3]
    mediane = np.median(tab)
    for i in tab :
        if i <0.5*mediane or i>01.5*mediane :
            tab.remove(i)
    mediane = np.median(tab)
    return mediane

def test_type_cout(dist,type):
    """ 
    retourne la bonne distance (avec coeff) en fonction de la nature du sol
    """
    if type== 'R' :
        return dist
    if type== 'H' :
        return dist*1.5
    if type== 'S' :
        return dist*2
    if type== 'O' :
        return dist*3
    
def test_type_vitesse(type):
    """ 
    retourne la bonne vitesse en fonction de la nature du sol
    """
    if type== 'R' :
        return 2
    if type== 'H' :
        return 1.5
    if type== 'S' :
        return 1
    if type== 'O' :
        return 0.5

def cout_deplacement(x1,y1,x2,y2,type) :
    """
    retourne le cout de déplacement en fct de la distance
    """
    coord1 = [x1,y1]
    coord2 = [x2,y2]
    dist = math.dist(coord1,coord2)
    return test_type_cout(dist,type)

def temps_trajet(x1,y1,x2,y2,type) :
    """
    retourne le temps de déplacement en fct de la distance
    """
    coord1 = [x1,y1]
    coord2 = [x2,y2]
    dist = math.dist(coord1,coord2)
    vitesse = test_type_vitesse(type)
    temps = dist/vitesse
    return temps



# -------------------- Exo2 -----------------------


def distance_simple(x1,y1,x2,y2) :
    """
    calcule la distance entre 2 points
    """
    dist = math.dist([x1,y1],[x2,y2])
    return dist

class Position :
    """
    représente une position (x,y)
    """
    def __init__(self, x=0, y=0) :
        """
        initialise la position a (0,0)
        """
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        surcharge de l'opérateur +
        """
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)

    def afficher(self):
        print(f"Position(x={self.x}, y={self.y})")
    
    def distance_vers(self,other) :
        """
        calcule la distance entre 2 positions
        """
        return distance_simple(self.x,self.y,other.x,other.y)




# -------------------- Exo3 -----------------------

class Robot : 
    """
    représente un robot
    """
    def __init__(self, position =None ):
        """
        initialise le robot a une position
        """
        if position is None : 
            self.position = Position()
        else :
            self.position = position 

    def avancer_droite(self,n) :
        self.position.x = self.position.x + n

    def avancer_haut(self,n) :
        self.position.y = self.position.y + n
    
    def afficher(self):
        print(f"Robot à position (x={self.position.x}, y= {self.position.y})")
    
    def distance_vers_robot(self,autre_robot) :
        """
        calcule la distance entre 2 robots
        """
        return self.position.distance_vers(autre_robot.position)
    
    def aller_vers(self,position_cible) :
        """
        fait bouger le robot vers une position cible
        """
        while self.position.x < position_cible.x :
            self.avancer_droite(1)
        while self.position.x > position_cible.x :
            self.avancer_droite(-1)
        while self.position.y < position_cible.y :
            self.avancer_haut(1)
        while self.position.y > position_cible.y :
            self.avancer_haut(-1)
        


# -------------------- Exo4 -----------------------

class Cible :
    """
    Représente une cible à atteindre par le robot
    """
    def __init__(self, position = None, name = str) :
        self.name = name
        if position is None : 
            self.position = Position()
        else :
            self.position = position 
        
    def est_atteinte_par(self,robot) :
        """
        Vérifie si la cible est atteinte
        """
        if self.position.distance_vers(robot.position)==0 :
            return True
        else : 
            return False
        
    def distance_depuis(self, robot) :
        """
        caclcule la distance entre le robot et la cible
        """
        return self.position.distance_vers(robot.position)
    
    def afficher(self):
        print(f"{self.name} se trouve à la position : (x={self.position.x}, y= {self.position.y})")
    



# -------------------- Exo5 -----------------------

class Parcours : 
    def __init__(self) :
        self.cibles = []
  
    def ajouter_cible(self,cible) :
        """
        ajout de cible dans la liste
        """
        self.cibles.append(cible)    

    def nombre_cibles(self) :
        """
        calcule le nombre de cibles
        """
        return len(self.cibles)
    
    def cible_suivante(self,robot) :
        """
        rerourne a la cible non atteinte par le robot
        """
        for cible in self.cibles :
            if not cible.est_atteinte_par(robot) : 
                return cible 
    
    def executer_parcours(self,robot) :
        for cible in self.cibles :
            robot.aller_vers(cible.position)
    
    def afficher(self):
        print("Parcours :")
        for i, cible in enumerate(self.cibles, start=1):
            print(f"{i}. {cible.name} à Position (x={cible.position.x}, y={cible.position.y})")
            




# -------------------- Exo6 -----------------------

class Terrain :
    def __init__(self) :
        self.robots =[]
        self.parcours = None

    def afficher_etat(self):
        for i, robot in enumerate(self.robots, start=1):
            print(f"Robot {i}: Position (x={robot.position.x}, y={robot.position.y})")

    def ajouter_robot(self,robot) :
        self.robots.append(robot)
    
    def definir_parcours(self,parcours) :
        self.parcours =parcours 
    
    def lancer_mission(self) :
        for robot in self.robots :
            self.parcours.executer_parcours(robot)
            




def demonstration_complete() :
    terrain = Terrain()
    robot1 = Robot(Position(7,1))
    robot2 = Robot(Position(3, 4))
    terrain.ajouter_robot(robot1)
    terrain.ajouter_robot(robot2)
    parcours = Parcours()
    parcours.ajouter_cible(Cible(Position(2, 0), "Point A"))
    parcours.ajouter_cible(Cible(Position(8, 1), "Point B"))
    parcours.ajouter_cible(Cible(Position(12, 1), "Point C"))
    parcours.afficher()
    terrain.definir_parcours(parcours)
    print("Etat au début : ")
    terrain.afficher_etat()
    terrain.lancer_mission()
    print("Etat final : ")
    terrain.afficher_etat()

demonstration_complete()


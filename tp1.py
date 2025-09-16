import numpy as np
import math 


# -------------------- Exo1 -----------------------

def distance_robuste(d1, d2, d3) :
    tab = [d1,d2,d3]
    mediane = np.median(tab)
    for i in tab :
        if i <0.5*mediane or i>01.5*mediane :
            tab.remove(i)
    mediane = np.median(tab)
    return mediane

def test_type_cout(dist,type):
    if type== 'R' :
        return dist
    if type== 'H' :
        return dist*1.5
    if type== 'S' :
        return dist*2
    if type== 'O' :
        return dist*3
    
def test_type_vitesse(type):
    if type== 'R' :
        return 2
    if type== 'H' :
        return 1.5
    if type== 'S' :
        return 1
    if type== 'O' :
        return 0.5

def cout_deplacement(x1,y1,x2,y2,type) :
    coord1 = [x1,y1]
    coord2 = [x2,y2]
    dist = math.dist(coord1,coord2)
    return test_type_cout(dist,type)

def temps_trajet(x1,y1,x2,y2,type) :
    coord1 = [x1,y1]
    coord2 = [x2,y2]
    dist = math.dist(coord1,coord2)
    vitesse = test_type_vitesse(type)
    temps = dist/vitesse
    return temps


# Cas normal : les 3 capteurs sont cohérents
assert abs(distance_robuste(2.0, 2.1, 1.9) - 2.0) < 0.1
# Cas avec un capteur défaillant
assert abs(distance_robuste(2.0, 2.1, 15.0) - 2.05) < 0.1
# Cas limite : deux capteurs défaillants
assert abs(distance_robuste(1.0, 15.0, 20.0) - 17.5) < 0.1
# Cas extreme : tous les capteurs donnent des valeurs incohérentes
# assert distance_robuste(1.0, 15.0, 30.0) == -1 # Signale une erreur
assert cout_deplacement(0, 0, 5, 0, 'R') == 5.0 # Route horizontale
assert cout_deplacement(0, 0, 3, 4, 'H') == 7.5 # Herbe, distance=5, cout=5*1.5
assert cout_deplacement(0, 0, 0, 2, 'S') == 4.0 # Sable vertical
assert cout_deplacement(1, 1, 1, 1, 'O') == 0.0 # Pas de mouvement
assert temps_trajet(0, 0, 6, 8, 'R') == 5.0 # 10m à 2m/s = 5s
assert temps_trajet(0, 0, 3, 4, 'S') == 5.0 # 5m à 1m/s = 5s
assert temps_trajet(0, 0, 0, 1, 'O') == 2.0 # 1m à 0.5m/s = 2s


# -------------------- Exo2 -----------------------


def distance_simple(x1,y1,x2,y2) :
    dist = math.dist([x1,y1],[x2,y2])
    return dist

class Position :
    def __init__(self, x=0, y=0) :
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)

    def afficher(self):
        print(f"Position(x={self.x}, y={self.y})")
    
    def distance_vers(self,other) :
        return distance_simple(self.x,self.y,other.x,other.y)

pos1 = Position()
pos1.afficher() # Position(x=0, y=0)
pos2 = Position(3, 4)
pos2.afficher() # Position(x=3, y=4)
pos3 = pos1 + pos2
pos3.afficher() # Position(x=3, y=4)
pos1 = Position(0, 0)
pos2 = Position(3, 4)
assert pos1.distance_vers(pos2) == 5.0


# -------------------- Exo3 -----------------------

class Robot : 
    def __init__(self, position =None ):
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
        return self.position.distance_vers(autre_robot.position)
    
    def aller_vers(self,position_cible) :
        while self.position.x < position_cible.x :
            self.avancer_droite(1)
        while self.position.x > position_cible.x :
            self.avancer_droite(-1)
        while self.position.y < position_cible.y :
            self.avancer_haut(1)
        while self.position.y > position_cible.y :
            self.avancer_haut(-1)
        
robot = Robot()
robot.afficher() # Robot à position Position(x=0, y=0)
robot.avancer_droite(3)
robot.avancer_haut(4)
robot.afficher() # Robot à position Position(x=3, y=4)
robot1 = Robot(Position(0, 0))
robot2 = Robot(Position(3, 4))
assert robot1.distance_vers_robot(robot2) == 5.0
robot1.aller_vers(Position(2, 3))
assert robot1.position.x == 2
assert robot1.position.y == 3

# -------------------- Exo4 -----------------------

class Cible :
    def __init__(self, position = None, name = str) :
        self.name = name
        if position is None : 
            self.position = Position()
        else :
            self.position = position 
        
    def est_atteinte_par(self,robot) :
        if self.position.distance_vers(robot.position)==0 :
            return True
        else : 
            return False
        
    def distance_depuis(self, robot) :
        return self.position.distance_vers(robot.position)
    
    def afficher(self):
        print(f"{self.name} se trouve à la position : (x={self.position.x}, y= {self.position.y})")
    

cible = Cible(Position(5, 3), "Sortie")
cible.afficher()
robot = Robot(Position(2, 1))
assert cible.est_atteinte_par(robot) == False
assert cible.distance_depuis(robot) == distance_simple(2, 1, 5, 3)
robot.aller_vers(Position(5, 3))
assert cible.est_atteinte_par(robot) == True


# -------------------- Exo5 -----------------------

class Parcours : 
    def __init__(self, cible) :
        self.cible =cible 
        cible =[]

    def ajouter_cible(self,cible) :
            

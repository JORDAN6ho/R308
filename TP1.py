
import math

class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.x} et {self.y}"
    
    def distanceCoord(self, a: float, b: float):
        return math.sqrt((self.x - a) ** 2 + (self.y - b) ** 2)
    
    def distancePoint(self, camarade):
        return self.distanceCoord(camarade.x, camarade.y)

class Cercle:
    def __init__(self, rayon, centre=None):
        if centre is None:
            centre = Point()
        self.rayon = rayon
        self.centre = centre
    
    def diametre(self):
        return 2 * self.rayon
    
    def perimetre(self):
        return 2 * math.pi * self.rayon
    
    def surface(self):
        return math.pi * self.rayon ** 2
    
    def intersection(self, autre):
        distance = self.centre.distancePoint(autre.centre)
        if abs(self.rayon - autre.rayon) <= distance <= self.rayon + autre.rayon:
            return True
        else:
            return False
    
    def pointInclus(self, p: Point):
        return self.centre.distancePoint(p) <= self.rayon

class Rectangle:
    def __init__(self, basgauche=None, longueur: float = 1, hauteur: float = 1):
        if basgauche is None:
            basgauche = Point()
        self.basgauche = basgauche
        self.longueur = longueur
        self.hauteur = hauteur
    
    @classmethod
    
    def deuxpoints(cls, basgauche: Point, hautdroit: Point):
        longueur = hautdroit.x - basgauche.x
        hauteur = hautdroit.y - basgauche.y
        return cls(basgauche, longueur, hauteur)
    
    def surfaceRectangle(self):
        return self.longueur * self.hauteur
    
    def perimetreRectangle(self):
        return 2 * (self.longueur + self.hauteur)
    
    def pointBasGauche(self):
        return self.basgauche
    
    def pointBasDroite(self):
        return Point(
            self.basgauche.x + self.longueur,
            self.basgauche.y
        )
    def pointHautGauche(self):
        return Point(
            self.basgauche.x,
            self.basgauche.y + self.hauteur
        )
    def pointHautDroite(self):
        return Point(
            self.basgauche.x + self.longueur,
            self.basgauche.y + self.hauteur
        )
    def pointInclus(self, p: Point):
        return (
            self.basgauche.x <= p.x <= self.basgauche.x + self.longueur
            and
            self.basgauche.y <= p.y <= self.basgauche.y + self.hauteur
        )

class TriangleRectangle:
    def __init__(self, cote1, cote2, angleDroit=None):
        if angleDroit is None:
            angleDroit = Point()
        self.cote1 = cote1
        self.cote2 = cote2
        self.angleDroit = angleDroit
    
    def hypotenuse(self):
        return math.sqrt(self.cote1 ** 2 + self.cote2 ** 2)
    
    def perimetre(self):
        return self.cote1 + self.cote2 + self.hypotenuse()
    
    def surface(self):
        return (self.cote1 * self.cote2) / 2
    
    def isIsocèle(self):
        return self.cote1 == self.cote2

if __name__ == "__main__":
   

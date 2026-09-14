import math


class Point :
    def __int__(self, x : float = 0.0, y : float = 0.0) :
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} et {self.y}"

    def distanceCoord(self,a : float,b : float) :
        return math.sqrt((self.x-a)**2+(self.y-b)**2)

    def distancePoint(self, camarade):
        return self.distanceCoord(camarade.x,camarade.y)

class Cercle:
    def __init__(self, rayon, centre = None):
        if centre is None:
            centre = Point()
        self.rayon = rayon
        self.centre = centre

    def diametre (self) :
        return 2 * self.rayon

    def perimetre(self) :
        return 2*3,14*self.rayon

    def surface(self):
        return 3,14 * self.rayon ** 2

    def intersection(self,autre):
        distance = self.centre.distancePoint(autre.centre)
        if self.rayon - autre.rayon <= distance <= self.rayon + autre.rayon:
            return True
        else :
            return False

    def pointInclus(self, p : Point) :
        return self.centre.distancePoint(p) <= self.rayon

if __name__ == "__main__":
    p1 = Point()
    p2 = Point()
    c1 = Cercle(5)
    print(c1)
    Point_c1 = Point()
    c2 = Cercle(10,p1)
    print(f"diametre {c2.diametre}")
    print(f"perimetre {c2.perimetre()}")
    print(f"le point {p1} est inclus dans {c1} : {c1.pointInclus(p1)}" )

class Rectangle:
    """
    represente un rectangle defini par un
    """
    def __init__(self, basgauche, longueur : float = 0, hauteur: float = 0) :
        self.basgauche = basgauche if basgauche is None else Point()
        self.longueur = longueur
        self.hauteur = hauteur

    @classmethod
    def deuxpoints(cls, basgauche: Point, hautdroit : Point):
        longueur = hautdroit.x + basgauche.x
        hauteur = hautdroit.y + basgauche.y
        return cls(basgauche, longueur, hauteur)

    def surfaceRectangle(self) :
        return self.longueur * self.hauteur

    def perimetreRectangle(self) :
        return (self.longueur + self.hauteur)*2

    def basgauche(self):
        return self.basgauche

    def basdroite(self):
        return Point(self.basgauche + self.longueur, self.basgauche.y)

    def hautgauche(self):
        return Point()



    def hautdroite(self):

def liste(*args):
    liste = []
    for valeur in args:
        if valeur > liste:
            liste = valeur
    return liste

def seuil(a : int ,b : int ) -> int :
    """
    :param a: a est le seuil qu'on a fixé
    :param b: b est un entier qui est aléatiore
    :return: retourne si la valeur passé b est supérieur au seuil
    """
    a = 10
    b = random.randint(1, 100)
    if a >= b :
        return f"La valeur {b}ne dépasse pas le seuil qui est {a} "
    else :
        return f"La valeur {b} dépasse le seuil qui est {a}"

c = input("Voulez vous changer le seuil?")
if c == "NON":
    return None
elif c == "OUI":
    a = int(input("Le seuil sera"))
    return a

def seuilliste(*args :list, seuil:int = 3) :
    nb = 0
    for valeur in args :
        if valeur > seuil :
            nb += 1
    return nb

def dictionnaire(**kwargs):
    print(f"mon nombre sera : "
          f"'{seuilliste(24,65,78,12,65,3,4,98,7,12,13,54985)}")
    print(f"mon nombre ne sera pas : {seuilliste(21,54,87,98,65,32,3,31)}")

class Tasse :
    attribut : str = "céramique"
    def __init__(self, couleur : str, contenance : float, marque : str ):
        self._couleur = couleur
        self._contenance = contenance
        self._marque = marque

    def __str__(self):
        print(f"la tasse de matière céramique, de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance} ml")

    def contenu(self, contenance : float) :
        self.contenance = contenance
        contenance = input("Combien de ml mettez vous dans votre contenant :")
        contenance = float(contenance)
        return contenance

    def __del__(self):
        if contenance < 0:
            del self.contenance
        return contenance

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

    def surface(self):
        return 3,14 * self.rayon ** 2

    def intersection(self, autre):
        distance = self.centre.distancePoint(autre.centre)
        return 

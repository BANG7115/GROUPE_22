class Forme:
    def surface(self):
        raise NotImplementedError("La méthode surface() doit être redéfinie dans une sous-classe.")

    def perimetre(self):
        raise NotImplementedError("La méthode perimetre() doit être redéfinie dans une sous-classe.")

class Rectangle(Forme): # Classe représentant un rectangle
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def surface(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

import math

class Cercle(Forme): # Classe représentant un cercle
    def __init__(self, rayon):
        self.rayon = rayon

    def surface(self):
        return math.pi * self.rayon ** 2

    def perimetre(self):
        return 2 * math.pi * self.rayon

class Triangle(Forme): # Classe représentant un triangle
    def __init__(self, côté1, côté2, côté3):
        self.côté1 = côté1
        self.côté2 = côté2
        self.côté3 = côté3

    def perimetre(self):
        return self.côté1 + self.côté2 + self.côté3

    def surface(self):
        # Formule de Héron
        p = self.perimetre() / 2
        return (p * (p - self.côté1) * (p - self.côté2) * (p - self.côté3)) ** 0.5

class Carre(Rectangle): # Classe représentant un carré, qui est un cas particulier de rectangle
    def __init__(self, côté):
        super().__init__(côté, côté)
        
import math

class TriangleRectangle(Forme):
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def surface(self):
        return (self.base * self.hauteur) / 2

    def perimetre(self):
        hypotenuse = math.sqrt(self.base ** 2 + self.hauteur ** 2)
        return self.base + self.hauteur + hypotenuse



class Rectangle: # Classe représentant un rectangle, défini par sa longueur et sa largeur
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def surface(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

import math

class Cercle: # Classe représentant un cercle, défini par son rayon

    def __init__(self, rayon):
        self.rayon = rayon

    def surface(self):
        return math.pi * self.rayon ** 2

    def perimetre(self):
        return 2 * math.pi * self.rayon

class Triangle:
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

class Carre:
    def __init__(self, côté):
        self.côté = côté

    def surface(self):
        return self.côté * self.côté

    def perimetre(self):
        return 4 * self.côté

import math

class TriangleRectangle:
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def surface(self):
        return (self.base * self.hauteur) / 2

    def perimetre(self):
        hypotenuse = math.sqrt(self.base ** 2 + self.hauteur ** 2)
        return self.base + self.hauteur + hypotenuse

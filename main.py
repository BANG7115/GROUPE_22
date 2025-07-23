from Formes import Forme, Rectangle, Cercle, Triangle, Carre, TriangleRectangle

print("=== Tests des formes géométriques ===\n")

# Test Rectangle
rect = Rectangle(longueur=5, largeur=3)
print("Rectangle :")
print(f"Surface : {rect.surface()} cm²")
print(f"Périmètre : {rect.perimetre()} cm\n")

# Test Cercle
cercle = Cercle(rayon=4)
print("Cercle :")
print(f"Surface : {cercle.surface():.2f} cm²")
print(f"Périmètre : {cercle.perimetre():.2f} cm\n")

# Test Triangle
tri = Triangle(côté1=5, côté2=6, côté3=7)
print("Triangle :")
print(f"Surface : {tri.surface():.2f} cm²")
print(f"Périmètre : {tri.perimetre()} cm\n")

# Test Carré
carre = Carre(côté=4)
print("Carré :")
print(f"Surface : {carre.surface()} cm²")
print(f"Périmètre : {carre.perimetre()} cm\n")

# Test Triangle rectangle
tri_rect = TriangleRectangle(base=3, hauteur=4)
print("Triangle rectangle :")
print(f"Surface : {tri_rect.surface()} cm²")
print(f"Périmètre : {tri_rect.perimetre():.2f} cm")




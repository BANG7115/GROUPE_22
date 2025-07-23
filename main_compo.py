from formes_composition import Rectangle, Cercle, Triangle, Carre, TriangleRectangle

print("=== Tests — Version par composition ===\n")

# Rectangle
rect = Rectangle(longueur=6, largeur=4)
print("Rectangle :")
print(f"Surface : {rect.surface()} cm²")
print(f"Périmètre : {rect.perimetre()} cm\n")

# Cercle
cercle = Cercle(rayon=5)
print("Cercle :")
print(f"Surface : {cercle.surface():.2f} cm²")
print(f"Périmètre : {cercle.perimetre():.2f} cm\n")

# Triangle
tri = Triangle(côté1=6, côté2=7, côté3=8)
print("Triangle :")
print(f"Surface : {tri.surface():.2f} cm²")
print(f"Périmètre : {tri.perimetre()} cm\n")

# Carré
carre = Carre(côté=5)
print("Carré :")
print(f"Surface : {carre.surface()} cm²")
print(f"Périmètre : {carre.perimetre()} cm\n")

# Triangle rectangle
tri_rect = TriangleRectangle(base=3, hauteur=4)
print("Triangle rectangle :")
print(f"Surface : {tri_rect.surface()} cm²")
print(f"Périmètre : {tri_rect.perimetre():.2f} cm")

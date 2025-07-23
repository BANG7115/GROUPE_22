Classe Forme
├── + surface() : float
└── + perimetre() : float
       ↑
       │
       ├── Classe Rectangle
       │     - longueur : float
       │     - largeur  : float
       │     + surface() : float
       │     + perimetre() : float
       │
       ├── Classe Carré
       │     - côté : float
       │     + surface() : float
       │     + perimetre() : float
       │     (hérite indirectement via Rectangle)
       │
       ├── Classe Cercle
       │     - rayon : float
       │     + surface() : float
       │     + perimetre() : float
       │
       ├── Classe Triangle
       │     - côté1 : float
       │     - côté2 : float
       │     - côté3 : float
       │     + surface() : float
       │     + perimetre() : float
       │
       └── Classe TriangleRectangle
             - base    : float  
             - hauteur : float  
             + surface() : float  
             + perimetre() : float


📌 Conseils pour la version graphique :

Utiliser des flèches d’héritage (Forme → Rectangle, etc.)

Regrouper les classes dans une hiérarchie verticale

Mentionner les attributs avec - et les méthodes avec +

Si possible, ajouter une légende en bas : "Diagramme UML — version héritage du projet Formes géométriques


2è PARTIE


Classe Rectangle
--------------------------
- longueur : float
- largeur : float
+ surface() : float
+ perimetre() : float

Classe Cercle
--------------------------
- rayon : float
+ surface() : float
+ perimetre() : float

Classe Triangle
--------------------------
- côté1 : float
- côté2 : float
- côté3 : float
+ surface() : float
+ perimetre() : float

Classe Carre
--------------------------
- côté : float
+ surface() : float
+ perimetre() : float

Classe TriangleRectangle
--------------------------
- base : float
- hauteur : float
+ surface() : float
+ perimetre() : float



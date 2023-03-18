'''Voici un exemple de code pour créer un graphe 3D avec matplotlib :

```python'''
# importer les bibliothèques matplotlib et numpy
import matplotlib.pyplot as plt
import numpy as np

# créer des données pour les axes x, y et z
x = np.outer(np.linspace(-2, 2, 100), np.ones(100)) # grille x de 100 x 100 points
y = x.copy().T # grille y de 100 x 100 points
z = np.cos(x ** 2 + y ** 2) # grille z de 100 x 100 points

# tracer le graphe 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='rainbow')

# ajouter des titres et des étiquettes d'axe
ax.set_title('Surface plot 3D')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.savefig("fig.png")
# afficher le graphe
plt.show()
'''```

Ce code utilise les fonctions `np.outer` et `np.linspace` de la bibliothèque numpy pour créer des grilles de 100 x 100 points pour les axes x et y, et la fonction `np.cos` pour calculer les valeurs de z. Ensuite, la fonction `plot_surface` de matplotlib est utilisée pour créer le graphe 3D.

Les différentes lignes de code sont commentées pour expliquer ce qu'elles font, ce qui facilitera votre compréhension.'''

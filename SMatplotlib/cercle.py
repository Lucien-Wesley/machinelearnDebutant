import numpy as np
import matplotlib.pyplot as plt

#on definit les angles, on sait que un cercle vas de 0 à 2pi
theta = np.linspace(0, 2*np.pi, 100)

#on definit le rayon du cercle, mais on aura besoin de la racine de celle-ci
R = 1.0
r = np.sqrt(R)

#on definit les coordonées des axes sachant que sur x=r*cos(theta) et y=r*sin(theta)
x1 = r*np.cos(theta)
x2 = r*np.sin(theta)

fig, ax = plt.subplots(1)

#on donne aux axes les points pour etre dessiner
ax.plot(x1, x2)
#ce qui suit juste ici c'est pour avoir une echelle de 1/1
ax.set_aspect(1)

plt.xlim(-1.25,1.25)
plt.ylim(-1.25,1.25)

#juste pour ajouter une grille
plt.grid(linestyle='-')

#on donne un titre à la figure
plt.title('Comment dessiner un cercle avec matplotlib ?', fontsize=8)

#on enregistre le graphe sous forme d'image png
plt.savefig("plot_circle_matplotlib_01.png", bbox_inches='tight')

plt.show()

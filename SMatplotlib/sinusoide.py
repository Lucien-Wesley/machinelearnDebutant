import matplotlib.pyplot as plt 
import numpy as np  
x = np.arange(0, 10, 0.1) 
y = np.sin(x)  
plt.plot(x, y) 
plt.xlabel('x') 
plt.ylabel('y') 
plt.title('Exemple de graphique sinusoïdal')  
plt.show() 

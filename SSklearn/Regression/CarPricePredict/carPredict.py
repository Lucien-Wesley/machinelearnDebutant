from sklearn.linear_model import LinearRegression

# Charger les données d'entraînement et de test
x_entrainement = [...] # données d'entraînement
y_entrainement = [...] # étiquettes des données d'entraînement
x_test = [...] # données de test

# Créer un modèle de régression linéaire
modele = LinearRegression()
modele.fit(x_entrainement, y_entrainement)

# Prévoir les ventes pour les données de test et calculer le coefficient de détermination (R²)
ventes_test = modele.predict(x_test)
r_squared = modele.score(x_test, ventes_test_reelles)

print("Le coefficient de détermination des ventes est : ", r_squared)

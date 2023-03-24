from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Charger les données d'entraînement et de test
emails_entrainement = [...] # données d'entraînement
etiquettes_entrainement = [...] # étiquettes des données d'entraînement
emails_test = [...] # données de test

# Transformer les données en vecteurs de compte
vectoriseur = CountVectorizer()
vecteur_entrainement = vectoriseur.fit_transform(emails_entrainement)
vecteur_test = vectoriseur.transform(emails_test)

# Créer le classifieur bayésien naïf Multinomial
classifieur = MultinomialNB()
classifieur.fit(vecteur_entrainement, etiquettes_entrainement)

# Prévoir les étiquettes pour les données de test et calculer l'exactitude
etiquettes_test = classifieur.predict(vecteur_test)
exactitude = (etiquettes_test == etiquettes_test_reelles).mean()

print("L'exactitude de la détection de spam est : ", exactitude)

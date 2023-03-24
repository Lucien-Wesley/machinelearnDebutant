import cv2

# Charger la cascade de classifiers Haar
cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# Charger l'image
image = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
# Convertir l'image en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image avec visages détectés', gray)

# Détecter les visages dans l'image en utilisant la cascade Haar
faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Dessiner un rectangle autour de chaque visage détecté
for (x, y, w, h) in faces:
	cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Afficher l'image avec les visages détectés
cv2.imshow('Image avec visages détectés', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

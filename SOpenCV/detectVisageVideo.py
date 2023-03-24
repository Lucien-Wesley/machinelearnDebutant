import cv2

# Charger la cascade de classifiers Haar
face_cascade=cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")

# Charger la video
cap=cv2.VideoCapture("video.mp4")

while True:
    # on lit la video pour recuperer chaque frame
    ret, frame=cap.read()
    # Convertir l'image en niveaux de gris
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Détecter les visages dans l'image en utilisant la cascade Haar
    face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(28, 28))
    # Dessiner un rectangle autour de chaque visage détecté
    for x, y, w, h in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    # Afficher la frame avec les visages détectés
    cv2.imshow('video', frame)
    key=cv2.waitKey(1)&0xFF
    # Si on clique sur q, on arrete la boucle
    if key==ord('q'):
        break
    # Si on clique si a, on fait une avance de 100 frame dans la video
    if key==ord('a'):
        for cpt in range(100):
            ret, frame=cap.read()

cap.release()
cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture(0)  # Abre la cámara
if not cap.isOpened():
    print("no se pudo abrir la camara")

while True:
    ret, frame = cap.read()  # Lee la imagen de la cámara
    if not ret:
        print("no se pudo recibir la imagen de la camara")
        break
    cv2.imshow('Imagen de la Cámara', frame)  # Muestra la imagen
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Presiona 'q' para salir
        break

cap.release()
cv2.destroyAllWindows()


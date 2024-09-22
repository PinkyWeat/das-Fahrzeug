import cv2
import os
import time

# Configurar la cámara
cap = cv2.VideoCapture(0)

# Crear una carpeta para guardar las imágenes
output_dir = "dataset"
os.makedirs(output_dir, exist_ok=True)

# Contador para el nombre de las imágenes
contador = 0

print("Capturando imágenes automáticamente...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo capturar la imagen de la cámara.")
        break

    # Guardar imagen cada segundo
    img_name = f"{output_dir}/imagen_{contador}.jpg"
    cv2.imwrite(img_name, frame)
    print(f"Imagen guardada: {img_name}")
    contador += 1

    time.sleep(1)  # Espera de 1 segundo entre capturas

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


""" script for capturing images until quit """
import cv2
import os
import time


# configure camera
cap = cv2.VideoCapture(0)

# create dir for saving images
output_dir = "dataset"
os.makedirs(output_dir, exist_ok=True)

contador = 0

print("Capturing images...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("!!! could not capture images !!!.")
        break

    # Guardar imagen cada segundo
    img_name = f"{output_dir}/imagen_{contador}.jpg"
    cv2.imwrite(img_name, frame)
    print(f"SAVED IMAGE: {img_name}")
    contador += 1

    time.sleep(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


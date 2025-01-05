""" script for testing the camera """
import cv2


cap = cv2.VideoCapture(0)  # opens camera
if not cap.isOpened():
    print("could not open camera")

while True:
    ret, frame = cap.read()  # reads image from camera
    if not ret:
        print("could not read image from camera")
        break
    cv2.imshow('image from cameraa', frame)  # shows image
    if cv2.waitKey(1) & 0xFF == ord('q'):  # on pressing q -> quits
        break

cap.release()
cv2.destroyAllWindows()


import os
import cv2

# opens camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

os.makedirs('saved_frames', exist_ok=True)

num_frames_to_save = 15
frame_count = 0

while frame_count < num_frames_to_save:
    ret, frame = cap.read()  # Capture frame by frame

    if not ret:
        print("Failed to grab frame")
        break

    # save the frame as an image file
    filename = f'saved_frames/frame_{frame_count}.jpg'
    cv2.imwrite(filename, frame)  # Display the frame
    print(f"Saved: {filename}")

    frame_count += 1

cap.release()
print("Finished capturing frames.")

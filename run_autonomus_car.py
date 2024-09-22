""" lets run the autonomus car !! """
import cv2
import time
import serial
import logging
import tensorflow as tf


# setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("starting the autonomous car script")

# load the trained model
logger.info("loading the trained model from 'coche_autonomo_model.h5'")
model = tf.keras.models.load_model('coche_autonomo_model.h5')
logger.info("model loaded successfully")

# configure communication with arduino
arduino_port = '/dev/ttyACM0'
logger.info(f"configuring communication with Arduino on port {arduino_port}")
try:
    arduino = serial.Serial(arduino_port, 9600)
    logger.info("communication with Arduino established")
except Exception as e:
    logger.error(f"failed to establish communication with Arduino: {e}")
    exit()

# capture video from the camera (adjust the camera ID if necessary)
camera_id = 0
logger.info(f"starting video capture from camera with ID {camera_id}")
cap = cv2.VideoCapture(camera_id)

if not cap.isOpened():
    logger.error(f"failed to open camera with ID {camera_id}")
    exit()

def enviar_comando_arduino(comando):
    """ sends cmd to arduino """
    arduino.write(comando.encode())
    print(f"cmd sent: {comando}")

while True:
    ret, frame = cap.read()

    if not ret:
        logger.warning("failed to read frame from the camera, ending video capture")
        break

    # preprocess the image
    resized_frame = cv2.resize(frame, (64, 64))
    normalized_frame = resized_frame / 255.0
    input_data = normalized_frame.reshape(1, 64, 64, 3)

    # make prediction with the model
    prediction = model.predict(input_data)
    action = prediction.argmax()  # 0 = move forward, 1 = move backward, 2 = stop
    logger.info(f"prediction made, action: {action}")

    # send command to Arduino based on the prediction
    if action == 0:
        enviar_comando_arduino('A')  # command to move forward
        logger.info("sent command to Arduino: move forward")
    elif action == 1:
        enviar_comando_arduino('R')  # command to move backward
        logger.info("sent command to Arduino: move backward")
    elif action == 2:
        enviar_comando_arduino('S')  # command to stop
        logger.info("sent command to Arduino: stop")

    # display the captured frame
    #cv2.imshow('Autonomous Car', frame)

    # exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        logger.info("key 'q' pressed, exiting the loop")
        break

# release the camera and close windows
logger.info("releasing the camera and closing all windows")
cap.release()
cv2.destroyAllWindows()
logger.info("script finished")

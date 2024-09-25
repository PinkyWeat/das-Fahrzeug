""" script for training the model """
import os
import logging
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# logging setup - the DevOps complex
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("Script for training the model started")

train_dir = 'train'
validation_dir = 'validation'

# processing of images & generation of batches 4 training
logger.info("Setting up ImageDataGenerators")
train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)

# load training and validation data
logger.info(f"Loading training data from {train_dir}")
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(64, 64),
    batch_size=32,
    class_mode='categorical'
)

logger.info(f"Loading validation data from {validation_dir}")
validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(64, 64),
    batch_size=32,
    class_mode='categorical'
)

# model creation !!!
logger.info("Creating the model")
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')  # Three classes: avanzar, retroceder, parar
])

# compiling the model
logger.info("Compiling the model")
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# actually train the model
logger.info("Starting model training")
model.fit(train_generator, epochs=10, validation_data=validation_generator)
logger.info("Model training completed")

# saving the model omg!!!
model_save_path = 'autonomus_car_model.h5'
logger.info(f"Saving the model to {model_save_path}")
model.save(model_save_path)
logger.info("Model saved successfully")

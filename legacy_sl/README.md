# das Fahrzeug

## Introduction
This project is focused on developing a self-driving car system capable of navigating autonomously in a controlled environment. The system uses computer vision techniques and deep learning models to understand its surroundings and make driving decisions.

## Project Structure
- `arduino/`: Directory for arduino movement scripts.
- `raw_data/`: Directory for all the data gathered in raw, without any filtering.
- `train/`: Directory containing training images.
- `utils/`: Directory for all utility scripts.
- `validation/`: Directory containing validation images.
- `coche_autonomo_model.h5`: The trained model file.
- `run_autonomous_car.py`: The main script to run the autonomous driving system.
- `train_model.py`: Script for training the model.

## Features
- Real-time object detection for navigation.
- Autonomous driving with three main actions: advance, reverse, stop.
- Deep learning model trained on custom datasets.

## Technologies Used
- Python
- Micropython
- TensorFlow and Keras for deep learning.
- OpenCV for image processing.

## Hardware Used
- Raspberry Pi 4b
- Arduino Nano RP2040
- Motor Drivers L298N
- Logical Switches (3.3v-5v)
- Motors
- Dupont Wires
- Protoboard
- Zendure Supertank 26800mah (optional but the best on a budget)

## Tools of preference
- VS Code (Nachop theme)
- Thonny for Arduino
- Terminal as always
- Microsoft RDP

## Installation
1. Clone the repository:

> https://github.com/PinkyWeat/das-Fahrzeug.git

2. Install the required Python packages:

> pip install tensorflow opencv-python

** I strongly suggest creating a venv.**

## Training the Model
The model was trained using a custom dataset categorized into three classes: avanzar (advance), retroceder (reverse), and parar (stop). The training script processes the images and trains a convolutional neural network (CNN) model.

To retrain the model, run:

> python train_model.py

*Note: Ensure you have a `train/` and `validation/` directory with categorized images.*

## Running the Autonomous Car
To start the autonomous driving system, execute:

> python run_autonomous_car.py

## Contributing
I'd me more than amazed to have contributors! If you have improvements or bug fixes, please open a pull request!

## License
This project is licensed under me? I loved doing it :D

## Acknowledgments
- Special thanks to the TensorFlow and OpenCV communities for their invaluable resources.
- Credit to @robloxhackerman for inspo on robotics setup and Brian my boyfriend for his invaluable support!
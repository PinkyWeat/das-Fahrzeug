# das-Fahrzeug

Welcome to the das-Fahrzeug repository! This project contains the implementation of a custom Gym environment for simulating a real traffic light system, along with a pre-trained DQN model.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Repository Structure](#repository-structure)
- [Environment Details](#environment-details)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Introduction

The das-Fahrzeug project aims to simulate a real traffic light system using a custom Gym environment. The environment interacts with a camera and an Arduino to control actions and capture observations. A pre-trained DQN model is provided to demonstrate the environment's capabilities.

## Installation

To get started with this project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/pinkyweat/das-Fahrzeug.git
cd das-Fahrzeug
pip install -r requirements.txt
```

## Usage
To run the environment and interact with the pre-trained DQN model, use the following command:

>  ``` python run.py ```

To train a new DQN model, use the following command:

> ``` python train.py ```


## Repository Structure
- `run.py`: Main script to run the environment and interact with the trained model.
- `train.py`: Script to train a new DQN model for the environment.
- `realtrafficlightenv.py`: Implementation of the RealTrafficLightEnv class, defining the custom Gym environment.
- `real_traffic_light_dqn.zip`: Pre-trained DQN model for the RealTrafficLightEnv environment.

##  Environment Details

#### RealTrafficLightEnv
The RealTrafficLightEnv class simulates a real traffic light system. It uses a camera to capture frames and an Arduino to control actions.

#### Observation Space
- 64x64 RGB frames
- Pixel values in the range [0, 1]

#### Action Space
- `0`: Move forward
- `1`: Move backward
- `2`: Stop


## Methods
- `__init__(self, render_mode=None)`: Initializes the environment, sets up observation and action spaces, and establishes connections to the camera and Arduino.
- `reset(self)`: Resets the environment and returns the initial observation.
- `step(self, action)`: Executes the given action, captures the next observation, calculates the reward, and returns the observation, reward, done flag, and additional info.
- `close(self)`: Closes the camera connection.
- `_send_action_to_arduino(self, action)`: Sends the chosen action to the Arduino.
- `_get_observation(self)`: Captures a frame from the camera, resizes it to 64x64, normalizes it, and returns the observation.
- `_detect_flag_color(self, observation)`: Detects whether a green or red flag is visible in the given observation.
- `_compute_reward(self, action, flag_color)`: Calculates the reward based on the correctness of the action versus the detected flag color.

## Model Details
The `real_traffic_light_dqn.zip` file contains a pre-trained DQN model for the `RealTrafficLightEnv environment`. This model can be used to demonstrate the environment's capabilities and serve as a starting point for further training and experimentation.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.
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
- [License](#license)
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

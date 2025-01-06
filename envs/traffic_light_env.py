""" Custom Gym env for simulating traffic lights """
import gym
from gym import spaces
import numpy as np
import cv2

class TrafficLightEnv(gym.Env):
    def __init__(self):
        super(TrafficLightEnv, self).__init__()
        # action space: 0 = Stop, 1 = Move Forward
        self.action_space = spaces.Discrete(2)
        
        # observation space: Simulated traffic light images (64x64 RGB)
        self.observation_space = spaces.Box(low=0, high=255, shape=(64, 64, 3), dtype=np.uint8)
        
        self.current_light = "red"  # initial state of the light
        self.done = False
        self.step_count = 0
        self.max_steps = 50

    def reset(self):
        self.current_light = "red"
        self.done = False
        self.step_count = 0
        return self._get_observation()

    def step(self, action):
        self.step_count += 1
        reward = 0
        
        # check if agent's action was correct
        if self.current_light == "red" and action == 0:
            reward = 1  # Correctly stopped at red light
        elif self.current_light == "green" and action == 1:
            reward = 1  # Correctly moved on green light
        else:
            reward = -1  # Incorrect action

        # switch light for next step
        self.current_light = "green" if self.current_light == "red" else "red"
        
        # end of episode after max steps
        if self.step_count >= self.max_steps:
            self.done = True

        return self._get_observation(), reward, self.done, {"current_light": self.current_light}

    def _get_observation(self):
        # simulate traffic light image
        img = np.zeros((64, 64, 3), dtype=np.uint8)
        if self.current_light == "red":
            cv2.circle(img, (32, 32), 10, (255, 0, 0), -1)  # Red light
        else:
            cv2.circle(img, (32, 32), 10, (0, 255, 0), -1)  # Green light
        return img

    def render(self):
        # render the current traffic light image
        img = (self._get_observation() * 255).astype(np.uint8)
        cv2.imshow("Traffic Light Environment", img)
        cv2.waitKey(1)


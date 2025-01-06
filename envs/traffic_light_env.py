""" Custom Gym env for simulating traffic lights """
""" Custom Gym env for simulating traffic lights """
import gym
from gym import spaces
import numpy as np
import cv2

class TrafficLightEnv(gym.Env):
    def __init__(self):
        super(TrafficLightEnv, self).__init__()
        # Action space: 0 = Stop, 1 = Move Forward
        self.action_space = spaces.Discrete(2)

        # Observation space: Simulated traffic light images (64x64 RGB)
        self.observation_space = spaces.Box(low=0, high=255, shape=(64, 64, 3), dtype=np.uint8)

        self.current_light = "red"  # Initial state of the light
        self.done = False
        self.step_count = 0
        self.max_steps = 50

    def reset(self, seed=None, options=None):
        """Resets the environment to its initial state."""
        super().reset(seed=seed)  # Set the random seed (optional)
        self.current_light = "red"
        self.done = False
        self.step_count = 0
        return self._get_observation(), {}

    def step(self, action):
        """Executes one time step in the environment."""
        self.step_count += 1
        reward = 0
        
        print(f"Before switch: Light={self.current_light}, Action={action}")

        # Reward based on current light state
        if self.current_light == "red" and action == 0:
            reward = 1  # Correctly stopped at red light
        elif self.current_light == "green" and action == 1:
            reward = 1  # Correctly moved on green light
        else:
            reward = -1  # Incorrect action

        # Switch light for the next step
        self.current_light = "green" if self.current_light == "red" else "red"
        
        print(f"After switch: Light={self.current_light}")

        # check for termination
        terminated = False
        truncated = self.step_count >= self.max_steps

        return self._get_observation(), reward, terminated, truncated, {"current_light": self.current_light}

    def _get_observation(self):
        """Generates the current traffic light image."""
        img = np.zeros((64, 64, 3), dtype=np.uint8)
        if self.current_light == "red":
            cv2.circle(img, (32, 32), 10, (255, 0, 0), -1)  # Red light
        else:
            cv2.circle(img, (32, 32), 10, (0, 255, 0), -1)  # Green light
        return img

    def render(self, mode="human"):
        """Renders the current state of the environment."""
        img = self._get_observation()
        cv2.imshow("Traffic Light Environment", img)
        cv2.waitKey(1)

    def close(self):
        """Cleans up resources when the environment is closed."""
        cv2.destroyAllWindows()


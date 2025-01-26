""" Custom Gym Environment """
import gym
import cv2
import numpy as np
import serial
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class RealTrafficLightEnv(gym.Env):
    def __init__(self, render_mode=None):
        super(RealTrafficLightEnv, self).__init__()

        # Observation Space
        # feeds 64x64 RGB frames, each pixel in [0..1]
        self.observation_space = gym.spaces.Box(
            low=0.0,
            high=1.0,
            shape=(3, 64, 64),  # Channels-First
            dtype=np.float32
        )

        # Action Space
        # 0 = forward, 1 = backward, 2 = stop
        self.action_space = gym.spaces.Discrete(3)

        # Hardware Section
        # Camera
        self.cap = cv2.VideoCapture(0)  # or 1, if 0 doesn't work
        # Arduino Connection
        arduino_port = '/dev/ttyACM0'
        self.arduino = serial.Serial(arduino_port, 9600)
        
        # optional: keep track of steps
        self.current_step = 0

    def reset(self):
        """ resets the environment """
        self.current_step = 0
        obs = self._get_observation()
        return obs

    def step(self, action):
        """
        1. Sends the chosen action to the arduino
        2. Waits for a short time so the car moves
        3. Reads the camera image for the *next* observation
        4. Detects what color flag is currently visible (green or red)
        5. Calculates reward based on correctness of action vs. color
        6. Returns (observation, reward, done, info)
        """
        self._send_action_to_arduino(action)
        
        # let the action take effect physically
        time.sleep(0.2)

        # Next camera image
        obs = self._get_observation()

        # determine which flag color is visible
        flag_color = self._detect_flag_color(obs)  # "green", "red", or None

        # calculate reward
        reward = self._compute_reward(action, flag_color)

        self.current_step += 1
        # Decide if episode ends
        done = False   # not ending, but num of steps can be chosen

        info = {}
        return obs, reward, done, info

    def close(self):
        """ cleanly closes camera conection """
        self.cap.release()
        cv2.destroyAllWindows()

    # ****** Helper methods ******

    def _send_action_to_arduino(self, action):
        """ converts numeric action into a char, sends it to arduino """
        if action == 0:
            cmd = 'A'  # forward
            logger.info("sent command to Arduino: move forward")
        elif action == 1:
            cmd = 'R'  # backward
            logger.info("sent command to Arduino: move backward")
        else:
            cmd = 'S'  # stop
            logger.info("sent command to Arduino: stop")
        self.arduino.write(cmd.encode())

    def _get_observation(self):
        """ Captures frame from camera,
        resize to 64x64,
        normalize,
        finally return (64,64,3)
        """
        ret, frame = self.cap.read()
        if not ret:
            # upon camera read fails, returns a blank observation
            return np.zeros((64, 64, 3), dtype=np.float32)

        # 1. Resize
        frame_resized = cv2.resize(frame, (64, 64))

        # 2. Normalize [0..1]
        frame_normalized = frame_resized.astype(np.float32) / 255.0

        # transpose to CHW -> (3,64,64)
        frame_transposed = np.transpose(frame_normalized, (2, 0, 1))

        return frame_transposed

    def _detect_flag_color(self, observation):
        """
          Detects whether a green or red flag is visible in the given observation
          Steps:
          1. 'observation' is a (3, 64, 64) tensor with values in [0..1], suitable for PyTorch (channels-first)
          2. Continue by transposing it to (64, 64, 3) to match OpenCV's preferred format (height, width, channels)
          3. Then scale it from [0..1] up to [0..255] and convert to 'uint8' so OpenCV can process it
          4. Switch from BGR to HSV color space
          5. Create masks for green and red pixels, counting how many pixels match each color
          6. If enough green pixels are found, return "green" (yeah, yeah we ain't driving in the countryside)
             If enough red pixels are found, return "red"
             Otherwise, return None (no flag detected)
        """
        # `observation` is (3, 64, 64), channels-first
        # transpose it back to (64, 64, 3) for OpenCV
        frame_chlast = np.transpose(observation, (1, 2, 0))  # now (64, 64, 3)
        
        # Scale up to 0..255 for easier color detection
        frame_255 = (frame_chlast * 255).astype(np.uint8)

        # Convert to HSV
        hsv = cv2.cvtColor(frame_255, cv2.COLOR_BGR2HSV)

        # definition of color
        green_lower = np.array([35, 100, 100])   # Hue ~35-85
        green_upper = np.array([85, 255, 255])

        red_lower1 = np.array([0, 100, 100])    # Hue ~0-10
        red_upper1 = np.array([10, 255, 255])
        red_lower2 = np.array([170, 100, 100])  # Hue ~170-180
        red_upper2 = np.array([180, 255, 255])

        # Create masks
        green_mask = cv2.inRange(hsv, green_lower, green_upper)
        red_mask1 = cv2.inRange(hsv, red_lower1, red_upper1)
        red_mask2 = cv2.inRange(hsv, red_lower2, red_upper2)
        red_mask = red_mask1 | red_mask2

        # If we detect enough green, call it green
        if cv2.countNonZero(green_mask) > 50:
            return "green"

        # If we detect enough red, call it red
        if cv2.countNonZero(red_mask) > 50:
            return "red"

        # no color/flag found
        return None

    def _compute_reward(self, action, flag_color):
        """
          If the flag is green, the best action is forward (action=0).
          If the flag is red, the best action is stop (action=2).
          Maybe backward (action=1), upcoming action..
        """
        if flag_color == "green":
            # +1 if action=0 (forward), -1 otherwise
            return 1.0 if (action == 0) else -1.0
        elif flag_color == "red":
            # +1 if action=2 (stop), -1 otherwise
            return 1.0 if (action == 2) else -1.0
        else:
            # If no flag is detected, go forward, -1 otherwise
            return 1.0 if (action == 0) else -1.0

# ===========================================================
# DIRECT ENVIRONMENT TEST - best for development from my pov
# ===========================================================
#if __name__ == "__main__":
#    env = RealTrafficLightEnv()
#    obs = env.reset()
#
#    for i in range(1000):
#        # picks a random action from {0,1,2}
#        action = env.action_space.sample()
#        obs, reward, done, info = env.step(action)
#        print(f"Step {i} -> Action: {action}, Reward: {reward}, Done: {done}")
#
#        if done:
#            environment signals done, reset
#            obs = env.reset()
#
#    env.close()


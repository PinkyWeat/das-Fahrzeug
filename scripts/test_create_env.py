import gymnasium as gym
import envs  # Ensure this runs the register() code

env = gym.make("TrafficLightEnv-v0")
print("Environment created successfully!")


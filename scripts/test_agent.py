import gym
from stable_baselines3 import DQN
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import envs
import envs.traffic_light_env

# loading env and trained model
model = DQN.load("models/simulated_traffic_light_dqn")
env = gym.make("TrafficLightEnv-v0")

# test them model
obs, _ = env.reset()  # Reset now returns a tuple (obs, info)
for _ in range(50):   # Run for 50 steps
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)
    env.render()
    print(f"Action: {action}, Reward: {reward}, Terminated: {terminated}, Truncated: {truncated}, Info: {info}")

    if terminated or truncated:
        obs, _ = env.reset()

env.close()

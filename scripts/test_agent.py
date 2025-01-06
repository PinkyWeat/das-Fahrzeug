import gym
from stable_baselines3 import DQN

import envs.traffic_light_env

# loading env and trained model
env = gym.make("TrafficLightEnv-v0")
model = DQN.load("models/simulated_traffic_light_dqn")

# test them model
obs = env.reset()
for _ in range(100):
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    #env.render()  # Visualize the environment
    print(f"Action: {action}, Reward: {rewards}, Info: {info}")
    if done:
        obs = env.reset()

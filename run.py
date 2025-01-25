import gym
from stable_baselines3 import DQN
from RealTrafficLightEnv import RealTrafficLightEnv

# creates environment
env = RealTrafficLightEnv()

# loads the trained model
model = DQN.load("real_traffic_light_dqn.zip")

# run (inference) loop
obs = env.reset()
done = False

while True:
    # use the trained model to pick the best action
    action, _states = model.predict(obs, deterministic=True)
    
    # executes action in the environment
    obs, reward, done, info = env.step(action)
    
    # print action and reward
    print(f"Action: {action}, Reward: {reward}")

    # a conditional can be added for 'done', so to reset environment
    if done:
        obs = env.reset()


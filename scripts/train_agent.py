import sys
import os
import gym
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import envs
import envs.traffic_light_env

print("Registered environments:", gym.envs.registry.keys())

# creates environment
env = gym.make("TrafficLightEnv-v0")

# creates DQN agent
model = DQN(
        "CnnPolicy",
        env,
        verbose=1,
        tensorboard_log="./logs/",
        buffer_size=50000,
)

# trains model
model.learn(total_timesteps=5000)

# saving trained model
model.save("models/simulated_traffic_light_dqn")
print("Model saved!")


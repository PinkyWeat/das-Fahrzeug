import gym
from RealTrafficLightEnv import RealTrafficLightEnv
from stable_baselines3 import DQN

# creates the c environment (headless for ssh run)
env = RealTrafficLightEnv(render_mode=None)  # or just RealTrafficLightEnv() if screen's available

# create DQN model
model = DQN(
    policy="CnnPolicy",            # args are positional
    env=env,                       # so order must be kept
    policy_kwargs={"normalize_images": False},
    learning_rate=1e-4,
    buffer_size=5000,
    learning_starts=1000,
    batch_size=32,
    verbose=1,
)

# train for n timesteps
model.learn(total_timesteps=3000)
model.save("real_traffic_light_dqn")


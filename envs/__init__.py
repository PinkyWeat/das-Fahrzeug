from gym.envs.registration import register

register(
    id="TrafficLightEnv-v0",
    entry_point="envs.traffic_light_env:TrafficLightEnv",
)
print("TrafficLightEnv-v0 is being registered!")


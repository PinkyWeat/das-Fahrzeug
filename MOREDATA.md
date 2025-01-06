# Running Train Agent
Over the envs env

## Logs at runtime shown explanation

----------------------------------
| rollout/            |          |
|    ep_len_mean      | 50       |
|    ep_rew_mean      | 41.3     |
|    exploration_rate | 0.05     |
| time/               |          |
|    episodes         | 84       |
|    fps              | 24       |
|    time_elapsed     | 174      |
|    total_timesteps  | 4200     |
| train/              |          |
|    learning_rate    | 0.0001   |
|    loss             | 0        |
|    n_updates        | 1024     |
----------------------------------

> `Rollout`
- Episode Length Mean: avg episode length. Shown at 50.
- Episode Reward Mean: avg reward per episode. Shown at 41.3, indicating agent's taking good actions.
- Exploration Rate: using epsilon-greedy, showing at this point in time not too frequent exploration.

> `Time`
- Episodes: number of completed episodes.
- FPS: frames per second during training, 24 is okay for CPU-based setup.
- Total Time Steps: num of time steps processed so far.

> `Train`
- Learning Rate: learning rate used by the optimizer, shown at 0.0001 which indicates the Q-network's learning effectively.
- Loss: loss during training. 0 is "perfect".
- n_updates: number of updates made to the Q-network. Current 1024 shows replay buffer is being utilized to improve policy.

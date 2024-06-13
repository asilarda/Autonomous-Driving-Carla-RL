from stable_baselines3 import PPO
import os
from environment import CarEnv
import time

'''
this is to start training a new RL model/policy
'''

print('Beginning of training script')

models_dir = f"models/{int(time.time())}/"
log_dir = f"logs/{int(time.time())}/"

print('initialized log and models folders')

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

print("connecting to environment...")

env = CarEnv()

env.reset()
print("Environment has been reset as part of launch")
model = PPO('MlpPolicy', env, verbose=1, learning_rate=0.001, tensorboard_log=log_dir) # PPO model from stable baselines 3

TIMESTEPS = 500_000
iters = 0

while iters<5:
    iters += 1
    print(f'Iteration {iters} is about to start...')
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f'PPO')
    print(f'Iteration {iters} has been trained')
    model.save(f'{models_dir}/{TIMESTEPS*iters}')

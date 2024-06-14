# Autonomous-Driving-Carla-RL

# Carla: https://carla.readthedocs.io/en/latest/start_introduction/

**use the same versions of Carla, e.g. 9.15 of the sim and Carla Python module 9.15

the sim should be running before starting the train.py script**

### There only exists builds for Linux and Windows. However there are issue on GitHub on how to build it on MacOS here: 

https://github.com/carla-simulator/carla/issues/150  
https://github.com/carla-simulator/carla/pull/5086
https://github.com/carla-simulator/carla/issues/176

## Two options to install Carla:
### 1. Build from source:
https://carla.readthedocs.io/en/latest/build_carla/
https://carla.readthedocs.io/en/latest/build_linux/
https://carla.readthedocs.io/en/latest/build_windows/

### 2. Install package (less tideous way and preferred way to run this project)
https://carla.readthedocs.io/en/latest/start_quickstart/

Either choose from the docs:
1. Debian Package (Ubuntu 18.04 recommended, Ubuntu 20.04 not officialy supported)
Currently there is a problem with the dist.carla.com server. The following issue comment might solve the problem: https://github.com/carla-simulator/carla/issues/7017#issuecomment-1908462106 

2. Package installation from GitHub repo

The docs explain every step needed to make Carla run.

## What I did?

I implemented a Self Driving Agent in a simulation environment called "Carla". For the model I used stable baselines 3 with the PPO model. The agent (self-driving car) is, depending on the situation caused by his actions, rewarded or punished via a reward counter for each episode. I took inspiration namely from @FullSimDriving, @carlasimulator8782, @sentdex on YouTube.

Terminology:
Episode: An episode represents a complete attempt by the car to "survive" and maximize rewards in the simulation. It starts with spawning a new car and ends when the car crashes or the episode duration limit is reached. In this context, an episode runs for 15 seconds. If the car crashes or invades a lane, the episode ends, and a new one begins, with the agent being penalized accordingly. Both crashes and lane invasions are detected using the collision sensor and lane invasion sensor of the Carla API.

Timestep: A timestep is a single frame of the simulation. During each timestep, the car receives a camera image and the reward from the previous step, makes a decision on control inputs, and sends these inputs to the simulation. Essentially, a timestep can be considered as one second, though it may be shorter if processing is fast.

Reward Logic: This is the algorithm applied at each timestep to calculate the reward based on the car's performance. The reward logic reflects the desired behavior that the car needs to learn. It guides the agent toward specific goals, such as staying on the road and avoiding obstacles.

Policy/Model: In reinforcement learning, the policy or model defines the rules or behavior that the agent learns. It dictates what actions to take based on the camera images received. The policy evolves during training sessions to improve performance over time.

Iterations: Iterations refer to training sessions comprising multiple episodes and timesteps. During an iteration, the policy/model is updated and refined. At the end of each iteration, the current policy is saved to a new file, allowing for testing and comparison of models at different training stages.


A loss function might be useful so that the agent follows the middle of the lane without mildly zickzacking.

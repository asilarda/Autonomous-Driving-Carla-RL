# Autonomous-Driving-Carla-RL

Carla: https://carla.readthedocs.io/en/latest/start_introduction/

There only exists builds for Linux and Windows. However there are issue on GitHub on how to build it on MacOS here: 

https://github.com/carla-simulator/carla/issues/150  
https://github.com/carla-simulator/carla/pull/5086
https://github.com/carla-simulator/carla/issues/176

Two options to install Carla:
1. Build from source
2. Install package (less customization for development but fine to run this project)



1. Step: https://carla.readthedocs.io/en/latest/start_quickstart/

Either install:
1. Debian Package (for Ubuntu 18.04, possibly 20.04)




2. Package installation from GitHub repo




I implemented a Self Driving Agent in a deterministic environment. For the model I used stable baselines 3 with the PPO model. The agent (self-driving car) is, depending on the situation caused by his actions, rewarded or punished via a reward counter for each episode. 

One episode is bascially, in this context, a simulation run.

Currently one episode runs for 15 seconds.

If the car crashes a new episode starts and the agent is being punished.

If the car invades a line the episode ends and a new one starts and the agent is being punished by the same amount as the car crash. (at least for now)

Both the car crash and lane invasion are determnined via the collision sensor and lane invasion sensor of Carla API.

A timestep basically can be seen as a single frame per second (not considering that a timestep might be less than 1 second if eg.: processing is slow). 

A loss function might be useful so that the agent follows the middle of the lane without mildly zickzacking.

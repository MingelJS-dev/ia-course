# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import gym

environment = gym.make("BipedalWalker-v3")
environment.reset()

for _ in range(2000):
    environment.render()
    environment.step(environment.action_space.sample())
    
environment.close()
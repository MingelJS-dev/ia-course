# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:44:13 2020

@author: PC
"""

from gym import envs

env_names = [env.id for env in envs.registry.all()]

for name in sorted(env_names):
    print(name)
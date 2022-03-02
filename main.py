#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from ray import ray
from media import *


rays = []

# initial ray
r0 = ray()
r0.r = np.array([0.5,0,0])
r0.s = np.array([0,0,1])
r0.eikonal = 0
rays.append(r0)

# calculation efficiency
dt = 0.01
Max_Steps = 1000

for j in tqdm(range(0,Max_Steps)):
    A = dt*getD(rays[j].r)
    B = dt*getD(rays[j].r+0.5*dt*getT(rays[j].r,rays[j].s)+0.125*dt*A)
    C = dt*getD(rays[j].r+dt*getT(rays[j].r,rays[j].s)+0.5*dt*B)
    nextT = getT(rays[j].r,rays[j].s)+1/6*(A+4*B+C)
    nextr = rays[j].r+dt*(getT(rays[j].r,rays[j].s)+1/6*(A+2*B))
    nexts = nextT/getn(nextr)
    # nexteikonal 
    nextray = ray()
    nextray.r = nextr
    nextray.s = nexts
    rays.append(nextray)

x = np.zeros(len(rays))
z = np.zeros(len(rays))

for j in range(0,len(rays)):
    x[j] = rays[j].r[0]
    z[j] = rays[j].r[2]

plt.plot(z,x)
plt.show()
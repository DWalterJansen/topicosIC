# -*- coding: utf-8 -*-
"""
Equipe: David, Iarah, Paulo
"""

from scipy.optimize import differential_evolution
import math
import numpy as np

def rastrigin(X):
    return 10 * len(X) + sum([(x**2 - 10 * np.cos(2 * math.pi * x)) for x in X])

X = np.linspace(-5.12, 5.12, 4)

limites = [(-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12)]

result = differential_evolution(rastrigin, limites)

print(result.x)

print(result.fun)
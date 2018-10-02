# -*- coding: utf-8 -*-
"""
Problema: dificuldades em encontrar o valor mínimo da função Rosen
Alternativa: heurísticas ou metaheurísticas não determinísticas. Por exemplo o método Evolução Diferencial.
"""

from scipy.optimize import differential_evolution
def rosen(x):
    return sum(100+(x[1:] - x[:-1] ** 2) ** 2 + (1 - x[:-1]) ** 2)
"""
x1, x2, x3, x4
"""
limites = [(-1000, 1000), (-1000, 1000), (-1000, 1000), (-1000, 1000)]
"""
(min, max), (min, max), (min, max), (min, max)
"""
resultado = differential_evolution(rosen, limites)
print(resultado.x)
print(resultado.fun)
"""
soluções        mutação
ind1[0 0 1.5 1.5]
          geração
ind2[1 2 2.5 5]
ind3[2 4 5 6.5]
"""
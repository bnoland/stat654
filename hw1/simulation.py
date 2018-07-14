import numpy as np
from scipy.stats import expon
from scipy import stats
import random

def proposal(x):
    return x + random.randint(-5,5)

density = lambda k: stats.binom.pmf(k, 100, 0.75)

def accept(x, y):
    acceptance_proba = min(1, density(y)/density(x))
    return 1 == np.random.binomial(1, acceptance_proba)

def next_state(x):
    y = proposal(x)
    if accept(x, y):
        return y
    else:
        return x


def run_chain(n, x0):
    states = []
    current = x0
    for i in range(n):
        current = next_state(current)
        states.append(current)
    return states
    
    
output = run_chain(10000, 1.0)

import matplotlib.pyplot as plt
n, bins, patches = plt.hist(output, 100, normed=1, facecolor='green', alpha=0.75)
plt.show()

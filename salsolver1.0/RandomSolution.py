import random


def RandomSolution(n_var):
    sol = range(1, n_var+1)
    for i in xrange(len(sol)):
        if random.random() < 0.5:
            sol[i] *= -1
    return sol

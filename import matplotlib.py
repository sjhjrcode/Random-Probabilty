import matplotlib.pyplot as plt
import numpy as np
import random

def simulate_drones(num_drones, num_simulations):
    counts = []
    for _ in range(num_simulations):
        positions = list(range(num_drones))
        random.shuffle(positions)
        count = sum(i == pos for i, pos in enumerate(positions))
        counts.append(count)
    return counts

num_drones = 5
num_simulations = 10000
counts = simulate_drones(num_drones, num_simulations)

plt.hist(counts, bins=range(num_drones + 2), align='left', rwidth=0.8, density=True)
plt.xlabel('Number of drones in original position')
plt.ylabel('Frequency')
plt.title('Histogram of drones in original positions')
plt.show()
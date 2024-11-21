"""An example of a ray to understand the data structure."""
import numpy as np

# the plot only works well with non-negative coordinates
ray = np.array( [ [1.0, 2.0], [3.0, 5.0] ] )
print("ray (as a matrix) = ")
print(ray)
print()

p0 = ray[0, :]
p1 = ray[1, :]
print("start (x, y) =", p0)
print("  end (x, y) =", p1)
print()

ray_vector = p1 - p0
print("ray vector (x, y) =", ray_vector)
print()

import matplotlib.pyplot as plt
plt.figure(1, figsize=(6, 4))
plt.plot(ray[:, 0], ray[:, 1], "b-")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Example of a ray")
plt.xlim(min(0.0, 0.9*min(ray[:, 0])), 1.1*max(ray[:, 0]))
plt.ylim(min(0.0, 0.9*min(ray[:, 1])), 1.1*max(ray[:, 1]))
ax = plt.gca()
ax.set_aspect('equal')
plt.gca().grid()
plt.show()


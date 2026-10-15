import random 
import matplotlib.pyplot as plt
from collections import Counter

movements = [ 
(0, 0, 1),(0, 0, -1),(0, 1, 0),
(0, 1, 1),(0, 1, -1),(0, -1, 0),
(0, -1, 1),(0, -1, -1),(1, 0, 0),
(1, 0, 1),(1, 0, -1),(1, 1, 0),
(1, 1, 1),(1, 1, -1),(1, -1, 0),
(1, -1, 1),(1, -1, -1),(-1, 0, 0),
(-1, 0, 1),(-1, 0, -1),(-1, 1, 0),
(-1, 1, 1),(-1, 1, -1),(-1, -1, 0),
(-1, -1, 1),(-1, -1, -1)
]

possible_weights = [
0.639, 0.0250, 0.270,
0.223,0.736, 0.677,
0.892, 0.086, 0.421, 
0.029, 0.218, 0.504,
0.025, 0.198, 0.649,
0.544, 0.220, 0.589,
0.809, 0.006, 0.808, 
0.698, 0.340, 0.155,
0.957, 0.336
]

steps_of_walk = 100
number_of_walks = 10

def random_walk(number_of_steps):

    x = 0
    y = 0 
    z = 0

    path = [(x,y,z)]

    for _ in range(number_of_steps):

        movement = random.choices(movements, weights=possible_weights, k=1)[0]

        x = x + movement[0]
        y = y + movement[1]
        z = z + movement[2]

        path.append((x,y,z))

    return path

all_paths = [
    random_walk(steps_of_walk) 
    for _ in range(number_of_walks)
    ]

visits = Counter(
    position 
    for walk in all_paths
    for position in walk
)

for location, count in visits.most_common(10):
    print(f"Most frequently visited postions: {location, count}")

##----------------------VISUALIZATION-----------------

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# Plot every walk
for walk in all_paths:
    xs = [p[0] for p in walk]
    ys = [p[1] for p in walk]
    zs = [p[2] for p in walk]

    ax.plot(xs, ys, zs, alpha=0.5, linewidth=1)

# Highlight the first walk's start and end
sample_path = all_paths[0]

ax.scatter(*sample_path[0], color="green",
           marker="o", s=60, label="Start")
ax.scatter(*sample_path[-1], color="red",
           marker="x", s=60, label="End of first walk")

ax.set_title(f"{number_of_walks} Random Walks")
ax.set_xlabel("East-West position")
ax.set_ylabel("North-South position")
ax.set_zlabel("Up-Down position")

ax.set_box_aspect((1, 1, 1))
ax.grid(True)
ax.legend()
plt.show()

print(f"Steps per walk: {steps_of_walk}")
print(f"Number of walks: {len(all_paths)}")
print(f"Final position of first walk: {all_paths[0][-1]}")
print(f"First 10 positions: {all_paths[0][:10]}")

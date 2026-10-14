import random
import matplotlib.pyplot as plt

movements = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1)
]

x,y = 0,0
steps = 100
path = []

for i in range(steps):

    movement = random.choice(movements)
    x += movement[0]
    y += movement[1]

    path.append((x,y))

plt.figure(figsize=(9,9))
plt.plot(path)
plt.show()

print(f"final position: {x,y}")
print(f"total number of steps: {steps}")
print(f"first 5 movements: {path[:5]}")
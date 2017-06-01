# Visualize input data from data.py to confirm data entry

import matplotlib.pyplot as plt
# import numpy as np
from data import NODES
from data import LINKS
from data import LOADS
from data import SUPPORTS

print(NODES)
print(LINKS)

# Plot
fig, ax = plt.subplots(1)  # Initiate plot
print(NODES[:][0])
# Plot NODES
for xy in range(len(NODES)):
    plt.plot(NODES[xy][1], NODES[xy][2], marker='o', color='g')

# Annotate NODES
for i, txt in enumerate([item[0] for item in NODES]):
    ax.annotate(txt, (NODES[i][1], NODES[i][2]))

# Plot LINKS
for ll in range(len(LINKS)):
    x1 = NODES[LINKS[ll][0]][1]
    x2 = NODES[LINKS[ll][1]][1]
    y1 = NODES[LINKS[ll][0]][2]
    y2 = NODES[LINKS[ll][1]][2]
    plt.plot([x1, x2], [y1, y2])

# Plot LOADS
for w in range(len(LOADS)):
    x0 = NODES[LOADS[w][0]][1]
    y0 = NODES[LOADS[w][0]][2]
    yy = y0-0.75
    w0 = LOADS[w][1]
    plt.plot([x0, x0], [y0, yy], color='r')
    plt.plot(x0, yy, 'v', markersize=8, color='r')

# Plot SUPPORTS
for ss in SUPPORTS:
    xs = NODES[ss][1]
    ys = NODES[ss][2]
    print(xs, ys)
    plt.plot(xs, ys, markersize=10, marker='^', color='k')

plt.gca().set_aspect('equal', adjustable='box')  # Same scale on axis
plt.grid(True)
plt.show()  # Show plot

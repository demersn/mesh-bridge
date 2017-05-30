import matplotlib.pyplot as plt
# import numpy as np
from data import NODES
from data import LINKS
from data import LOADS

print(NODES)
print(LINKS)

# Plot
fig, ax = plt.subplots(1)  # Initiate plot

# Plot NODES
for xy in range(len(NODES)):
    plt.plot(NODES[xy][1], NODES[xy][2], 'ro')

# Annotate NODES
for i, txt in enumerate(NODES[:][0]):
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
    plt.plot([x0, x0], [y0, yy])
    plt.plot(x0, yy, 'v')

plt.gca().set_aspect('equal', adjustable='box')  # Same scale on axis
plt.show()  # Show plot

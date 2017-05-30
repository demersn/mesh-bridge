NODES = [  # Node name, x position, y position
    [0, 0.0, 0.0],
    [1, 0.5, 1.0],
    [2, 1.0, 0.0],
    [3, 1.5, 1.0],
    [4, 2.0, 0.0],
    [5, 2.5, 1.0],
    [6, 3.0, 0.0]
    ]

LINKS = [  # Which node connected to which
    [0, 1],
    [0, 2],
    [1, 2],
    [1, 3],
    [2, 3],
    [2, 4],
    [3, 4],
    [3, 5],
    [4, 5],
    [4, 6],
    [5, 6]
    ]

LOADS = [  # On which node is the load, load
    [2, 2000]
    ]

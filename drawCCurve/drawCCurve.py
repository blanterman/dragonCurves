import matplotlib.pyplot as plt
import numpy as np

"""
Draw a segmented curve defined by a list of turns where 0 represents a right
turn, a 1 represents a left turn, a 2 represents going straight, and a 3 
represents going back. Then displaythe graph on an axis with equal scale. Used 
for drawing the C curve.
"""
def drawCurve(turns):
    # Fist line goes from (0,0) to (1, 0) toward the 'east'.
    beg_point = [0, 0]
    # Keep track of all the points
    points = [beg_point]
    points.append([1, 0])
    direction = 'e'

    # This dictionary of dictionaries will allow the lookup of the next
    # direction and what needs to be added to the current x and y values based
    # on the current direction and the turn.
    # 0 - Right Turn, 1 - left turn, 2 - straight, 3 - back
    directionChange = {
            'e':{0:['s', [0, -1]], 1:['n', [0, 1]], 2:['e', [1, 0]], 3:['w', [-1, 0]]},
            's':{0:['w', [-1, 0]], 1:['e', [1, 0]], 2:['s', [0, -1]], 3:['n', [0, 1]]},
            'w':{0:['n', [0, 1]], 1:['s', [0, -1]], 2:['w', [-1, 0]], 3:['e', [1, 0]]},
            'n':{0:['e', [1, 0]], 1:['w', [-1, 0]], 2:['n', [0, 1]], 3:['s', [0, -1]]}
            }

    # interate through the given turns and creates a list of points that the
    # turns follow
    for turn in turns:
        # Append the next point based on the last point, current direction and
        # the turn value.
        points.append([points[-1][0] + directionChange[direction][turn][1][0],
                       points[-1][1] + directionChange[direction][turn][1][1]])
        # update the direction based on the current direction, and the turn
        direction = directionChange[direction][turn][0]

    # Grab all the x and y values from the points for graphing all the lines.
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Set up the figure, axis, and plot. Plot all lines. Equalize axis scale.
    fig = plt.figure()
    ax = fig.add_subplot()
    plt.plot(x_values, y_values)
    ax.set_aspect('equal', adjustable='box')
    plt.show()


# Script code
"""
Determine the next set of turns for the curve, then send the list of
turns to be graphed.
Ask the user if they want to do the next iteration.
"""
cont = True
turns = [0]
middle = [0]
while cont:
    nextMiddle = {0:2, 2:1, 1:3, 3:0}
    drawCurve(turns)
    choice = input('do next? [y/n] ')
    if choice == 'y' or choice == 'Y':
        # Next set of curve turns is defined by combining last set of
        # turns, the next middle turn in the rotation, and the last set of
        # turns.
        oldturns = turns[:]
        middle = [nextMiddle[middle[0]]]
        turns = []
        turns = oldturns + middle + oldturns
    else:
        cont = False

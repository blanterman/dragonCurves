import matplotlib.pyplot as plt
import numpy as np

"""
Draw a segmented curve defined by a list of turns where 0 represents a right
turn and a 1 represents a left turn. Then display the graph on an axis with
equal scale. Used for drawing the dragon curve.
"""
def drawCurve(turns, title):
    # Fist line goes from (0,0) to (1, 0) toward the 'east'.
    beg_point = [0, 0]
    # Keep track of all the points
    points = [beg_point]
    points.append([1, 0])
    direction = 'e'

    # This dictionary of dictionaries will allow the lookup of the next
    # direction and what needs to be added to the current x and y values based
    # on the current direction and the turn.
    directionChange = {
            'e':{0:['s', [0, -1]], 1:['n', [0, 1]]},
            's':{0:['w', [-1, 0]], 1:['e', [1, 0]]},
            'w':{0:['n', [0, 1]], 1:['s', [0, -1]]},
            'n':{0:['e', [1, 0]], 1:['w', [-1, 0]]}
            }

    # interate through the given turns and creates a list of points that the
    # turns follow
    for turn in turns:
        # Append the next point based on the last point, current direction and
        # the turn value (0 for right and 1 for left)
        points.append([points[-1][0] + directionChange[direction][turn][1][0],
                       points[-1][1] + directionChange[direction][turn][1][1]])
        # update the direction based on the current direction, and the turn
        direction = directionChange[direction][turn][0]

    # Grab all the x and y values from the points for graphing all the lines.
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Set up the figure, axis, and plot. Plot all lines. Equalize axis scale.
    fig = plt.figure(num='Dragon Curve')
    ax = fig.add_subplot()
    plt.plot(x_values, y_values)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')
    plt.title(title)
    plt.show()


# Script code
"""
Determine the next set of turns for the dragon curve, then send the list of
turns to be graphed.
Ask the user if they want to do the next iteration.
"""
cont = True
turns = [0]
middle = [0]
iteration = 1
title = ""
while cont:
    title = "Iteration {}".format(iteration)
    drawCurve(turns, title)
    choice = input('do next? [y/n] ')
    if choice == 'y' or choice == 'Y':
        # Next set of dragon curve turns is defined by combining last set of
        # turns swapped and reversed, the middle turn, and the last set of
        # turns again.
        iteration = iteration + 1
        oldturns = turns[:]
        begturns = [0 if turn == 1 else 1 for turn in turns]
        begturns.reverse()
        turns = []
        turns = begturns + middle + oldturns
    else:
        cont = False

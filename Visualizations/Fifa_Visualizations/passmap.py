import json
from pandas.io.json import json_normalize
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Rectangle, ConnectionPatch
from matplotlib.offsetbox import OffsetImage
import squarify
from functools import reduce

def draw_pitch(ax):

    #pitch Outline & center line
    plt.plot([0,0],[0,80], color = 'black')
    plt.plot([0,120],[80,80], color = 'black')
    plt.plot([120,120],[80,0], color = 'black')
    plt.plot([120,0],[0,0], color = 'black')
    plt.plot([60,60],[0,80], color = 'black')

    #Left Penalty Area
    plt.plot([14.6,14.6],[57.8,22.2], color = 'black')
    plt.plot([0,14.6],[57.8,57.8], color = 'black')
    plt.plot([0,14.6],[22.2,22.2], color = 'black')

    #Right Penalty Area
    plt.plot([120,105.4],[57.8,57.8], color = 'black')
    plt.plot([105.4,105.4],[57.8,22.5], color = 'black')
    plt.plot([120,105.4],[22.5,22.5], color = 'black')

    #Left 6-yard Box
    plt.plot([0,4.9],[48,48], color = 'black')
    plt.plot([4.9,4.9],[48,32], color = 'black')
    plt.plot([0,4.9],[32,32], color = 'black')

    #Right 6-yard Box
    plt.plot([120,115.1],[48,48], color = 'black')
    plt.plot([115.1,115.1],[48,32], color = 'black')
    plt.plot([120,115.1],[32,32], color = 'black')

    #Prepared Cicles
    centreCircle = plt.Circle((60, 40), 8.1, color = 'black', fill = False)
    centreSpot = plt.Circle((60, 40), 0.71, color = 'black')
    leftPenSpot = plt.Circle((9.7, 40), 0.71, color = 'black')
    rightPenSpot = plt.Circle((110.3, 40), 0.71, color = 'black')

    #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)

    #Prepare Arcs
    # arguments for Arc
    # x, y coordinate of centerpoint of arc
    # width, height as arc might not be circle, but oval
    # angle: degree of rotation of the shape, anti-clockwise
    # theta1, theta2, start and end location of arc in degree
    leftArc = Arc((9.7, 40), height=16.2, width = 16.2, angle=0, theta1=310,theta2=50, color='black')
    rightArc = Arc((110.3, 40), height=16.2, width=16.2, angle=0, theta1=130, theta2=230, color='black')

    #Draw Arcs
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)

fig = plt.figure()
fig.set_size_inches(7,5)
ax = fig.add_subplot(1,1,1)
draw_pitch(ax)
plt.show()

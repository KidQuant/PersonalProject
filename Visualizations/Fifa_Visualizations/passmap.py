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

with open('./Visualizations/Fifa_Visualizations/events/7567.json', encoding = 'utf-8') as data_file:
    data = json.load(data_file)

df = json_normalize(data, sep = "_")
ozil_pass = df[(df['type_name'] == "Pass") & (df['player_name']=='Mesut Özil')] # get passing information of Ozil
pass_column = [i for i in df.columns if i.startswith("pass")]
ozil_pass = ozil_pass[["id", "period", "timestamp", "location", "pass_end_location", "pass_recipient_name"]]
ozil_pass.head()

fig, ax = plt.subplots()
fig.set_size_inches(7, 5)
ax.set_xlim([0,120])
ax.set_ylim([0,80])
for i in range(len(ozil_pass)):
    # can also differentiate by color
    color = "blue" if ozil_pass.iloc[i]['period'] == 1 else "red"
    ax.annotate("", xy = (ozil_pass.iloc[i]['pass_end_location'][0], ozil_pass.iloc[i]['pass_end_location'][1]), xycoords = 'data',
               xytext = (ozil_pass.iloc[i]['location'][0], ozil_pass.iloc[i]['location'][1]), textcoords = 'data',
               arrowprops=dict(arrowstyle="->",connectionstyle="arc3", color = "blue"),)
plt.show()

def heat_pass_map(data, player_name):
    pass_data = data[(data['type_name'] == "Pass") & (data['player_name'] == player_name)]
    action_data = data[(data['player_name']==player_name)]

    fig=plt.figure()
    fig.set_size_inches(7, 5)
    ax=fig.add_subplot(1,1,1)
    draw_pitch(ax)
    plt.axis('off')

    for i in range(len(pass_data)):
        # we also differentiate different half by different color
        color = "blue" if pass_data.iloc[i]['period'] == 1 else "red"
        ax.annotate("", xy = (pass_data.iloc[i]['pass_end_location'][0], pass_data.iloc[i]['pass_end_location'][1]), xycoords = 'data',
               xytext = (pass_data.iloc[i]['location'][0], pass_data.iloc[i]['location'][1]), textcoords = 'data',
               arrowprops=dict(arrowstyle="->",connectionstyle="arc3", color = color),)
    x_coord = [i[0] for i in action_data["location"]]
    y_coord = [i[1] for i in action_data["location"]]
    sns.kdeplot(x_coord, y_coord, shade = "True", color = "green", n_levels = 30)
    plt.ylim(0, 80) # need this, otherwise kde plot will go outside
    plt.xlim(0, 120)
    plt.show()

heat_pass_map(df, 'Toni Kroos')

ozil_action = df[(df['player_name'] == 'Mesut Özil')][['id', 'type_name', 'period', 'timestamp', 'location']]
ozil_action.head()
ozil_action


fig, ax = plt.subplots()
fig.set_size_inches(7,5)

x_coord = [i[0] for i in ozil_action['location']]
y_coord = [i[1] for i in ozil_action['location']]

sns.kdeplot(x_coord, y_coord, shade = 'True', color = 'green', n_levels = 30)
plt.show()

def heat_pass_map(data, player_name):
    pass_data = data[(data['type_name'] == "Pass") & (data['player_name'] == player_name)]
    action_data = data[(data['player_name']==player_name)]

    fig=plt.figure()
    fig.set_size_inches(7, 5)
    ax=fig.add_subplot(1,1,1)
    draw_pitch(ax)
    plt.axis('off')

    for i in range(len(pass_data)):
        # we also differentiate different half by different color
        color = "blue" if pass_data.iloc[i]['period'] == 1 else "red"
        ax.annotate("", xy = (pass_data.iloc[i]['pass_end_location'][0], pass_data.iloc[i]['pass_end_location'][1]), xycoords = 'data',
               xytext = (pass_data.iloc[i]['location'][0], pass_data.iloc[i]['location'][1]), textcoords = 'data',
               arrowprops=dict(arrowstyle="->",connectionstyle="arc3", color = color),)
    x_coord = [i[0] for i in action_data["location"]]
    y_coord = [i[1] for i in action_data["location"]]
    sns.kdeplot(x_coord, y_coord, shade = "True", color = "green", n_levels = 30)
    plt.ylim(0, 80) # need this, otherwise kde plot will go outside
    plt.xlim(0, 120)
    plt.show()

heat_pass_map(df, 'Thomas Müller')
heat_pass_map(df, 'Toni Kroos')
heat_pass_map(df, 'Mesut Özil')

data_id = [7546, 7563, 8655, 8658, 7530, 7580, 8649]
all_france = pd.DataFrame()
for i in data_id:
    with open('./Visualizations/Fifa_Visualizations/events/'+str(i)+'.json', encoding = 'utf-8') as data_file:
        data = json.load(data_file)
    df = json_normalize(data, sep = '_')
    if all_france.empty:
        all_france = df
    else:
        all_france = pd.concat([all_france, df], join = 'outer', sort = False)

shot_data = all_france[(all_france['type_name'] == 'Shot') & (all_france['team_name'] == 'France')]

fig=plt.figure()
fig.set_size_inches(7,5)
ax=fig.add_subplot(1,1,1)
draw_pitch(ax)
plt.axis('off')

for i in range(len(shot_data)):
    color = 'red' if shot_data.iloc[i]['shot_outcome_name'] == 'Goal' else 'black'
    ax.annotate('', xy = (shot_data.iloc[i]['shot_end_location'][0], shot_data.iloc[i]['shot_end_location'][1]),
    xycoords = 'data', xytext = (shot_data.iloc[i]['location'][0], shot_data.iloc[i]['location'][1]),
    textcoords = 'data', arrowprops = dict(arrowstyle='->', connectionstyle='arc3', color = color),)

plt.ylim(0,80)
plt.xlim(0,120)
plt.show()

def draw_half_pitch(ax):
    # focus on only half of the pitch
    #Pitch Outline & Centre Line
    Pitch = Rectangle([60,0], width = 60, height = 80, fill = False)
    #Right Penalty Area
    RightPenalty = Rectangle([105.4,22.3], width = 14.6, height = 35.3, fill = False)

    #Right 6-yard Box
    RightSixYard = Rectangle([115.1,32], width = 4.9, height = 16, fill = False)

    #Prepare Circles
    centreCircle = Arc((60,40),width = 8.1, height = 8.1, angle=0,theta1=270,theta2=90,color="black")
    centreSpot = plt.Circle((60,40),0.71,color="black")
    rightPenSpot = plt.Circle((110.3,40),0.71,color="black")
    rightArc = Arc((110.3,40),height=16.2,width=16.2,angle=0,theta1=130,theta2=230,color="black")

    element = [Pitch, RightPenalty, RightSixYard, centreCircle, centreSpot, rightPenSpot, rightArc]
    for i in element:
        ax.add_patch(i)

fig=plt.figure()
fig.set_size_inches(7, 5)
ax=fig.add_subplot(1,1,1)
draw_half_pitch(ax)
plt.axis('off')
# draw the scatter plot for goals
x_coord_goal = [location[0] for i, location in enumerate(shot_data["location"]) if shot_data.iloc[i]['shot_outcome_name'] == "Goal"]
y_coord_goal = [location[1] for i, location in enumerate(shot_data["location"]) if shot_data.iloc[i]['shot_outcome_name'] == "Goal"]
# shots that end up with no goal
x_coord = [location[0] for i, location in enumerate(shot_data["location"]) if shot_data.iloc[i]['shot_outcome_name'] != "Goal"]
y_coord = [location[1] for i, location in enumerate(shot_data["location"]) if shot_data.iloc[i]['shot_outcome_name'] != "Goal"]
#put the two scatter plots on the pitch

ax.scatter(x_coord_goal, y_coord_goal, c = 'red', label = 'goal')
ax.scatter(x_coord, y_coord, c = 'blue', label = 'shots')
plt.ylim(0, 80)
plt.xlim(0, 120)
plt.legend(loc='upper right')
plt.axis('off')
plt.show()

# we use a joint plot to see the density of the shot distribution across the 2 axes of the pitch
joint_shot_chart = sns.jointplot(x_coord, y_coord, stat_func=None,
                                 kind='scatter', space=0, alpha=0.5)
joint_shot_chart.fig.set_size_inches(7,5)
ax = joint_shot_chart.ax_joint
# overlaying the plot with a pitch
draw_half_pitch(ax)
ax.set_xlim(0.5,120.5)
ax.set_ylim(0.5,80.5)
# draw the scatter plot for goals
x_coord_goal = [location[0] for i, location in enumerate(shot_data["location"]) if shot_data.iloc[i]['shot_outcome_name'] == "Goal"]
y_coord_goal = [location[1] for i, location in enumerate(shot_data["location"]) if shot_data.iloc[i]['shot_outcome_name'] == "Goal"]
# shots that end up with no goal
x_coord = [location[0] for i, location in enumerate(shot_data["location"]) if shot_data.iloc[i]['shot_outcome_name'] != "Goal"]
y_coord = [location[1] for i, location in enumerate(shot_data["location"]) if shot_data.iloc[i]['shot_outcome_name'] != "Goal"]
# put the two scatter plots on to the pitch
ax.scatter(x_coord, y_coord, c = 'b', label = 'shots')
ax.scatter(x_coord_goal, y_coord_goal, c = 'r', label = 'goal')
# Get rid of axis labels and tick marks
ax.set_xlabel('')
ax.set_ylabel('')
joint_shot_chart.ax_marg_x.set_axis_off()
ax.set_axis_off()
plt.ylim(-.5, 80)
plt.axis('off')
plt.show()

france = plt.imread('')

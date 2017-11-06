import random
from math import sqrt,cos,sin,atan2,fabs

########################################
#   Mandatory functions for the rrt    #
########################################

# Tests if the new_node is close enough to the goal to consider it a goal
def winCondition(new_node,goal_node,WIN_RADIUS):
    """
    new_node - newly generated node we are checking
    goal_node - goal node
    WIN_RADIUS - constant representing how close we have to be to the goal to
        consider the new_node a 'win'
    """
    return dist(new_node,goal_node) <= WIN_RADIUS

# Find the nearest node in our list of nodes that is closest to the new_node
def nearestNode(nodes,new_node):
    """
    nodes - a list of nodes in the RRT
    new_node - a node generated from getNewPoint
    """
    if nodes == []:
        return new_node
    distances = {}
    for n in nodes:
        distances[n] = dist(n,new_node)
    return min(distances, key = distances.get)

# Find a new point in space to move towards uniformally randomly but with
# probability 0.05, sample the goal. This promotes movement to the goal.
def getNewPoint(XDIM,YDIM,XY_GOAL):
    """
    XDIM - constant representing the width of the game
    YDIM - constant representing the height of the game
    XY_GOAL - node (tuple of integers) representing the location of the goal
    """
    a = random.random()
    if a < 0.05:
        return XY_GOAL
    else:
        w = random.uniform(0,XDIM)
        h = random.uniform(0,YDIM)
        return (w,h)

# Extend (by at most distance delta) in the direction of the new_point and place
# a new node there
def extend(current_node,new_point,delta):
    """
    current_node - node from which we extend
    new_point - point in space which we are extending toward
    delta - maximum distance we extend by
    """
    if dist(current_node,new_point) <= delta:
        return new_point
    else:
        x = new_point[0]-current_node[0]
        y = new_point[1]-current_node[1]
        theta = atan2(y,x)
        dy = sin(theta)*delta
        dx = cos(theta)*delta
        new_x = int(current_node[0]+dx)
        new_y = int(current_node[1]+dy)
        return (new_x,new_y)

# iterate throught the obstacles and check that our point is not in any of them
def isCollisionFree(obstacles,point,obs_line_width):
    """
    obstacles - a dictionary with multiple entries, where each entry is a list of
        points which define line segments of with obs_line_width
    point - the location in space that we are checking is not in the obstacles
    obs_line_width - the length of the line segments that define each obstacle's
        boundary
    """
    for key, sequence in obstacles.items():
        for i in range(len(sequence)-1):
            if point_line(point,sequence[i],sequence[i+1]) < obs_line_width:
                return False
    return True
    
################################################
#  Any other helper functions you need go here #
################################################

def dist(n1, n2):
    return sqrt((n1[0]-n2[0])**2 + (n1[1]-n2[1])**2)

def point_line(p,p1,p2):
    x = p[0]
    y = p[1]
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    d1 = dist((x,y),(x1,y1))
    d2 = dist((x,y),(x2,y2))
    
    # For vertical obstacles
    if (x1 == x2) and (min(y1,y2) <= y <= max(y1,y2)):
        return abs(x-x1)
    elif (x1 == x2):
        return min(d1,d2)
    # For horizontal obstacles
    if (y1 == y2) and (min(x1,x2) <= x <= max(x1,x2)):
        return abs(y-y1)
    elif (y1 == y2):
        return min(d1,d2)
    # For sloped obstacles
    m = float(y2-y1)/(x2-x1)
    b = y1-m*x1
    x_new = (x + m*(y-b))/(m**2+1)
    y_new = m * x_new + b

    if ((min(x1,x2) <= x_new <= max(x1,x2)) and (min(y1,y2) <= y_new <= max(y1,y2))):
        return dist(p,(x_new,y_new))
    return min(d1,d2)





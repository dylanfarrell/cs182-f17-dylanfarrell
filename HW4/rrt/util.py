import random
from math import sqrt,cos,sin,atan2

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
    pass

# Find the nearest node in our list of nodes that is closest to the new_node
def nearestNode(nodes,new_node):
    """
    nodes - a list of nodes in the RRT
    new_node - a node generated from getNewPoint
    """
    pass

# Find a new point in space to move towards uniformally randomly but with
# probability 0.05, sample the goal. This promotes movement to the goal.
def getNewPoint(XDIM,YDIM,XY_GOAL):
    """
    XDIM - constant representing the width of the game
    YDIM - constant representing the height of the game
    XY_GOAL - node (tuple of integers) representing the location of the goal
    """
    pass

# Extend (by at most distance delta) in the direction of the new_point and place
# a new node there
def extend(current_node,new_point,delta):
    """
    current_node - node from which we extend
    new_point - point in space which we are extending toward
    delta - maximum distance we extend by
    """
    pass

# iterate throught the obstacles and check that our point is not in any of them
def isCollisionFree(obstacles,point,obs_line_width):
    """
    obstacles - a dictionary with multiple entries, where each entry is a list of
        points which define line segments of with obs_line_width
    point - the location in space that we are checking is not in the obstacles
    obs_line_width - the length of the line segments that define each obstacle's
        boundary
    """
    pass

################################################
#  Any other helper functions you need go here #
################################################

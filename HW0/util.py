##### Filename: util.py
##### Author: {Dylan Farrell}
##### Date: {9/7/17}
##### Email: {dylanfarrell@college.harvard.edu}

import copy
from collections import deque

## Problem 1

def matrix_multiply(x, y):
    def dot(x, y):
        n = sum([a*b for a, b in zip(x, y)])
        return n
    lsts = []
    for i in x:
        lst = []
        for j in range(0, len(y[0])):
            lst.append(dot(i, [row[j] for row in y]))
        lsts.append(lst)
    return lsts


## Problem 2, 3

class MyQueue:
    def __init__(self):
        self.data = deque([])
    def push(self, val):
        self.data.append(val)
    def pop(self):
        if self.data:
            copy = self.data[0]
            del self.data[0]
            return copy
        else:
            return None
    def __eq__(self, other):
        return self.data == other.data
    def __ne__(self, other):
        return not(self.data == other.data)
    def __str__(self):
        return str(self.data)

class MyStack:
    def __init__(self):
        self.data = deque([])
    def push(self, val):
        self.data.append(val)
    def pop(self):
        if self.data == []:
            return None
        else:
            copy = self.data[-1]
            del self.data[-1]
            return copy
    def __eq__(self, other):
        return self.data == other.data
    def __ne__(self, other):
        return not(self.data == other.data)
    def __str__(self):
        return str(self.data)

## Problem 4

def add_position_iter(lst, number_from=0):
    return [a+number_from+i for i, a in enumerate(lst)]

def add_position_recur(lst, number_from=0):
    if lst:
        frst = [lst[0]+number_from]
        a = number_from+1
        return frst+(add_position_recur(lst[1:len(lst)], number_from=a))
    else:
        return lst

def add_position_map(lst, number_from=0):
    return list(map(lambda (x): x[0]+x[1]+number_from, enumerate(lst)))

## Problem 5

def remove_course(roster, student, course):
    roster[student].remove(course)
    return roster

## Problem 6

def copy_remove_course(roster, student, course):
    c = copy.deepcopy(roster)
    remove_course(c, student, course)
    return c


import numpy as np

# Input number of nodes, total time, list of nodes

num = open('meta.in')
adjacency = open('node_adjacency.in')
num_nodes = int(num.readline().strip())

matrix = numpy.zeros((num_nodes,num_nodes))

# consider if we want to store things here or not
locations = [dict() for i in range(num_nodes)]

# Get adjacency list
for i in range(num_nodes):
    arr = adjacency.readline().split(' ')
    index = 0
    for i in arr:
        matrix[i][index]
        index+=1

time = 10
for t in range(time):
    # iteration of the steps
    current_items, no_longer_needed_items = getData('step_%3d'%t)

    # HARDCORE LOGIC
    # Inputs:
    #   current items: list of needed items with (id, amount, time, priority)
    #   no longer needed items: list of extra items with (id, amount)
    #   map of adjacency list in matrix which connects location
    #   locations?

    # CREATE ALGORITHM HERE
    for i in range(num_nodes):
        '''
            1. at the start, iterate through locations and decrement all time values
            2. For each node, first determine what we need, (not coming yet) in transit, (t>0) and have(t=0).
            NOTE: locations[id] will contain the amount of incoming items and at what time
            3. starting at the node, BFS to find as many items as you can get as possible, keep running track of what we need,
                    and add to locations when you find things to obtain - in order of priority
                            (all priority 1, then 2, then 3, etc)
            NOTE: store incoming resources as (amount, time) in locations[]
            4. Figure out what to do with things that you have failed to find in general - if so - create a beacon maybe?
        '''

def getData(file):
    file = open(file)
    current = []
    extra = []
    for x in range(num_nodes):
        temp = file.readline().split(' ')
        index = 0
        len = temp[index]
        for number in len:
            id = temp[index * number + 0]
            amount = temp[index * number + 1]
            time_needed = temp[index * number + 2]
            priority = temp[index * number + 3]
            current.append((id,amount,time_needed,priority))
            index+=1

    for x in range(num_nodes):
        temp = file.readline().split(' ')
        index = 0
        len = temp[index]
        for number in len:
            id = temp[index * number + 0]
            amount = temp[index * number + 1]
            extra.append((id,amount));
            index+=1

    return (current, extra)

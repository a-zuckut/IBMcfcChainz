
import numpy as np

# Input number of nodes, total time, list of nodes

num = open('meta.in')
adjacency = open('node_adjacency.in')
num_nodes = int(num.readline().strip())

matrix = numpy.zeros((num_nodes,num_nodes))
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
    current_items, extra_items = getData('step_%3d'%t)

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

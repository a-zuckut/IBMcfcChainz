
import numpy as np

# Input number of nodes, total time, list of nodes

num = open('meta.in')
adjacency = open('node_adjacency.in')
num_nodes = int(num.readline().strip())

matrix = numpy.zeros((num_nodes,num_nodes))
locations = [dict() for i in range(num_nodes)]

for i in range(num_nodes):
    arr = adjacency.readline().split(' ')
    index = 0
    for i in arr:
        matrix[i][index]
        index+=1

time = 10
for t in range(time):
    # iteration of the steps

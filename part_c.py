import numpy as np
import sys

filename = raw_input('Enter the file name: ')
file = open(filename, 'r')
 #delete "[num_nodes]"
file.readline()
 #obtain the size
size = int(file.readline())
 #delete "\n"
file.readline()
 #delete "[edges]"
file.readline()

pos = np.zeros((size, size))
pos = np.matrix(pos)
#placing values given
for line in file:
	dash = line.index(' -- ')
	pos [int(line[0:dash]),  int(line[dash+4:len(line)])] = 1
	pos [int(line[dash+4:len(line)]),  int(line[0:dash])] = 1

print np.matrix(pos)
m = input("Enter the length of the path: ")
pos = pos**m
u = input("Enter vertice 1: ")
v = input("Enter vertice 2: ")
print np.matrix(pos[u,v])
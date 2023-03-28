import numpy as np
import matplotlib.pyplot as plt

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   12.16 Lab: Pretty plot
# Date:         11 / 14 / 2022
# 
#style 


Initial_point = [0,1]
Initial_Matrix = [[1.01, 0.09], [-0.09, 1.01]]

def calcualtions(Initial_point,Initial_Matrix):
    graph_values = [] #x 
    graph_values2 = [] #y
    v1 = [[0,0],[0,0]]
    for i in range(200):
        v1[0] = (Initial_Matrix[0][0] * Initial_point[0]) + (Initial_Matrix[0][1] * Initial_point[1] )
        v1[1] = (Initial_point[0] * Initial_Matrix[1][0]) + (Initial_point[1] * Initial_Matrix[1][1])
        Initial_point[0] = v1[0]
        Initial_point[1] = v1[1]
        graph_values.append(Initial_point[0])
        graph_values2.append(Initial_point[1])
    plt.plot(graph_values,graph_values2)
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.suptitle("The Shape of the plot is a Spiral")
    plt.show()
        
calcualtions(Initial_point,Initial_Matrix)       
        
        
        
        
        
        
        
        
               
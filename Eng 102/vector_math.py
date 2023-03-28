# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   7.27 Lab: Vector math
# Date:         10 / 04 / 2022
# 
#style 

from math import *

VectorA = list(map(float, input("Enter the elements for vector A: ").split()))
VectorB = list(map(float, input("Enter the elements for vector B: ").split()))

            
def magnitude(VectorA, VectorB):
    vectorA = []
    total_magnitude = 0
    for i in range(len(VectorA)):
        vectorA.append(float(VectorA[i]) ** 2)
    total_magnitude = sqrt(sum(vectorA)) 
    print(f"The magnitude of vector A is {total_magnitude:.5f}")
    vectorB = []
    total_magnitude2 = 0
    for a in range(len(VectorB)):
        vectorB.append(float(VectorB[a]) ** 2)
    total_magnitude2 = sqrt(sum(vectorB))
    print(f"The magnitude of vector B is {total_magnitude2:.5f}")
    
def adding(VectorA, VectorB):
    adding_list = []
    for x in range(len(VectorA)):
        adding = float(VectorA[x]) + float(VectorB[x])
        adding_list.append(adding)
    print("A + B is",adding_list)

def substracting(VectorA,VectorB):
    subs_list = []
    for x in range(len(VectorA)):
        subs = float(VectorA[x]) - float(VectorB[x])
        subs_list.append(subs)
    print("A - B is",subs_list)





def dot(VectorA,VectorB):
    dotproduct = 0
    for s in range(len(VectorB)):
        dotproduct += float(VectorA[s]) * float(VectorB[s]) 
    print(f"The dot product is {dotproduct:.2f}") 
#-------------------------------

magnitude(VectorA,VectorB)
adding(VectorA,VectorB)
substracting(VectorA, VectorB)
dot(VectorA,VectorB)

        
    
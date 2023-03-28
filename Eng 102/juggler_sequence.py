# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   6.14 Lab: Juggler sequence
# Date:         9 / 26 / 2022
# 
#style 

from math import *

n = int(input("Enter a positive integer: "))
count = 0
sequence = n
list = [n]

while sequence > 1:
    even_or_odd = sequence % 2
    if even_or_odd == 0:
        sequence = int(sequence**(1/2))
        list.append(sequence)
        count+=1 
    elif even_or_odd != 0:
        sequence = int(sequence**(3/2))
        list.append(sequence)
        count+= 1 
print("The Juggler sequence starting at ",n," is:")
print(*list, sep =", ")
print("It took ",count, " iterations to reach 1")
    
        
    
        
            
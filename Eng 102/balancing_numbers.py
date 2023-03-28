# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   6.15 Lab: Balancing numbers
# Date:         9 / 26 / 2022
# 
#style 

from math import *

n = int(input("Enter a value for n: "))
add = 0
for i in range (1,n): 
     add += i
r_times = int((-2*n-1+sqrt(8*(n**2)+1))/2)
LHS = n*r_times + ((r_times*(r_times+1))/2)
#(-2n-1+sqrt(8n^2+1))/2
if LHS == add:
    print(n," is a balancing number with r=",int(r_times))
else:
    print(n ,"is not a balancing number")

    

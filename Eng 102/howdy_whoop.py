# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   6.13 Lab: Howdy Whoop
# Date:         9 / 26 / 2022
# 
#style 

from math import *

first = int(input("Enter an integer: "))
second = int(input("Enter another integer: "))


for i in range(1,101):
    Division1 = i % first 
    Division2 = i % second 
    if Division1 == 0 and Division2 == 0:
        print("Howdy Whoop")
    elif Division1 == 0:
        print("Howdy")
    elif Division2 == 0:
        print("Whoop")
    else: 
        print(i)
    


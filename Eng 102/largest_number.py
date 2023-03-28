# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   4.16 LAB: Largest number
# Date:         9 / 12 / 2022
#

#comments
from math import *
num1 = float(input("Enter  number 1: "))
num2 = float(input("Enter  number 2: "))
num3 = float(input("Enter  number 3: "))

def CheckLargest(num1,num2,num3):
    list = [num1, num2, num3] #stores values on a list
    return float(max(list)) # max() check for largest value in list
print("The largest number is " + str(CheckLargest(num1,num2,num3)))
    
    
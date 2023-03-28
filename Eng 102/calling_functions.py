# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   3.18 Lab: Print Math
# Date:         9 / 10 / 2022
# 
from math import *
from sympy import *
side = float(input("Please enter the side length : "))
area = None
def printresult(shape,side,area):
    if shape == 'triangle':
        triangle_area = ((sqrt(3))/4)*(pow(side, 2))
        area = triangle_area 
        print(f'A {shape} with side {side:.2f} has area {area:.3f}')
    elif shape == 'square':
        square_area = (side)**2
        area = square_area
        print(f'A {shape} with side {side:.2f} has area {area:.3f}')
    elif shape == 'pentagon':
        pentagon_area = ((1/4)*(5)*(side**2)*cot(pi/5))
        area = pentagon_area  
        print(f'A {shape} with side {side:.2f} has area {area:.3f}')
    elif shape == 'dodecagon':
        dodecagon_area = (3 * (side**2)) * (2 + sqrt(3)) 
        area = dodecagon_area
        print(f'A {shape} with side {side:.2f} has area {area:.3f}')
# example function call:
# printresult(<string of shape name>, <float of area>, <float of side>)
printresult('triangle', side, area)
printresult('square', side, area)
printresult('pentagon', side, area)
printresult('dodecagon', side, area)

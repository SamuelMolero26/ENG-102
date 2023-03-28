# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brandon Becerra
#               Samuel Molero
#               Jackson Barge
#               Christian Flewelling
# Section:      506
# Assignment:   4.14 Lab: Pretty equation
# Date:         09 12 2022
#
#style
from math import *
from sympy import *
import re

init_printing()

x = symbols('x')
A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))
print('The quadratic equation is ', end='')
print(re.sub('^-', '- ', str(A*x**2 + B*x + C).replace('**', '^').replace('*', '')), end='')
print(' = 0')










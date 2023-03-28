
#By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:     
#               Samuel Molero
# Section:      506
# Assignment:   Lab 4.19 
# Date:         09 16 2022
#Coemments 
from math import *

Coefficient_A = float(input("Please enter the coefficient A: "))
Coefficient_B = float(input("Please enter the coefficient B: "))
Coefficient_C = float(input("Please enter the coefficient C: "))

def equationroots( Coefficient_A, Coefficient_B, Coefficient_C): 
    a = Coefficient_A
    b = Coefficient_B
    c = Coefficient_C
    
    right_side = ((b**2) - 4 * a * c)
    final = sqrt(abs(right_side))
    
    if a == 0:
        print("The root is x = ", (-c / b))
    elif right_side > 0:  
        print("The roots are x = ",((-b + final)/(2 * a))," and ","x = ",((-b - final)/(2 * a)))
         
    elif right_side == 0: 
        print("The root is x = ",(-b / (2 * a))) 
        
    else:
        print("The roots are x = ",(- b / (2 * a)), " + ", (final - 1),  "i", " and x = " , (- b / (2 * a)), " - ", (final - 1), "i" ) 

if Coefficient_A == 0 and Coefficient_B == 0: 
        print("You entered an invalid combination of coefficients!") 
else:
    equationroots(Coefficient_A, Coefficient_B, Coefficient_C)

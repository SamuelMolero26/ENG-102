# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   5.4 Lab: Boiling curve
# Date:         9 / 20 / 2022                n  
# 

from math import *
#Ask for excess
excess = float(input("Enter the excess temperature: "))

def heat_flux(excess):
    #Equation used : y = y(x/x0)^m , m = log(y1/y0)/log(x1,x0)
    x = excess # x would be the input provided by the user
    ###First Range###
    if x > 1  and x <= 5: #from point A to B
        y0 = 1000
        x0 = 1.3
        y1 = 7000
        x1 = 5
        m = log(y1/y0)/log(x1/x0) #calculate m 
        y = round((y0*(x/x0)**m)) 
        print("The surface heat flux is approximately ",y," W/m^2")
    ###Second Range###
    elif x > 5 and x <= 30: #from point B to C
        x0 = 5
        y0 = 7000
        y1 = 1.5*10**6
        x1 = 30
        m = log(y1/y0)/log(x1/x0)
        y = round((y0*(x/x0)**m))
        print("The surface heat flux is approximately ",y," W/m^2")
    ###Thrid Range### 
    elif x > 30 and x <= 120: #from point C to D
        x0 = 30     
        y0 = 1.5*10**6
        x1 = 120
        y1 = 2.5*10**4
        m = log(y1/y0)/log(x1/x0)
        y = round((y0*(x/x0)**m))
        print("The surface heat flux is approximately ",y," W/m^2")
    ###Fourth Range###
    elif x > 120 and x <= 1000: # from point D to E
        x0 = 120
        y0 = 2.5*10**4
        x1 = 1200
        y1 = 1.5*10**6
        m = log(y1/y0)/log(x1/x0)
        y = round((y0*(x/x0)**m))
        print("The surface heat flux is approximately ",y," W/m^2")
    elif x <= 0 or x > 1000: # for any values outside of the curve
        print("Surface heat flux is not available")  

heat_flux(excess)
    

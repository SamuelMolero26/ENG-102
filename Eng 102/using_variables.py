# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   1.11 Lab: Print Math
# Date:         26 / 8 / 2022
#
from math import * 

#1
mass = 3 
accelaration = 5.5                             
force = mass * accelaration
print("Force is " + str(force) + " N")

#2 
distance = (2 * 0.025)
angle = sin(radians(25))
Wavelength =  distance  * angle                   
print("Wavelength is "  + str(Wavelength) + " nm")

#3
initial_amount = 5 
half_life = 3.8 
days = 3 
halflife_and_days = (2**(-days/half_life))
Radiactive_Decay = initial_amount * halflife_and_days
print("Radon-222 left is " + str(Radiactive_Decay) + " g")  

#4
volume = 0.25 
temperature = 415
constant = 8.314
moles = 5 
Pressure = ((moles*constant*temperature)/volume)  * 10**-3
print("Pressure is " + str(Pressure)  + " kPa")     



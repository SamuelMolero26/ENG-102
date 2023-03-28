# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   3.17 Lab Using input
# Date:         9 / 9 / 2022
#
from math import *


#force
print("This program calculates the applied force given mass and acceleration")
user_mass = float(input("Please enter the mass (kg): "))
user_acceleration = float(input("Please enter the acceleration (m/s^2): "))

def force(user_mass , user_acceleration):
    mass = user_mass 
    acceleration = user_acceleration
    force_total = mass * acceleration
    return force_total

print("Force is " + str(round(force(user_mass,user_acceleration), 1)) + " N")
print()
#wavelenght
print("This program calculates the wavelength given distance and angle")
user_distance = float(input("Please enter the distance (nm): "))
user_angle = float(input("Please enter the angle (degrees): "))

def wavelenght(user_distance, user_angle):
    distance = 2 * (user_distance)
    angle = sin(radians(user_angle))
    wavelenght_total = distance * angle
    return wavelenght_total

print("Wavelength is " + str(format(wavelenght(user_distance,user_angle), ".4f")) + " nm")
print()
print("This program calculates how much Radon-222 is left given time and initial amount")
user_days = float(input("Please enter the time (days): "))
user_initial = float(input("Please enter the initial amount (g): "))
def radiactive_decay(user_initial):
    half_life = 3.8
    days = user_days
    initial_amount = user_initial
    halflife_and_days = (2**(-days/half_life))
    decay = initial_amount * halflife_and_days
    return decay 

print("Radon-222 left is " + str(round(radiactive_decay(user_initial),2)) + " g")
print()
print("This program calculates the pressure given moles, volume, and temperature")
user_moles = float(input("Please enter the number of moles: "))
user_volume = float(input("Please enter the volume (m^3): "))
user_temperature = float(input("Please enter the temperature (K): "))
def idealGas(user_moles,user_volume,user_temperature):
    moles = user_moles
    volume = user_volume
    temperature = user_temperature
    constant = 8.314 * 10 **-3
    idealGas_total = ((moles*constant*temperature)/volume)
    return idealGas_total 
print("Pressure is " + str(round(idealGas(user_moles,user_volume,user_temperature))) + " kPa")

    
    
    
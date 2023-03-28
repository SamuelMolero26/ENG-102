#By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jackson Barge
#               Brandon Becerra
#               Christian Flewelling
#               Samuel Molero
# Section:      CRN 506
# Assignment:   Lab 3.15 team
# Date:         09 09 2022
#
#
# YOUR CODE HERE
#

# comment for commenting's sake
from math import *


#define lbs to newtons conversion equation
def lbs_force_to_newtons(lbs):
    return lbs * 4.4482216153


def meters_to_feet(meters):
    return meters * 3.280839


def atmospheres_to_kilopascals(atms):
    return atms * 101.325


def watts_to_btuph(watts):
    return watts * 3.412141633


def liters_to_gallons(liters):
    return liters * 15.85032314


def celcious_to_farenheit(celcius):
    return celcius * (9 / 5) + 32


val = float(input('Please enter the quantity to be converted: '))

print('{:.2f} pounds force is equivalent to {} Newtons'.format(
    val, round(lbs_force_to_newtons(val), 2)))
print('{:.2f} meters is equivalent to {} feet'.format(
    val, round(meters_to_feet(val), 2)))
print('{:.2f} atmospheres is equivalent to {} kilopascals'.format(
    val, round(atmospheres_to_kilopascals(val), 2)))
print('{:.2f} watts is equivalent to {} BTU per hour'.format(
    val, round(watts_to_btuph(val), 2)))
print('{:.2f} liters per second is equivalent to {} US gallons per minute'.
      format(val, round(liters_to_gallons(val), 2)))
print('{:.2f} degrees Celsius is equivalent to {} degrees Fahrenheit'.format(
    val, round(celcious_to_farenheit(val), 2)))

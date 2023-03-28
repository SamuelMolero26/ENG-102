# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brandon Becerra
#               Samuel Molero
#               Jackson Barge
#               Christian Flewelling
# Section:      506
# Assignment:   6.12 Lab: Pyramid Area 2
# Date:         30 9 2022
#

#style
import math

l = float(input("Enter the side length in meters: "))

n = int(input("Enter the number of layers: "))

def surface_area_layer(n, l):
  #return (n*l) * math.sqrt((n*l)**2 - (n*l/2)**2) + (3.0*(n*l*l))
  return (3.0*(n*l*l))
  #return (((n*l) * math.sqrt((n*l)**2 - (n*l/2)**2) / 2), (n*l) * math.sqrt((n*l)**2 - (n*l/2)**2) + (3.0*(n*l*l)))


def total_gold(num_layers, side_len):
  total = (n*l) * math.sqrt((n*l)**2 - (n*l/2)**2) / 2
  total += 3*(n)*((n+1)/2) * (l*l)
  
  return total
  
surface_area = total_gold(n, l)

print("You need {:0.2f}m^2 of gold foil to cover the pyramid".format(surface_area))

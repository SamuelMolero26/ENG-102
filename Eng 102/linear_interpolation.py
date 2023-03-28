# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        MARCO VERDERAME
#               DIEGO PONCE
#               SAMUEL MOLERO
#               MATTHEW VARGHESE
#               JAMES GLENN
# Section:      102
# Assignment:   Lab 
# Date:         31 08 2022

#variables of time in minutes and distance in kilometres
import math
#time in minutes
time_1 = 10
time_2 = 55
timeVar = 25

#distance in kilometres
distance_1 = 2026
distance_2 = 23026

#((d2 - d1) / (t2 - t1)) = ((d - d1)/(t - t1))
slope = (distance_2 - distance_1)/(time_2 - time_1)

# equationAns is an arbitrary distance function
equationAns = (slope * (timeVar - time_1)) + distance_1
print("Part 1:")
print("For t = 25 minutes, the position p = ", equationAns, "kilometers")

# circumference in kilometres and timeVar in minutes
circumference = (2 * (math.pi) * 6745)
timeVar2 = 300
equationAns2 = (slope * (timeVar2 - time_1)) + distance_1

#actualDistance in kilometres
actualDistance = equationAns2 % circumference
print("Part 2:")
print("For t = 300 minutes, the position p = ", actualDistance, "kilometers")
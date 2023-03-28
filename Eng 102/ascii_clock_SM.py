# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:     Samuel Molero
#      
# Section:      506
# Assignment:   
# Date:         19 October 2022



hours = int(time.split(':')[0])
mins = int(time.split(':')[1])
if hours*100 + mins >= 2400 or mins >= 60:
  print('Error, time is not valid')
  exit(1)


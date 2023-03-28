# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brandon Becerra
#               Samuel Molero
#               Jackson Barge
#               Christian Flewelling
# Section:      506
# Assignment:   9.15 Lab: Shoelace formula 
# Date:         28 October 2022
#


def getpoints(points):
  list1 = points.split(" ")

  final_list = []
  for i in range(len(list1)):
    num = eval(list1[i]) # bad practice
    final_list.append([*num])
  
  return final_list

def cross(p1, p2):
  return (p1[0] * p2[1]) - (p2[0] * p1[1])

def shoelace(points):
  area = 0
  for i in range(len(points)-1):
    area += cross(points[i], points[i+1])

  area += cross(points[len(points)-1],points[0])
  return area / 2

def main():
  points_str = input("Please enter the vertices: ")
  points = getpoints(points_str)
  area = shoelace(points)
  print('The area of the polygon is {}'.format(area))

  

if __name__ == '__main__':
  main()

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   4.18 LAB: How many gadgets
# Date:         9 / 13 / 2022
#style
productivity = 5
days = int(input("Please enter a positive value for day: "))
def CheckProductivity(days, productivity):
    productivity = 5
    if days <= 0:
        productivity = "You entered an invalid number!"
        print(productivity)
    elif  days < 11:
        productivity = 5 * days
        print("The total number of gadgets produced on day " + str(days) +" is " + str(productivity)) 
    elif days >= 11 and days <= 60:
        productivity = (50 * (days - 10)) + 50
        print("The total number of gadgets produced on day " + str(days) +" is " + str(productivity))
    elif  days >= 61 and days <= 101:
        productivity = int((22.5 * (days))+ 1492.5)
        print("The total number of gadgets produced on day " + str(days) +" is " + str(productivity)) 
    elif days >= 102: 
        productivity = int(((22.5 * (99)) + 1492.5) + 10)
        print("The total number of gadgets produced on day " + str(days) +" is " + str(productivity)) 

CheckProductivity(days,productivity)
    
    
    
    
    
    
    

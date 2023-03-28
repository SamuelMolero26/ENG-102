# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   6.13 Lab: Howdy Whoop
# Date:         10 / 24 / 2022
# 
#style 


from math import *


import statistics

# Part A
def parta(r_sphere, r_hole): #parta()
    
    volume_sphere = (4/3)*(pi)*((r_sphere)**3)
    h =  r_sphere - sqrt((r_sphere**2)-(r_hole**2)) 
    volume_cylinder = (pi)*(((r_hole)**2)*((r_sphere * 2) - (2*h)))
    volume_endcap = (((pi)*(h**2))/3) * (3*r_sphere-h)
    Volume_final = (volume_sphere - (2*volume_endcap) - volume_cylinder)
    return Volume_final
print(parta(1,0.95))

#Part B 

def partb(n): #partb()
    oddlist = []
    if n < 10 and n % 2 == 1:
        oddlist.append(n)
        return oddlist
    elif n < 10 and n % 2 == 0:
        formula = (n-2)/2
        oddlist.append(int(formula))
        formula += 2 
        oddlist.append(int(formula))
        return oddlist
    elif n > 10 and n < 20 and n % 2 != 0:
        formula = (n-6) / 3 
        oddlist.append(int(formula))
        formula += 2
        oddlist.append(int(formula))
        formula += 2
        oddlist.append(int(formula))
        return oddlist
    elif n >= 20 and n < 100:
        formula =  (n - 9) / 6 
        oddlist.append(int(formula))
        formula += 2 
        oddlist.append(int(formula))
        formula += 2 
        oddlist.append(int(formula))
        formula += 2  
        oddlist.append(int(formula))
        formula += 2  
        oddlist.append(int(formula))
        return oddlist
    elif n >= 100 and n % 2 != 1:
        return False

print(partb(75)) 

# Part C
def partc (character,name,company,email): #partc()
    name_len = len(name)
    company_len = len(company)
    email_len = len(email)
    len_list = [name_len,company_len,email_len]
    maximum = max(len_list)
    length2 = maximum + 6
    length3 = int((maximum) + 4)
    grid = f"{character*length2}\n{character}{name.center(length3)}{character}\n{character}{company.center(length3)}{character}\n{character}{email.center(length3)}{character}\n{character*length2}"
    return grid

partc("*","Dr. Ritchey","Texas A&M University", "snritchey@tamu.edu")

# Part D
def partd(listt): #partd()
    mm = (min(listt))
    m = (statistics.median(listt))
    M = (max(listt))
    return mm, m, M
print(partd([1,2,3]))


#Part E
def parte(list1, list2): #parte()
    # formula x1-x2 / t 
    result_v = []
    previous_v = 0
    
    for i in range(len(list2)-1):
        distance = list2[i+1] - list2[i]
        time = list1[i+1] - list1[i]
        v = (distance) / (time)
        result_v.append(v)
    return result_v


#print(parte([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [-0.1, 1.5, 1.54, 3.09, 3.95, 4.78, 5.92, 7.5, 8.37, 9.03, 9.54]))

#Part F
def partf(list1): #partf()
    for i in list1:
        second_num = 2026 - i 
        if second_num in list1:
            return second_num * i 
            break 
    else:
        return False
        

print(partf([1149, 5926, 1111, 2222, 3333, 915, 5555]))


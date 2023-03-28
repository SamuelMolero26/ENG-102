# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   7.28 Lab: Kaprekar's constant
# Date:         10 / 05 / 2022
# 
#style 

from math import *

User_number = int(input("Enter a four-digit integer: "))



def kaprekar(User_number):
    n = str(User_number)
    num_list = [User_number]
    count = 0
    for i in range(len(n)-1):
        if (n[i] == n[i+1]):
            count += 1 
    if (len(n) == 1 ):
        zeros = "".join(sorted(str(n).zfill(4)))
        next_num = None
        while next_num != 0:
              zeros = "".join(sorted(str(User_number).zfill(4)))
              regular = "".join(sorted(str(User_number).zfill(4), reverse = True))
              #print(zeros, regular)
              next_num = int(regular) - int(zeros)
              num_list.append(next_num)
              User_number = next_num
              if(User_number == 6174):
                  print(*num_list, sep = " > ")
                  User_number = n
                  print(User_number,"reaches 6174 via Kaprekar's routine in",(len(num_list)-1),"iterations")
                  break
              
    else:
        pass
        if (len(n) - count != 1):
            pass
        else:
            next_num = None
            while next_num != 0:
              zeros = "".join(sorted(str(User_number).zfill(4)))
              regular = "".join(sorted(str(User_number).zfill(4), reverse = True))
              #print(zeros, regular)
              next_num = int(regular) - int(zeros)
              num_list.append(next_num)
              User_number = next_num
              if(User_number == 0):
                  print(*num_list, sep = " > ")
                  User_number = n
                  print(User_number,"reaches 0 via Kaprekar's routine in",(len(num_list)-1),"iterations")
                  break
            
    
    if (len(n) + count == 1) or (len(n) - count == 1) and (len(n) > 3) :
        pass
    else:
        next_num = None
        while next_num != 0:
              zeros = "".join(sorted(str(User_number).zfill(4)))
              regular = "".join(sorted(str(User_number).zfill(4), reverse = True))
              #print(zeros, regular)
              next_num = int(regular) - int(zeros)
              num_list.append(next_num)
              User_number = next_num
              if(User_number == 6174):
                  print(*num_list, sep = " > ")
                  User_number = n
                  print(User_number,"reaches 6174 via Kaprekar's routine in",(len(num_list)-1),"iterations")
                  break
    

    
kaprekar(User_number)


    



    
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   7.25 Lab: Pig Latin
# Date:         10 / 03 / 2022
# 
#style 

from math import *

words = input("Enter word(s) to convert to Pig Latin: ")  

list = [words]
list = words.split(' ')


vowels = ["a","e","i","o","u", "A", "E", "I","O", "U", "Y", "y"]
new_list = []
for i in range (0,len(list)):
    word = list[i]
    if word[0].lower() in vowels:
        pig_latin = word + "yay"
        new_list.append(pig_latin)
    elif not word[0].lower() in vowels and not word[1].lower() in vowels:
        pig_latin = word[2:]+ word[0] +  word[1]  + "ay"
        new_list.append(pig_latin)
    elif not word[0].lower() in vowels:
        pig_latin = word[1:] + word[0]  + "ay"      
        new_list.append(pig_latin)
print("In Pig Latin,"+ "\""+str(words)+"\""+ " is: ", *new_list, sep = " ", end = " ")



        
    

    
    
    





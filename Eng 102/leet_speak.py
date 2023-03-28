# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   7.26 Lab: Leet speak
# Date:         10 / 03 / 2022
# 
#style 



leet = {"a":"4", "e":"3", "o":"0", "s":"5", "t":"7"}

text = input("Enter some text: ")

listt = text.split(" ")

new_word = ''
new_list = []

for word in listt:
    new_word = word
    for letter in new_word:   
        if letter in leet:
            new_word = new_word.replace(letter, leet[letter])
    new_list.append(new_word)
print("In leet speak,""\""+str(text)+"\"","is:")
print(*new_list, sep = " ")
            



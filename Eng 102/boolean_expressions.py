# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brandon Becerra
#               Samuel Molero
#               Jackson Barge
#               Christian Flewelling
# Section:      506
# Assignment:   4.15 Lab: Boolean Expressions
# Date:         09 16 2022
#
#style
############ Part A ############
def handle_input(s):
  true_strs = {'True', 'T', 't'}
  false_strs = {'False', 'F', 'f'}
  
  s_bool = True
  if s in false_strs:
    s_bool = False
  elif s not in true_strs:
    pass
  return s_bool
a = input("Enter True or False for a: ")
a_bool = handle_input(a)
b = input("Enter True or False for b: ") 
b_bool = handle_input(b)
c = input("Enter True or False for c: ")
c_bool = handle_input(c)

############ Part B ############
check1 = a_bool and b_bool and c_bool
print("a and b and c: ", check1)
check2 = a_bool or b_bool or c_bool
print("a or b or c: ", check2)

############ Part C ############
def fake_xor(a, b):
  return (a and not b) or (not a and b)

def odd_or_even(a, b, c):
   return(a and not b and not c) or (not a and b and not c) or (not a and not b and c) or (a and b and c)
print('XOR: {}'.format(fake_xor(a_bool, b_bool)))
print("Odd number: ",odd_or_even(a_bool,b_bool,c_bool))
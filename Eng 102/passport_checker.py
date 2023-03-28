import re
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brandon Becerra
#               Samuel Molero
#               Jackson Barge
#               Christian Flewelling
# Section:      506
# Assignment:   11.9 LAB: Passport checker Part A
# Date:         11 7 2022

file = input("Enter the name of the file: ")

def parse_passport(passport):
  var_set = set()
  for prop in passport.strip().split(' '):
    name, val = prop.split(':')    
    if name in set(['ecl', 'hgt', 'byr','cid','pid','eyr','iyr']):
      var_set.add(name)
    if len(var_set) == 7:      
      return True
  return False

new_file = open ('valid_passports.txt', 'w')

count_passports = 0
with open(file) as passports:
  current_passport = []
  for line in passports:
    if line == '\n':
      valid = parse_passport(' '.join(current_passport))
      if valid:
        new_file.write(''.join(current_passport))
        count_passports += 1 
      current_passport.clear()
    current_passport.append(line)
    # print(line, end='')
  print(f"There are {count_passports} valid passports")
  

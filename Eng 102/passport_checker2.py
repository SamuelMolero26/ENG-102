# By submitting this assignment, I agree to the following:#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brandon Becerra
#               Samuel Molero
#               Jackson Barge
#               Christian Flewelling
# Section:      506
# Assignment:   11.9 LAB: Passport checker Part A
# Date:         11 7 2022

import re

file = input("Enter the name of the file: ")


def check_height(val):
  return (val[-2:] == 'cm'
          and 150 <= int(val[:-2]) <= 193) or (val[-2:] == 'in'
                                               and 59 <= int(val[:-2]) <= 76)


def check_pid(val):
  return re.match('\d{9}', val)


#comment
def parse_passport(passport):
  var_set = set()
  for prop in passport.strip().split(' '):
    val = prop.split(':')[1].strip()
    name = prop.split(':')[0].strip()
    #print(check_pid(val))
    if name == 'ecl' and val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] or \
    name == 'byr' and 1920 <= int(val) <= 2005 or \
    name == 'iyr' and 2012 <= int(val) <= 2022 or \
    name == 'hgt' and check_height(val) or \
    name == 'eyr' and 2022 <= int(val) <= 2032 or \
    name == 'pid' and check_pid(val) or \
    name == 'cid' and len(str(int(val))) == 3:
      var_set.add(name)
      #print('valid', val, name)
    else:
      pass
      #print('invalid', val, name)

    if len(var_set) == 7:
      return True
  return False


new_file = open('valid_passports2.txt', 'w')

count_passports = 0
with open(file) as passports:
  current_passport = []

  for line in passports:
    if line == '\n':
      valid = parse_passport(' '.join(current_passport))

      if valid:
        #print('should be writing', ''.join(current_passport))
        new_file.write(''.join(current_passport))
        count_passports += 1

      current_passport.clear()

    current_passport.append(line)
    # print(line, end='')
  print(f"There are {count_passports} valid passports")

new_file.close()
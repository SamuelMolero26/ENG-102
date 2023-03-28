#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brandon Becerra
#               Samuel Molero
#               Jackson Barge
#               Christian Flewelling
# Section:      506
# Assignment:   5.3 Lab: Diabetes Risk
# Date:         09 23 2022
import math


# Assuming only valid input is pretty bad practice, even if the input is automated and controlled
# For a class that seeks to teach engineering principles through code, this is a pretty important lost opportunity
# I dont know if this is something yall plan to cover later, so include that in the context of the above comments

# In an ideal world we would throw an error on invalid input...
# converts 'Y|N' string input to bool
def yn_to_bool(s):
  return s.lower() == 'y'

# from Griffin SJ, Little PS, Hales CN, et al., Diabetes risk score: towards earlier detection of Type 2 diabetes in
# general practice, Diabet Metab Res Rev. 2000; 16: 164-71.
def calc_risk(sex, age, BMI, hyper, steroids, smoker, history):
  n = 6.322 + sex - (0.063 * age) - BMI - hyper - steroids - smoker - history
  # print(n)
  # print(steroids)
  # print(history)
  # print(hyper)
  # print(BMI)
  # print(6.322+0-(0.063 * 42)-(-0.218))
  # print(6.322+sex-(0.063 * age)-(smoker))
  return 100.0 / (1 + pow(math.e, n))

# from 'Lap Topic 5 team risk calculation.pdf' in canvas
def diabetes_check(user_sex, user_age, user_BMI, user_hyper, user_steroids, user_cigs, user_cigs_prev, user_diab_fam, user_sibling, user_parent):
    sex = 0.879 if user_sex.lower() == 'f' else 0

    BMI = 2.518 # user_bmi >= 30 since we are not checking for invalid input...
    if user_BMI < 25:
      BMI = 0
    elif user_BMI >= 25 and user_BMI <= 27.49:
      BMI = 0.699
    elif user_BMI >= 27.5 and user_BMI <= 29.99:
      BMI = 1.97


    hyper = 1.222 if user_hyper else 0

    steroids = 2.191 if user_steroids else 0

    smoker = 0.855 if user_cigs else 0

    if user_cigs_prev:
      smoker = -0.218

    history = 0
    if user_sibling or user_parent:
      history = 0.728
    if user_sibling and user_parent:
      history = 0.753

    risk = calc_risk(sex, user_age, BMI, hyper, steroids, smoker, history)
    return risk


user_sex = input("Enter your sex (M/F): ")
user_age = int(input("Enter your age (years): "))
user_BMI = float(input("Enter your BMI: "))
user_hyper = yn_to_bool(input('Are you on medication for hypertension (Y/N)? '))
user_steroids = yn_to_bool(input('Are you on steroids (Y/N)? '))
user_cigs = yn_to_bool(input('Do you smoke cigarettes (Y/N)? '))
user_cigs_prev = False
if not user_cigs:
    user_cigs_prev = yn_to_bool(input('Did you used to smoke (Y/N)? '))
user_diab_fam = yn_to_bool(input('Do you have a family history of diabetes (Y/N)? '))

user_sibling = False
user_parent = False

if user_diab_fam:
  both = yn_to_bool(input('Both parent and sibling (Y/N)? '))
  if both:
      user_sibling = True
      user_parent = True
  else:
      user_sibling = True
      user_parent = False
  # user_sibling = yn_to_bool(input('idk what to put here yet we kinda just have to throw? '))
  # user_parent = yn_to_bool(input('idk what to put here yet we kinda just have to throw? '))


risk = diabetes_check(user_sex, user_age, user_BMI, user_hyper, user_steroids, user_cigs, user_cigs_prev, user_diab_fam, user_sibling, user_parent)

# print to single decimal place
print('Your risk of developing type-2 diabetes is {:.1f}%'.format(risk))

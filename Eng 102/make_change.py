# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brandon Becerra
#               Samuel Molero
#               Jackson Barge
#               Christian Flewelling
# Section:      506
# Assignment:   4.13 Lab: Make Change
# Date:         09 12 2022
#

from math import * 

payment = float(input("How much did you pay? "))
                
cost = float(input("How much did it cost? "))

change = 100 * round((payment - cost), 2)

def change_coin(change, coin_val):
  cnt = int(change // coin_val)
  change = change % coin_val
  return (cnt, change)

coin_vals = {
  'quarter|quarters': 25,
  'dime|dimes': 10,
  'nickel|nickels' : 5,
  'penny|pennies' : 1,
}

print("You received ${:.2f} in change. That is...".format(change / 100))

for name in coin_vals:
  coin_val = coin_vals[name]
  #print(coin_val)
  (cnt, change) = change_coin(change,coin_val)
  final_name = name.split('|')
  if cnt > 1:
    print(str(cnt) + " " + final_name[1])
  elif cnt == 0:
    pass
  else:
    print(str(cnt) + " " + final_name[0])

  
  
  
  
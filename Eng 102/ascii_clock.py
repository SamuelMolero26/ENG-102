# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brandon Becerra
#               Samuel Molero
#               Jackson Barge
#               Christian Flewelling
# Section:      506
# Assignment:   
# Date:         19 October 2022



time = input("Enter the time: ")
print() # zybooks being different than my machine smh
dk = {':':11, '0':10} # 11 because 0-indexed
time_list = [int(dk.get(t, t)) - 1 for t in [*time]]

hours = int(time.split(':')[0])
mins = int(time.split(':')[1])
if hours*100 + mins >= 2400 or mins >= 60:
  print('Error, time is not valid')
  exit(1)

s = """
 1  222 333 4 4 555 666 777 888 999 000   
11    2   3 4 4 5   6     7 8 8 9 9 0 0 : 
 1  222 333 444 555 666   7 888 999 0 0   
 1  2     3   4   5 6 6   7 8 8   9 0 0 : 
111 222 333   4 555 666   7 888 999 000   
"""
s = '\n'.join(s.split('\n')[1:-1]) # remove triple quote lines (first and last)

n_rows = len(s.split('\n'))
n_cols = len(s.split('\n')[0])


# time of 12:34 -> [0, 1, 10, 2, 3] for cols list
def print_cols(s, r, c, cols, width):
  for row in s.split('\n'):
    s_out = ''
    for col in cols:
      # grabbing from width*col (start of the number)
      # to width*col+width (end including space if width is correct)
      s_out += row[width*col:(width*col)+width]
    print(s_out)

print_cols(s, n_rows, n_cols, time_list, 4)
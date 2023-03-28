# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brandon Becerra
#               Samuel Molero
#               Jackson Barge
#               Christian Flewelling
# Section:      506
# Assignment:   Lab 7
# Date:         7 10 2022
#
from enum import Enum
import re
from colorama import Fore

print(Fore.GREEN + "  ▄▀▀▀▀▄        ▄▀▀▀▀▄  ")
print(" █             █      █ ")
print(" █    ▀▄▄      █      █  ") 
print(" █     █ █     ▀▄    ▄▀  ")
print("  ▀▄▄▄▄▀ ▐       ▀▀▀▀   ")
print()

board = [[".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]] 

class Player(Enum):
  WHITE = 'o'
  BLACK = '@'

# oh boy i sure love (global) state
def print_board():
  print('  ', end='')
  for i in range(1, 10):
    print('{} '.format(i), end='')
  print()  

  for i in range(len(board)):
    sub = board[i]
    print(i+1, end=' ')
    print(' '.join(map(str,sub)))

  
player = Player.BLACK

# event loop
stop_cnt = 0
while True:
  print_board()
  
  raw_in = input('Enter in a move for {} in the form \"X Y\": '.format(player.name))

  if raw_in == 'stop':
    stop_cnt += 1
  else:
    stop_cnt = 0

  if stop_cnt == 2:
    break

  if not re.search('\d \d', raw_in):
    print('Invalid move')
    continue # will skip player update
    
  # this is bad obv but idc
  x = int(raw_in.split(' ')[1])
  y = int(raw_in.split(' ')[0])
  
  canplace = (9 >= x >= 1) and (9 >= y >= 1)

  if not canplace:
    print('Invalid move')
    continue # will skip player update
    
  if board[x-1][y-1] != '.':
    print('Invalid move')
    continue # will skip player update

  board[x-1][y-1] = player.value
  
  
  # flip player
  player = Player.WHITE if player == Player.BLACK else Player.BLACK
  
  




print_board()
print("final board")
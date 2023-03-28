# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   10.14 Lab: Guessing Game
# Date:         10 / 24 / 2022
# 
#style 


print("Guess the secret number! Hint: it's an integer between 1 and 100...")
    
def guess_number():
        guess_target = 26
        return guess_target
guess_number()
     
    
    

def game_code():
    target = guess_number()
    repeat = True
    count = 0 
    while repeat: 
        try:
            try:
                guess = int(input("What is your guess? "))
                if guess == target:
                    count += 1
                    print(f"You guessed it! It took you {count} guesses.")
                    break
                elif guess < target:
                    count += 1
                    print("Too low!")
                    repeat = True
                elif guess > target:
                    count += 1 
                    print("Too high!")
                    repeat = True
            except ValueError:
                guess = int(input("Bad input! Try again: "))
                if guess == target:
                    count += 1
                    print(f"You guessed it! It took you {count} guesses.")
                    break
                elif guess < target:
                    count += 1
                    print("Too low!")
                    repeat = True
                elif guess > target:
                    count += 1
                    print("Too high!")
                    repeat = True
        except ValueError:
            try:
                guess = int(input("Bad input! Try again: "))
                if guess == target:
                    count += 1
                    print(f"You guessed it! It took you {count} guesses.")
                    break
                elif guess < target:
                    count += 1
                    print("Too low!")
                    repeat = True
                elif guess > target:
                    count += 1
                    print("Too high!")
                    repeat = True
            except ValueError:
                guess = int(input("Bad input! Try again: "))
                if guess == target:
                    count += 1
                    print(f"You guessed it! It took you {count} guesses.")
                    break
                elif guess < target:
                    count += 1
                    print("Too low!")
                    repeat = True
                elif guess > target:
                    count += 1
                    print("Too high!")
                    repeat = True
                

       

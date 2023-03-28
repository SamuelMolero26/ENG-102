# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:     Samuel Molero
#      
# Section:      506
# Assignment:   11.12 LAB: Counting coins
# Date:         4 November 2022

coins_count = 0 # number of coins 

coins_total = [] #gained or lost

with open('game.txt','r') as game:
    read_file = game.readlines()
    i = 0 
    while i < len(read_file):
        data_collected = read_file[i].split() #split the read_file line into a list
        check = data_collected[0] #checlks for coin or jump 
        value_hold = int(data_collected[1])
        
        if check == "coin":
            coins_count += value_hold
            coins_total.append(value_hold)
            i += 1
        elif check == "jump":
            i += value_hold
        else:
            i += 1 
    game.close()
    
with open('coins.txt','w') as coin:
    for a in coins_total:
        coin.write(str(a) + "\n")
    coin.close()
    
print(f"Total coins collected: {coins_count}")
        
            
        
        
        
        
        
    
        


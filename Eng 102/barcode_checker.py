# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:     Samuel Molero
#      
# Section:      506
# Assignment:   11.11 LAB: Barcode checker
# Date:         4 November 2022


name = input("Enter the name of the file: ")
#barcodes = open(f"{name}","r")



#variables and lists i need
every_other1 = []
every_other2 = []
sum1 = 0
sum2 = 0
full_digits = []
#last_digit = 0
count = 0 

fp = open('valid_barcodes.txt', 'w')

count = 0
with open(f"{name}","r") as barcode:
    for code in barcode:
        full_digits.append(code)
        every_other1.append(int(code[:12:2]))
        every_other2.append(int(code[1::2]))
    for i in range(len(every_other1)):
        output1 = list(map(int, str(every_other1[i])))
        output2 = list(map(int, str(every_other2[i])))
        #print(*output1)
        #print(*output2)
        for s in output1:
            sum1 = sum1 + s
        for s in output2:
            sum2 = sum2 + s
        sum2 *= 3
        total_sum = sum2 + sum1              
        last_digit = (10 - (total_sum % 10 ))
        last = int(full_digits[i]) % 10
        if last == last_digit:
            count += 1
            fp.write(full_digits[i])
fp.close()
print("There are ?? valid barcodes")           
        
             
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            

        
            
            
            
            
                      
            
    

import numpy as np
from matplotlib import pyplot as plt

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   12.17 LAB: Plotting data
# Date:         11 / 15 / 2022
#



data = []
temp = []
wind = []
dates = []
total_w = 0 
min_temp = []
months  = []  

january_temp = []
february_temp = []
march_temp = []
april_temp = []
may_temp = []
june_temp = []
july_temp = []
august_temp = []
sept_temp = []
oct_temp = []
nov_temp = []
decem_temp = []

sum_j = 0
sum_f = 0
sum_m = 0
sum_a = 0
sum_my = 0
sum_jn = 0
sum_jl = 0
sum_ag = 0
sum_sp = 0 
sum_oct = 0
sum_n  = 0 
sum_d = 0 

with open("WeatherDataCLL.csv") as weather:
    
    read_weather = weather.readlines()
    

    for i in read_weather: # read the file 
        new = i.split(",")
        data.append(new)
    for j in data:
        try:
            temp.append(float(j[4]))
            wind.append(float(j[1]))
            min_temp.append(int(j[5]))
            dates.append(j[0])
        except ValueError:
            pass
                 
    #######getting dates######
    for month in data:
        rewrite = month[0].split('/')
        month[0] = rewrite
        if month[0][0] == "1":
            january_temp.append(int(month[3]))
            sum_j = sum(january_temp)
        elif month[0][0] == "2":
            february_temp.append(int(month[3]))
            sum_f = sum(february_temp)
        elif month[0][0] == "3":
            march_temp.append(int(month[3]))
            sum_m = sum(march_temp)
        elif month[0][0] == "4":
            april_temp.append(int(month[3]))
            sum_a = sum(april_temp)
        elif month[0][0] == '5':
            may_temp.append(int(month[3]))
            sum_my = sum(may_temp)
        elif month[0][0] == '6':
            june_temp.append(int(month[3]))
            sum_jn = sum(june_temp)
        elif month[0][0] == '7':
            july_temp.append(int(month[3]))
            sum_jl = sum(july_temp)
        elif month[0][0] == '8':
            august_temp.append(int(month[3]))
            sum_ag = sum(august_temp)
        elif month[0][0] == "9":
            sept_temp.append(int(month[3]))
            sum_sp = sum(sept_temp)
        elif month[0][0] == '10':
            oct_temp.append(int(month[3]))
            sum_oct = sum(oct_temp)
        elif month[0][0] == '11':
            nov_temp.append(int(month[3]))
            sum_n = sum(nov_temp)
        elif month[0][0] == '12':
            decem_temp.append(int(month[3]))
            sum_d = sum(decem_temp)
        

    
    high_j = max(january_temp)
    high_f = max(february_temp)
    high_m = max(march_temp)
    high_a = max(april_temp)
    high_my = max(may_temp)
    high_jn = max(june_temp)
    high_jl = max(july_temp)
    high_ag = max(august_temp)
    high_s = max(sept_temp)
    high_o = max(oct_temp)
    high_n = max(nov_temp) 
    high_d = max(decem_temp)
    
    min_j = min(january_temp)
    min_f = min(february_temp)
    min_m = min(march_temp)
    min_a = min(april_temp)
    min_my = min(may_temp)
    min_jn = min(june_temp)
    min_jl = min(july_temp)
    min_ag = min(august_temp)
    min_s = min(sept_temp)
    min_o = min(oct_temp)
    min_n = min(nov_temp)
    min_d = min(decem_temp)
     
    
 
high_temp = [high_j, high_f, high_m, high_a, high_my, high_jn, high_jl, high_ag, high_s, high_o, high_n, high_d]   
min_temp2 = [min_j,min_f,min_m,min_a,min_my,min_jn,min_jl,min_ag,min_s,min_o,min_n,min_d]
sum_j = int(sum_j/len(january_temp))
sum_f = int(sum_f/len(february_temp))
sum_m = int(sum_m /len(march_temp))
sum_a = int(sum_a/len(april_temp))  
sum_my = int(sum_my/len(may_temp))
sum_jn = int(sum_jn/len(june_temp))
sum_jl = int(sum_jl/len(july_temp))
sum_ag = int(sum_ag/len(august_temp))
sum_sp = int(sum_sp/len(sept_temp))
sum_oct = int(sum_oct/len(oct_temp))
sum_n = int(sum_n/len(nov_temp))
sum_d = int(sum_d/len(decem_temp))
total_temp = [sum_j,sum_f,sum_m,sum_a,sum_my,sum_jn,sum_jl,sum_ag,sum_sp,sum_oct,sum_n,sum_d]
    
    
    
#plot 1 
plt.title('Maximum Temperature and Average Wind Speed')
ax1 = plt.subplot()
plt.xlabel("Dates: ")
plt.ylabel("Maximum Temperature, F")
plt.plot(temp, color = "red" ,label = 'Maximum Temperature')
plt.legend(['Maximum Temperature'], loc = 'lower left' , bbox_to_anchor = (0.005,0.05) )
    
ax2 = ax1.twinx()
plt.ylabel('Average Wind Speed, mph')
plt.plot(wind, color = 'b', label = 'Average Wind Speed') 

plt.legend(['Average Wind Speed'],loc = 'lower left',bbox_to_anchor = (0.005,0.004))
    
plt.show()
    
#plot 2
plt.title('Histogram of average wind speed')
plt.ylabel('Number of days')
bins = np.linspace(0,20,31)
plt.xlabel('Average Wind Speed, mph')
plt.hist(wind,bins, color = "g", edgecolor = 'black',)  # type: ignore
plt.show()
    
    #plot 3
plt.title("Average Wind Speed vs MInimum Temperature")
plt.ylabel('Average Wind Speed, mph')
plt.xlabel("Minimum Temperature, F")
plt.scatter(min_temp,wind, color = "black")
plt.show()
    
x_month = [1,2,3,4,5,6,7,8,9,10,11,12]
    #plot 4 
plt.title("Temperature by Month")
plt.xlabel("Month")
plt.ylabel("Average Temperature, F")
plt.bar(x_month, total_temp, color= "yellow", edgecolor = 'black') 

plt.plot(x_month,high_temp, color = "r")

plt.plot(x_month, min_temp2, color = 'b' )
plt.legend(["High T", 'Low T'], loc = 'upper left')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.yticks([0,20,40,60,80,100])


plt.show()



    
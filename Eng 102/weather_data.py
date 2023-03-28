
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:     Samuel Molero
#      
# Section:      506
# Assignment:   11.13 LAB: Weather data
# Date:         4 November 2022
import statistics

data = []
Max_Temp = 0 
Min_Temp = 0
temp = []
temp2 = []
prec = 0
prec_list = []

with open("WeatherDataCLL.csv") as weather:
     read_weather = weather.readlines()
     for i in read_weather: # read the file 
        new = i.split(",")
        data.append(new)
     
     for a in data: # conver each value to int
        try:
            temp.append(int(a[4]))
        except ValueError: #account for the string, prevent an error 
            pass
     for e in data: # for the min 
         try:
            temp2.append(int(e[5]))
         except ValueError:
            pass
     for s in data:
         try:
             prec += float(s[2]) 
             prec_list.append(float(s[2]))
         except ValueError:
             pass
            
            
Max_Temp = max(temp)
Min_Temp = min(temp2)

Average_prep = float(prec / len(prec_list))

print(f"3-year maximum temperature: {Max_Temp} F")
print(f"3-year minimum temperature: {Min_Temp} F")
print(f"3-year average precipitation: {Average_prep:.3f} inches")
print()
month = input("Please enter a month: ")
year = input("Please enter a year: ")
print()

def User_check (month,year,data):
    Max_td = 0
    temp_date = []
    wind = []
    rain = []
    
    dates = []
    m_value = 0 #value of the month 
    # library to assign a value corresponding to each month
    month_dic = {"January":"1", 
                "February":"2", 
                "March":"3",
                "April":"4",
                "May":"5",
                "June":"6",
                "July":"7", 
                "August":"8",
                "September":"9",
                "October":"10",
                "November":"11",
                "December":"12"}
    
    if month in month_dic:
        m_value = month_dic[month] #set the month to a value that applicable on the file 
    
    
    
    for i in data: # gather the necessary values at the teh given month and year
        if i[0] == "Date":
            pass
        else:
            if m_value in i[0] and year in i[0]:
                rewrite = i[0].split("/")
                i[0] = rewrite 
                if i[0][0] == m_value and i[0][2] == year:
                    temp_date.append(float(i[4]))
                    wind.append(float(i[1]))
                    rain.append(float(i[2]))
    total_w = 0   
    for w in rain:
        if w > 0:
            total_w += 1 
    percent = (total_w / len(wind)) * 100  
    
    
    print(f"For {month} {year}:")
    mean_tp = statistics.mean(temp_date)
    print(f"Mean maximum daily temperature: {mean_tp:.1f} F")
    mean_ws = statistics.mean(wind)
    print(f"Mean daily wind speed: {mean_ws:.2f} mph")
    print(f"Percentage of days with precipitation: {percent:.1f} %")
    
User_check(month,year,data)
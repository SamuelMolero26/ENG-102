# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Samuel Molero
# Section:      536
# Assignment:   1.10 LAB: Howdy World
# Date:         9 / 1 / 2022
#

#1 coordinates
t1_seconds = 12 
x1_point = 8
y1_point = 6
z1_point = 7
#2 coordinates
t2_seconds = 85 
x2_point = -5
y2_point = 30
z2_point = 9

def linear_interpolation(time_seconds,p):
        x_value = (((x2_point - x1_point)/(t2_seconds - t1_seconds)) * (time_seconds - t1_seconds) + x1_point)
        y_value = (((y2_point - y1_point)/(t2_seconds - t1_seconds)) * (time_seconds - t1_seconds) + y1_point)
        z_value =(((z2_point - z1_point)/(t2_seconds - t1_seconds)) * (time_seconds - t1_seconds) + z1_point)
        print("At time " + str(float(time_seconds)) + " seconds:")
        print("x" + str(p) + " = " + str(x_value) + " m")
        print("y" + str(p) + " = " + str(y_value) + " m")
        print("z" + str(p) + " = " + str(z_value) + " m"   )


time_seconds = 30
p = 1
linear_interpolation(time_seconds, p)
print("-----------------------")
time_seconds = 37.5
p = 2
linear_interpolation(time_seconds, p)
print("-----------------------")
time_seconds = 45
p = 3
linear_interpolation(time_seconds, p)
print("-----------------------")
time_seconds = 52.5
p = 4
linear_interpolation(time_seconds, p)
print("-----------------------")
time_seconds = 60
p = 5
linear_interpolation(time_seconds, p)



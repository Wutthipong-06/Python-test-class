from math import pi

print("%d" %100) #decimal
print("%d" %100.11) #decimal with float
print("%f" %-100.111) #decimal with float
print("%.2f" %100.111) #float with 2 decimal places
print("%.4f" %pi) #string with decimal
print("5+4" ,"= %.2f" %(5+4)) #string with calculation


# Using format specifiers to print variables
age = 25
price = 3500
id = 1 

print("My age is %d years and the price is %d bath." %(age, price) + " ID: %d" % id)
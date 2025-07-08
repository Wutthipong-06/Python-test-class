height = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))  

bmi = weight / (height * height)

print("Your BMI is:", format(bmi, '.2f'))
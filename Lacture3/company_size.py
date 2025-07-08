employees = int(input("Enter the number of employees in the company: "))

if employees < 50:
    print("Small business")
elif employees < 250:
    print("Medium-sized business")
elif employees >= 250:
    print("Large business")
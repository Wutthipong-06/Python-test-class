hours_worked = float(input("Enter the number of hours worked: "))
hours_rate = float(input("Enter the hourly rate: "))

if hours_worked <= 40:
    pay = hours_worked * hours_rate
else:
    overtime_hours = hours_worked - 40
    pay = (40 * hours_rate) + (overtime_hours * hours_rate * 1.5)
    
print("The gross pay is: $", pay)
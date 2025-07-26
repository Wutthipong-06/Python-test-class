temp = input("Enter a temperature in Celsius: ")

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
fahrenheit = celsius_to_fahrenheit(float(temp))
print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")
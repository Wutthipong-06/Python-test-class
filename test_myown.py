#โจทย์ Python

#หาค่าเฉลี่ยของตัวเลข 3 ตัว
def average(numbers):
    numbers = sum(numbers)
    avg = numbers / 3
    return avg
print(average([10, 20, 30]))

#ตรวจสอบเลขคู่เลขคี่
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(7))

#แปลงองศาเซลเซียสเป็นฟาเรนไฮต์
def celsius_to_fahrenheit(celsius):
    input_temp = float(input("Enter temperature in Celsius:"))
    fahrenheit = (input_temp * 9/5) + 32
    return fahrenheit
print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(0)}")

# หาผลรวมของเลขตั้งแต่ 1 ถึง n
def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print(f"Sum of numbers from 1 to 5: {sum_numbers(10)}")

# เช็คว่าตัวอักษรเป็นสระหรือไม่
def is_vowel(char):
    vowels = 'aeiouAEIOU'
    if char in vowels:
        return True
    else:
        return False
print(is_vowel('y'))


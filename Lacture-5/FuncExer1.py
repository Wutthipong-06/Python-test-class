def is_armstrong(number):
    digits = str(number) #แปลงตัวเลข ให้เป็น str
    power = len(digits) #หาความยาวของ str เริ่มจาก 1
    total = sum(int(digit) ** power for digit in digits)
    return total == number

print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))
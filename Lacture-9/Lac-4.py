try:
    value = int(input('Enter of num: '))
    re = 10 / value
except ZeroDivisionError:
    print('Error: Division by zero is not allowed.')
else:
    print(f'result is {re}')
print('End of program')
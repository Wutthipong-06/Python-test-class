try:
    value = int(input('Enter a number: '))
    re = 10 / value
except ValueError:
    print('Invalid input: Please enter a number.')
except ZeroDivisionError:
    print('Cannot divide by Zero!!')
print('End of program')
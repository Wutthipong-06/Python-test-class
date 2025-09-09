try:
    numer = float(input('Enter the numerator: '))
    deno = float(input('Enter the denominator: '))

    result = numer / deno
    print(f'The result is: {result:.2f}')

except ZeroDivisionError:
    print(f'Error: You cannot divide bt zero.')

except ValueError:
    print('Error: invalid input. Please enter numeric value.')

finally:
    print('Excution completed, whether as exception occurred ar not.')
print('End of program.')
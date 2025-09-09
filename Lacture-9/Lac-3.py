try:
    value = int(input('Enter a number: '))
    re = 10 / value
except Exception as e:
    print(f'An error occurred: {e}')
print(f'End of program re is a {re}')

name = input('what is your name? ')
age = input('what is your age? ')
income = float(input('what is your income? '))

print('here is data you entered: ')
print('name: ' + name)
print('age: ' + age)
print('income: ', format(income, '12,.2f') + " Bath") # format income with commas and 2 decimal places
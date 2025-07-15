keep_going = 'y'

while keep_going == 'y':
    sales = float(input('Enter the sales amount: '))
    com_rate = float(input('Enter the commission rate (as a decimal): '))
    commission = sales * com_rate
    print(f'The commission is: ${commission:.2f}')
    keep_going = input('Do you want to calculate another commission? (y/n): ')
    
    if keep_going.lower() != 'y':
        print('Thank you for using the commission calculator!')
        break
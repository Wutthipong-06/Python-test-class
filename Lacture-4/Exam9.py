keep_going = 'y'

while keep_going == 'y':
    sales = float(input('Enter the sales amount: '))
    com_rate = sales * 2.5
    print(f'The commission is: ${com_rate:.2f}')
    keep_going = input('Do you want to calculate another commission? (y/n): ')
    
    if keep_going.lower() != 'y':
        print('Thank you for using the commission calculator!')
        break
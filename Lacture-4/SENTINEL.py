keep_going = 'y'

while keep_going.lower() == 'y':
    cost = float(input('Enter the cost of the item: '))
    retail_price = cost * 2.5
    print(f'The retail price is: ${retail_price:.2f}')
    keep_going = input('Do you want to calculate another retail price? (y/n): ')
    if keep_going.lower() != 'y':
        print('Thank you for using the retail price calculator!')
        break
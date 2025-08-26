num_emp = int(input('How many employee record do you want to create? '))

with open('employees.txt', 'w') as emp_file:
    for count in range(1, num_emp + 1):
        print('Enter data for employee #' , count, sep='')
        name = input('Name: ')
        id_num = input('ID number: ')
        dept = input('Department: ')

        emp_file.write('Name :' + name + '\n')
        emp_file.write('ID :' + id_num + '\n')
        emp_file.write('Dept :' + dept +'\n')
        print()
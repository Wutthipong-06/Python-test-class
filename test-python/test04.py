def calculate_sum_and_average():
    counter = 0
    sum = 0
    for i in range(1, 6):
        num = float(input(f"Enter number {counter + 1} : "))
        counter += 1
        sum += num
    average = sum / 5
    print(f'''sum : {sum:.2f}
average : {average:.2f}''')

calculate_sum_and_average()

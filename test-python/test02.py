def find_multiples_of_three_and_four():
    return [i for i in range(10, 25) if i % 3 == 0 and i % 4 == 0]
result = find_multiples_of_three_and_four()
print(result)
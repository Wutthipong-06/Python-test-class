def find_multiples_of_three():
    return [i for i in range(1, 1000) if i % 3 == 0]
result = find_multiples_of_three()
print(result)
def find_non_multiples():
    return [i for i in range(10, 25) 
            if i % 3 != 0 and i % 4 != 0 and i % 5 != 0
            ]
result = find_non_multiples()
print(result)
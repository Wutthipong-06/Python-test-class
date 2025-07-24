aggregated = 0
numbers = [39, 89, 72, 27, 15]

for number in numbers:
    if number > 72:
        print("That's a big number:", number)
    aggregated += number

print("Total sum:", aggregated)
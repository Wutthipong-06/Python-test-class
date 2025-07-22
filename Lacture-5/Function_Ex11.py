def calculate_state(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimun = min(numbers)
    return total_sum, average, maximum, minimun

numbers = [5, 10, 15, 20, 25]
total, avg, max_num, min_num = calculate_state(numbers)

print(f"Total sum : {total}")
print(f"Average: {avg}")
print(f"Maximum: {max_num}")
print(f"Minimun: {min_num}")
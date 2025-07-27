scores = int(input("Enter the number of scores: "))
total = 0
for i in range(scores):
    score = float(input(f"Enter score {i + 1}: "))
    total += score
average = total / scores
if average > 95:
    print("Congratulations!")
print(f"The average score is: {average:.2f}")
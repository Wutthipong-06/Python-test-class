score = float(input("Enter the score for test 1: "))
score = float(input("Enter the score for test 3: "))
score = float(input("Enter the score for test 3: "))

average = (score + score + score) / 3
if average >= 95:
    print(("Your  average is: ") + str(average))
    print("Congratulations! You have passed the Exam.")
else:
    print(average)
    print("You need to improve your score.")
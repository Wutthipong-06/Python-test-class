test = input("Enter a string: ")
vowels = "aeiou"
count = 0

for char in test:
    if char.lower() in vowels:
        count += 1
        print(f"Vowel found: {char}")
        print(f"Total vowels found: {count}")
    else:
        print()
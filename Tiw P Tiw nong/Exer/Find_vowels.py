test = input("Enter a string: ")
vowels = "aeiou"
count = 0

# เอาไว้เช็คตัวอักษรพิเศษ
has_special_chars = any(not c.isalnum() and not c.isspace() for c in test)

# ถ้ามีตัวอักษรพิเศษให้แสดงผล count = 0
if has_special_chars:
    print(f"Total vowels found: 0 (contains special characters)")
else:
    # นับ vowels ตามปกติ
    for char in test:
        if char.lower() in vowels and char.isalpha():
            count += 1
            # print(f"Vowel found: {char}")
    print(f"Total vowels found: {count}")
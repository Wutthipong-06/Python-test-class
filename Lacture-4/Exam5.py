text = input("Enter a string: ")

modified_text = " "

vowels = "aeiouAEIOU"

for char in text:
    upper_char = char.upper()
    if upper_char in vowels:
            modified_text += "*"
    else:
            modified_text += upper_char
            
print(modified_text)
# This code replaces vowels in the input string with '*' and converts all characters to uppercase.
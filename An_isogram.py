def is_isogram(string):
    string = string.lower()
    seen = set()
    for char in string:
        if char in seen:
            return False
        seen.add(char)
    return True

print(is_isogram("Dermatoglyphics"))  # True
print(is_isogram("aba"))              # False
print(is_isogram("moOse"))            # False
print(is_isogram(""))                 # True
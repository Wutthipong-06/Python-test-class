inchar = input("Enter a character: ")
if inchar >= 'A' and inchar <= 'Z':
    print("Uppercase letter" , inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("Lowercase letter" , inchar)
elif inchar >= '0' and inchar <= '9':
    print("You in put number" , inchar)
else:
    print("It's not a letter or number" , inchar)
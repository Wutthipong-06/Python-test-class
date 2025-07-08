a = [1, 2, 3]
b = a

c = [1, 2, 3]
d = [1, 2, 3]

print(a is b)  # True, because b is a reference to the same list as a
print(a is c)  # False, because c and d are two different lists with the
print(c is d)  # False, because c and d are two different lists with the same content


print(a == b)  # True, because they have the same content
print(c == d)  # True, because they have the same content
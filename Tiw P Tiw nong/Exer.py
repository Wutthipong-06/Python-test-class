num = [1,2,3,4,5,1,2,3]
new = []

for i in num:
    if i not in new:
        new.append(i)
print(new)
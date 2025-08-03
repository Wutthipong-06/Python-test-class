n = input()
s = ''
for i in n:
    s.append(n)
    for j in s:
        if s not in n:
            print('False')
        else:
            print("true")
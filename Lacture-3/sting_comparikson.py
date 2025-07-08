string = "Mary"
string2 = "Mark"

if string == string2:
    print(f'"{string}" and "{string2}" are equal.')
else:
    print(f'"{string}" and "{string2}" are not equal.')

if string < string2:
    print(f'"{string}" come before "{string2}" in lexicographical order.')
elif string > string2:
    print(f'"{string}" come after "{string2}" in lexicographical order.')
    #.lower() method to ignore case
if string.lower() == string2.lower():
    print(f'"{string}" and "{string2}" are equal when case is ignored.')
else:
    print(f'"{string}" and "{string2}" are not equal when case is ignored.')
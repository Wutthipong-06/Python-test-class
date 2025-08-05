phonebook = {'Wutthipong': '1234', 'Pong': '5678', 'Nong': '9012'}

print(phonebook)

print(phonebook['Wutthipong'])
print(phonebook['Pong'])
print(phonebook['Nong'])

key = 'pluto'
if key in phonebook:
    print(phonebook[key])
else:
    print(key + 'not in phonebook')

phonebook['Simpson'] = '7766-788'
phonebook['Pluto'] = '777-444'
phonebook['Micky'] = '777-2122'
print(phonebook)

del phonebook['Simpson']
print(phonebook)
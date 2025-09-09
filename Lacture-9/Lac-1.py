filename = input('enter a filename ')
try:
    infile = open(filename, 'r')
    content = infile.read()
    print(content)
    infile.close()
except IOError:
    print('An error occured trying to read')
    print('the file', filename)
print('End of program')
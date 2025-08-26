def exam():
    with open('example_w+.txt', 'w+') as file:
        file.write('This is the first line in the file. \n')
        file.write('This is the second line in the file.\n')

        file.seek(0)
        content = file.read()
        print(f'Content of the file: {content}')
exam()
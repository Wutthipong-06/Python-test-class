def main():
    in_file = open('philosopher.txt', 'r')
    file_content = in_file.read()
    in_file.close()
    print(file_content)
main()
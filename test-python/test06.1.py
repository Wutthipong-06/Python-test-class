def folk_69(n):
    for i in range(1, 101):
        if n % i == 0:
            print("is not prime")
        else:
            print("is prime")
folk_69(20)
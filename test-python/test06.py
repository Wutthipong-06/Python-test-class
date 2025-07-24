def check_prime(n):
    if n % 2 == 0:
        print("not prime")
    
    elif n % 3 == 0:
        print("not prime")

    elif n % 7 == 0:
        print("not prime")
    
    elif n % 11 == 0:
        print("not prime")
    
    elif n % 13 == 0:
        print("not prime")
    else:
        print("prime")

    
    #check_prime(104)


def is_prime(n):
    return "is prime" if n > 1 and all(n % i for i in range (2,int(n**0.5)+1)) else " not prime " ;

print(is_prime(int(input())))
print( "i oof kai")

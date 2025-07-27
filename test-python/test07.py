import math

def is_prime(n: int) -> bool:
    if n <= 1: 
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_numbers_in_range(start: int, end: int) -> tuple:
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    total = sum(primes)
    return (primes, total)
print(prime_numbers_in_range(10, 20))
# Output: ([11, 13, 17, 19], 60)          cv
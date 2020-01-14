import sys
import math


def isPrime(num):
    ceiling = int(math.sqrt(num)) + 1
    for i in range(2, ceiling):
        if num % i == 0:
            print("Not a prime number")
            return False
    print("Prime found!")
    return True


# isPrime(int(sys.argv[1]))

def sieve(num):
    composites = set()
    primes = []
    for i in range(2, num + 1):
        if i not in composites:
            primes.append(i)
            base = i * 2
            while base <= num:
                composites.add(base)
                base += i
    return composites


print(sieve(120))

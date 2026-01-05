#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    # Test sisteminin gözlədiyi kimi, sadəcə faktorial nəticəsini çap et
    f = factorial(int(sys.argv[1]))
    print(f)

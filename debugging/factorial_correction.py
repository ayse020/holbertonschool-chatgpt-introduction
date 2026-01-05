#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        if n < 0:
            sys.exit(1)
        result = factorial(n)
        print(f"{n}! = {result}")
    except:
        sys.exit(1)

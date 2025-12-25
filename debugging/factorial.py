#!/usr/bin/python3
"""
Factorial Calculator - Task 4: Documentation

DESCRIPTION:
    This script calculates the factorial of a non-negative integer.
    Factorial (denoted as n!) is the product of all positive integers
    from 1 to n. By definition, 0! = 1.

MATHEMATICAL DEFINITION:
    For any integer n ≥ 0:
        n! = n × (n-1) × (n-2) × ... × 2 × 1
    Special Cases:
        0! = 1
        1! = 1

COMMAND-LINE USAGE:
    ./factorial.py <number>

EXAMPLES:
    $ ./factorial.py 5
    120
    $ ./factorial.py 0
    1
    $ ./factorial.py 3
    6

ERROR HANDLING:
    - Validates that exactly one argument is provided
    - Ensures the argument is a valid integer
    - Checks that the number is non-negative
    - Provides helpful error messages for invalid input
"""

import sys


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    This function uses an iterative approach with a while loop
    to compute the factorial. The implementation is optimized
    for clarity and handles the edge case of n = 0 correctly.
    
    PARAMETERS:
        n (int): The non-negative integer whose factorial is to be computed.
                 Must satisfy: n ≥ 0
    
    RETURNS:
        int: The factorial of n (n!)
    
    RAISES:
        ValueError: If n is negative (factorial is undefined for negative numbers)
    
    TIME COMPLEXITY: O(n)
    SPACE COMPLEXITY: O(1)
    
    EXAMPLES:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
        >>> factorial(1)
        1
    
    IMPLEMENTATION DETAILS:
        1. Validates input is non-negative
        2. Initializes result to 1 (covers 0! and 1!)
        3. Uses while loop for iterative calculation
        4. Critical fix: includes 'n -= 1' to avoid infinite loop
    """
    # Validate input: factorial is undefined for negative numbers
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Initialize result to 1 (handles 0! = 1 and 1! = 1)
    result = 1
    
    # Iterative factorial calculation
    # Multiply result by n, then decrement n, repeat until n ≤ 1
    while n > 1:
        result *= n      # Multiply current result by n
        n -= 1           # Decrement n (CRITICAL FIX from Task 0)
    
    return result


def main() -> None:
    """
    Main function to handle command-line execution.
    
    RESPONSIBILITIES:
        1. Parse command-line arguments
        2. Validate input format and value
        3. Handle errors gracefully with informative messages
        4. Execute factorial calculation
        5. Display results to user
    
    EXIT CODES:
        0: Success
        1: Invalid input or arguments
    """
    # Check if exactly one command-line argument is provided
    if len(sys.argv) != 2:
        print("ERROR: Invalid number of arguments.", file=sys.stderr)
        print(f"USAGE: {sys.argv[0]} <number>", file=sys.stderr)
        print(f"EXAMPLE: {sys.argv[0]} 5", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Convert input string to integer
        input_number = int(sys.argv[1])
        
        # Calculate factorial
        result = factorial(input_number)
        
        # Display the result
        print(f"{input_number}! = {result}")
        
    except ValueError as e:
        # Handle invalid input (non-integer or negative number)
        print(f"ERROR: {e}", file=sys.stderr)
        print("Please provide a valid non-negative integer.", file=sys.stderr)
        sys.exit(1)


# Standard Python idiom: execute main() only when script is run directly
if __name__ == "__main__":
    main()

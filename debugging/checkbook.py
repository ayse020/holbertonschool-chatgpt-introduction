#!/usr/bin/python3
"""
Checkbook Program - Task 5: Error Handling

DESCRIPTION:
    A simple banking application that allows users to manage their
    checkbook balance with deposit, withdrawal, and balance checking
    functionality. Includes comprehensive error handling for all
    user inputs.

FEATURES:
    - Deposit money into account
    - Withdraw money from account (with overdraft protection)
    - Check current balance
    - Exit program gracefully

ERROR HANDLING IMPLEMENTED:
    1. Invalid menu choices (non-numeric or out of range)
    2. Non-numeric amounts for deposits/withdrawals
    3. Negative amounts
    4. Withdrawals exceeding available balance
    5. Keyboard interrupts (Ctrl+C)
    6. General unexpected errors
"""

import sys


def display_menu() -> None:
    """Display the main menu options to the user."""
    print("\n" + "=" * 40)
    print("        CHECKBOOK PROGRAM")
    print("=" * 40)
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit Program")
    print("=" * 40)


def get_numeric_input(prompt: str) -> float:
    """
    Get a valid numeric input from the user with error handling.
    
    This function repeatedly prompts the user until a valid
    positive number is entered.
    
    PARAMETERS:
        prompt (str): The message to display when asking for input
    
    RETURNS:
        float: A validated positive number
    
    ERROR HANDLING:
        - Non-numeric input (e.g., "abc", "12.34.56")
        - Negative numbers
        - Empty input
    """
    while True:
        try:
            user_input = input(prompt).strip()
            
            # Check for empty input
            if not user_input:
                print("ERROR: Input cannot be empty. Please enter a number.")
                continue
            
            # Convert to float with validation
            amount = float(user_input)
            
            # Check for negative amount
            if amount < 0:
                print("ERROR: Amount cannot be negative. Please enter a positive number.")
                continue
            
            return amount
            
        except ValueError:
            print(f"ERROR: '{user_input}' is not a valid number. Please enter a numeric value (e.g., 100.50).")
        except KeyboardInterrupt:
            print("\n\nInput cancelled by user.")
            raise
        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.")


def checkbook_program() -> None:
    """
    Main checkbook program loop with comprehensive error handling.
    
    This function manages the main program flow, including:
    - Menu display and selection
    - Balance tracking
    - Transaction processing
    - Error recovery
    """
    balance = 0.0
    transactions = []
    
    print("Welcome to the Checkbook Program!")
    print(f"Initial balance: ${balance:.2f}")
    
    while True:
        display_menu()
        
        try:
            # Get menu choice with error handling
            choice_input = input("Enter your choice (1-4): ").strip()
            
            # Validate menu choice
            if choice_input not in ["1", "2", "3", "4"]:
                print(f"ERROR: '{choice_input}' is not a valid choice. Please enter 1, 2, 3, or 4.")
                continue
            
            choice = int(choice_input)
            
            if choice == 1:  # Deposit
                amount = get_numeric_input("Enter deposit amount: $")
                balance += amount
                transactions.append(("DEPOSIT", amount))
                print(f"✓ Successfully deposited: ${amount:.2f}")
                print(f"✓ New balance: ${balance:.2f}")
                
            elif choice == 2:  # Withdraw
                amount = get_numeric_input("Enter withdrawal amount: $")
                
                # Check for sufficient funds
                if amount > balance:
                    print(f"✗ ERROR: Insufficient funds. Current balance: ${balance:.2f}")
                    print(f"  Withdrawal attempted: ${amount:.2f}")
                    print(f"  Shortfall: ${(amount - balance):.2f}")
                else:
                    balance -= amount
                    transactions.append(("WITHDRAWAL", amount))
                    print(f"✓ Successfully withdrew: ${amount:.2f}")
                    print(f"✓ New balance: ${balance:.2f}")
                    
            elif choice == 3:  # Check Balance
                print(f"\nCurrent Balance: ${balance:.2f}")
                if transactions:
                    print(f"Number of transactions: {len(transactions)}")
                else:
                    print("No transactions yet.")
                    
            elif choice == 4:  # Exit
                print("\n" + "=" * 40)
                print("PROGRAM SUMMARY:")
                print(f"Final balance: ${balance:.2f}")
                print(f"Total transactions: {len(transactions)}")
                print("Thank you for using the Checkbook Program!")
                print("=" * 40)
                break
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user (Ctrl+C).")
            print(f"Current balance preserved: ${balance:.2f}")
            break
        except Exception as e:
            print(f"\nUnexpected error occurred: {e}")
            print("The program will continue. Please try again.")


def main() -> int:
    """
    Main entry point with top-level error handling.
    
    RETURNS:
        int: Exit code (0 for success, 1 for error)
    """
    try:
        checkbook_program()
        return 0
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
        return 0
    except Exception as e:
        print(f"\nFATAL ERROR: {e}")
        print("The checkbook program has encountered a critical error and must close.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

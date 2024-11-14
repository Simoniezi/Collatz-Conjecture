"""
This is a simple algorhithm to calculate the famous Collatz conjecture: 3x+1
If the number is odd, you multiply it by 3 and add 1.
If the number is even, you divide by 2.
The process continues until reaching 1.
This version also allows the user to specify an exponent for the starting number,
handles very large numbers, and includes a step limit to prevent infinite loops.
"""

from colorama import Fore, Style, init
init(autoreset=True) # Initialises colorama to reset colour after each print

import sys
sys.set_int_max_str_digits(0)

def collatz_conjecture(max_steps=1000000):
    print(Fore.CYAN + Style.BRIGHT + "Welcome to the Collatz Conjecture Program!")
    print(Fore.CYAN + "-" * 40)

    while True: # Asks the user for a base integer and an exponent integer for the sequence
        try:
            base = int(input(Fore.YELLOW + "Enter a base number greater than 1: "))
            if base <= 1:
                print(Fore.RED + "Please enter a base number greater than 1.")
                continue
            exponent = int(input(Fore.YELLOW + "Enter an exponent (enter 1 if you don't want to raise it): "))
            num = base ** exponent
            break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter an integers for both the base and the exponent.")

    print(Fore.CYAN + "-" * 40)
    print(Fore.MAGENTA + f"Starting number ({base}^{exponent}) is: {num}")
    print(Fore.CYAN + "-" * 40)

    num_list = [] # Initialises the sequence list
    calculation_count = 0 # Initialises counter for the number of calculations
    highest_number = num # Tracks the highest number reached
    num_of_odds = 0
    num_of_evens = 0

    while num != 1 and calculation_count < max_steps: #Checks that the integer is not 1
        num_list.append(num)

        # Checks whether the number is even or odd by finding the remainder through the modulus of 2
        if num % 2 == 0: 
            print(Fore.GREEN + f"[Even] {num_list[-1]} → " + Fore.YELLOW + f"{num // 2}")
            num //= 2
            num_of_evens += 1
        else:
            print(Fore.RED + f"[Odd] {num_list[-1]} → " + Fore.YELLOW + f"{num * 3 + 1}")
            num = num * 3 + 1 
            num_of_odds += 1

        calculation_count += 1 # Increments the calculation count for each operation
        highest_number = max(highest_number, num) # Updates highest number if needed

    # Handles cases where the step limit is reached
    if num == 1:
        num_list.append(1) # Adding the last number, 1
        print(Fore.CYAN + "\nReached 1; end of Collatz sequence.")
    else:
        print(Fore.RED + "\nReached the maximum step limit; stopping sequence.")
    

    # Display results    
    print(Fore.CYAN + "-" * 40)
    print(Fore.BLUE + Style.BRIGHT + "Summary of Results".center(38))
    print(Fore.CYAN + "-" * 40)
    print(Fore.MAGENTA + "Sequence Length: " + Fore.YELLOW + Style.BRIGHT + f"{len(num_list)}")
    print(Fore.MAGENTA + "Total calculations performed: " + Fore.YELLOW + Style.BRIGHT + f"{calculation_count}")
    print(Fore.MAGENTA + "The highest number reached in the sequence was: " + Fore.YELLOW + Style.BRIGHT + f"{highest_number}")
    print(Fore.MAGENTA + "Your starting number was: " + Fore.YELLOW + Style.BRIGHT + f"({base}^{exponent}) = {base ** exponent}")
    print(Fore.MAGENTA + "Amount of " + Fore.RED + "odds: " + Fore.YELLOW + Style.BRIGHT + f"{num_of_odds}")
    print(Fore.MAGENTA + "Amount of " + Fore.GREEN + "evens: " + Fore.YELLOW + Style.BRIGHT + f"{num_of_evens}")
    print(Fore.CYAN + "-" * 40)

    while True:
        if input(Fore.YELLOW + "\nWould you like the Full Sequence? (Y/N): ").strip().upper() != 'Y':
            break
        else:
            print(Fore.MAGENTA + "Full Sequence:")
            print(Fore.MAGENTA + Style.BRIGHT + ", ".join(Fore.YELLOW + Style.BRIGHT + f"{n}" for n in num_list))
            break

while True: # Checks whether user wants to continue
    collatz_conjecture()
    if input(Fore.YELLOW + "\nWould you like to repeat the program? (Y/N): ").strip().upper() != 'Y':
        print(Fore.CYAN + "Goodbye! Thank you for using the Collatz Conjecture Program.")
        break
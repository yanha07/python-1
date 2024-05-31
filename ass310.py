'''Created by Yanha Loharwad
Python program to reverse a positive numbrer.'''
n = input("Enter a positive integer: ")
if n.isdigit():
    n = int(n)
    if n <= 0:
        print("Error: Input must be a positive integer.")
    else:
        reversed_n = int(str(n)[::-1])
        print("Reversed number:", reversed_n)
else:
    print("Error: Invalid input. Please enter a valid positive integer.")




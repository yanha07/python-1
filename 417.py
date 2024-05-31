'''Created by Yanha Loharwad.
Python program to sum the list.'''
number = input("Enter a number: ")
digits = [int(digit) for digit in number]
total_sum = sum(digits)
print("Sum of digits in the number:", total_sum)

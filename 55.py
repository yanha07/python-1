'''Created by YAnha Loharwad
Python program to check if the number is palindrome'''
def is_palindrome(number):
    num_str = str(number)
    reversed_str = num_str[::-1]
    return num_str == reversed_str
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

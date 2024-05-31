'''Created by Yanha Loharwad.
Python program to find greatest number in list.'''
# Initialize an empty list to store numbers
numbers = []

# Take input from the user for 5 numbers
for i in range(5):
    num = float(input("Enter number {} ".format(i+1)))
    numbers.append(num)

# Find the largest number in the list
largest = max(numbers)

# Print the largest number
print("The largest number is:", largest)

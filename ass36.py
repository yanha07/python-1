'''Created by Yanha Loharwad
Python program to change the values of 5th and 6th element'''
# Original tuple
numbers_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# Convert tuple to list
numbers_list = list(numbers_tuple)

# Make changes to the 5th and 6th elements
numbers_list[4] = 55  # Changing the 5th element to 55
numbers_list[5] = 65  # Changing the 6th element to 65

# Convert the list back to a tuple
numbers_tuple = tuple(numbers_list)

print(numbers_tuple)  
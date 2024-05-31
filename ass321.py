'''Created by Yanha Loharwad.
Find the output.'''
list1 = [2, 3, [4, 5]]
list2 = list1.copy()  # Shallow copy

# Modify the first element of list2
list2[0] = 88

# Print list1
print("Original list1:", list1)

# Print list2
print("Modified list2:", list2)



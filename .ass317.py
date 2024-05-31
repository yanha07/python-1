'''Created by Yanha Loharwad
Python program to multiply two lists.'''
A = [1, 4, 5, 7, 3]
B = [2, 0, 8, -3]

result = [a * b for a, b in zip(A, B)]

print("Multiplication result:", result)

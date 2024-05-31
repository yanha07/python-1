'''Created by Yanha Loharwad.
Python program to print multiplication table.'''
a = int(input("enter a number: "))
print("Multiplication table of", a, "is:")
for i in range(0, 11):
    print(a, "X", i, "is:", a * i)

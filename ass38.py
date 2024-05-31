'''Created by Yanha Loharwad.
Python program to print Pascal's triangle.'''
from math import factorial
n = 5
for i in range(n):
    for j in range(n-i+1):
        # for space 
        print(end=" ")
    for j in range(i+1):
        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    # for new line
    print()

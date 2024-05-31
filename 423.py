'''Created by Yanha Loharwad
Python program to multiply elements in dictionary.'''
d = {'A':57, 'B': 100, 'C': 84}
mul=1
for i in d:
    mul=mul*d[i]
print("Multiplication of all values of dictionary is : ",mul)

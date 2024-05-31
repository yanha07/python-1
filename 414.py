'''Created by Yanha Loharwad.
Python program to change list values of tuple.'''
t = (1,2, ['a', 'b', 1.2], 3,4)
s=list(t)
s[2][0]=100
t=tuple(s)
print(t)

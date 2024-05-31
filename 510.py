'''Created by Yanha Loharwad
Python program to retrieve only negative numbers'''
lst = [-1,-2,-3,3,4,5,-6]
neg = []
for num in lst:
    if num < 0:
        neg.append(num)
print("Negative numbers:", neg)

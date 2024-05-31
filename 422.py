'''Created by Yanha Loharwad.'''
def findSum(dict1):
    sum = 0
    for i in dict1:
        sum += dict1[i]
    return sum

marks = {'Maths': 75, 'Chemistry': 87, 'Physics': 77, 'Biology': 92, 'English':96}
print("Sum of marks:", findSum(marks))


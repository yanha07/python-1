'''Created by Yanha Loharwad
Python program to find econd largest number in a list'''
lst = [10, 5, 8, 20, 15]
sorted_list = sorted(lst, reverse=True)
result=sorted_list[1]
print("The second largest number in the list is:", result)

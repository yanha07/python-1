'''Created by Yanha Loharwad
Python program to retrieve the second element from the list and convert list into tuple.
'''
lis = [[10, 20, 'a'], [30, 'b', 40], ['x', 50]]
second_element = lis[1]
print("Second element from the list:", second_element)
lis_as_tuple = tuple(map(tuple, lis))
print("List converted to tuple:", lis_as_tuple)

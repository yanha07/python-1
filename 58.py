# Created by Yanha Loharwad
# Python program to search for an element in a list

def search(lst, element):
    for idx, e in enumerate(lst):
        if e == element:
            return idx 
    return -1  
elements = [10, 20, 30, 40, 50]
element = int(input("Enter element to search for: "))
index = search(elements, element)
if index != -1:
    print(f"{element} found at index {index}")
else:
    print(f"{element} not found in the list")

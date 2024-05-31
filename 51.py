'''Created by Yanha Loharwad
Oython program to find the frequency'''
list = [1, 2, 1, 2, 4, 2, 5, 7, 5, 8, 6, 9, 5, 5, 4, 1, 26, 5, 21, 6, 5, 21, 6, 5, 2, 1, 7, 41, 3, 6, 25, 74]
num = int(input("Enter the number to find its frequency: "))
frequency = 0
for item in list:
        if item == num:
            frequency += 1
print(f"The frequency of {num} in the list is: {frequency}")

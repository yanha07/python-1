'''Created by Yanha Loharwad.
Python program to count the number of even and odd numbers from a given range of numbers.'''
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

even_count = 0
odd_count = 0

for num in range(start, end + 1):
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

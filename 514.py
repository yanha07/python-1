'''Created by Yanha Loharwad
Python program to print fibonacci series'''
def fib(n):
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series

num = int(input("Enter the number of terms: "))
fib_series = fib(num)
print("Fibonacci series:", fib_series)

'''Created by Yanha Loharwad
Python program to do Assertion handling'''
while True:
    try:
        number = float(input("Enter a number greater than zero: "))
        assert number > 0, "Number must be greater than zero"
        break  
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except AssertionError as e:
        print(e)

print("You entered:", number)

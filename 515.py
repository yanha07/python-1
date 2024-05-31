'''Created by Yanha Loharwad.
Python program to find cosine value'''
import math
def cos_angle(angle_degrees, terms=10):
    angle_radians = math.radians(angle_degrees)
    cos_value = 0
    for n in range(terms):
        term = ((-1) ** n) * (angle_radians ** (2 * n)) / math.factorial(2 * n)
        cos_value += term
    return cos_value

angle = float(input("Enter the angle in degrees: "))
cosine_value = cos_angle(angle)
print("Cosine of", angle, "degrees is approximately:", cosine_value)

'''Created by Yanha Loharwad
Python program to find the grade'''

def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'E'

marks = []
avg = 0

for i in range(5):
    subject_marks = float(input("Enter marks of the subject: "))
    marks.append(subject_marks)

avg = sum(marks) / 5
grade = calculate_grade(avg)
print("Grade:", grade)

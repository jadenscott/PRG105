"""This program will ask the user a series of questions that will determine whether he is eligible for financial aid
or not"""

# Variables are declared here, assumes student qualifies for financial aid
student_qualifies = True
student_status = input("Are you a new or returning student? (enter n or r): ")
gpa = float(input("What is your current GPA?: "))
record = input("Have you ever been convicted of a drug felony? (enter y or n): ")
credit_hours = int(input("How many credit hours are you enrolled for next semester?: "))
income = int(input("What is your gross annual income rounded to the nearest dollar? (do not use commas): "))

# Tests if the user cannot receive financial aid
if student_status == "r" and gpa < 3.200:
    student_qualifies = False
    if record == "y":
        student_qualifies = False
        if credit_hours < 6:
            student_qualifies = False
            if income >= 50000:
                student_qualifies = False

# Determines whether the user can receive financial aid or not depending on the value of student_qualifies
if student_qualifies is False:
    print("You are not eligible for financial aid.")
else:
    print("You are eligible for financial aid.")

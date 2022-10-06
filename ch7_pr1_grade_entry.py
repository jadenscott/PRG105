"""
This program gets an amount of students from the user then collects each student's name and final letter grade and
writes that information to a text file.
"""


def main():
    # creates two-dimensional list
    students_list = []

    # gets the amount of students to enter data for
    num_students = int(input("How many students do you need to enter grades for? "))

    # initializes count variable used in for loop
    count = 0

    # opens 'grade_entry.txt' for writing
    grades_file = open('grade_entry.txt', 'w')

    for num in range(1, num_students + 1):
        # gets the name of each student
        name = input(f"Enter the name of student {count + 1}: ")

        # gets the final letter grade of each student
        grade = input("Enter the student's final letter grade: ")

        # adds the name and grade of each student to students_list
        students_list.append([name, grade])

        # writes the data to 'grade_entry.txt'
        grades_file.write(f"'{name}', '{grade}'\n")

        # adds one to the count
        count += 1

    # closes grades_file
    grades_file.close()
    
    # prints students_list to the console
    print(students_list)


if __name__ == '__main__':
    main()

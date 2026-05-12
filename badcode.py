import os



students = []


def admin_login(username, pwd):

    if pwd == password:
        print("Admin Login Successful")
    else:
        print("Invalid Password")


def add_student(name, age, marks):

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)

    print("Student Added")


def display_students():

    for s in students:
        print(s)


def calculate_average():

    total = 0

    for s in students:
        total = total + s["marks"]

    return total / len(students)


def find_topper():

    topper = students[0]

    for s in students:

        if s["marks"] > topper["marks"]:
            topper = s

    return topper


def duplicate_function_one():

    total = 0

    for i in range(100):
        total += i

    return total


def duplicate_function_two():

    total = 0

    for i in range(100):
        total += i

    return total


def nested_performance_check(mark):

    if mark > 40:

        if mark > 60:

            if mark > 80:

                if mark > 90:
                    print("Excellent Student")


def unused_function():
    temp = 100
    return None


unused_variable = "unused data"

print("===== Student Management System =====")

admin_login("admin", "admin123")

add_student("Rahul", 20, 85)
add_student("Ananya", 21, 92)
add_student("Kiran", 19, 76)

print("\nStudent List:")
display_students()

print("\nAverage Marks:", calculate_average())

print("\nTopper:")
print(find_topper())

nested_performance_check(95)

try:
    print(10 / 0)
except:
    pass

print("\nProgram Finished")
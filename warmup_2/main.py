from student import Student
import random

def create_students(filename):
    """
    Return a list of students, that are created.
    Read a name and a student id (a number, that only one student have (in Aalto between 100000 and 999999))
    of the new student to be created, from the given file.
    The name and the student id are separated by a '/'.
    If the file is somehow incorrect read the next line. You can assume that the program always finds the called file.

    RETURNS
    a list of created __Student__-objects

    EXAMPLE
    create_students(filename)
        file:
        Teemu Teekkari/123456
        Tiina Teekkari/234567
        this line is incorrect
        Kaisa Kemisti/345678
        Kalle Kemisti/456789
    returns: a list of 4 Student-objects
    """
    #write your own code here
    file = open(filename)
    students = []
    for row in file:
        row1 = row.rstrip()
        if "/" in row1:
            try:
                #if int(row1.split("/")[1]):
                student = Student(row1.split("/")[0], int(row1.split("/")[1]))
                students.append(student)
            except:
                continue
    file.close()
    return students

def add_credits(student):
    """
    Ask credits (whole numbers, int) from the user and add the input to __student__-object as a list of numbers.
    The credits are separeted from each others by a "," in user input.
    If the input is incorrect return False, and don't save any of the given credits,
    otherwise return True and save the credits to object.

    RETURNS
    True/False

    EXAMPLE
    add_credits(student)
        user input: "5,5,5,4,3,10,3,8,5,15,5"
    returns: True
    saves to student: 5,5,5,4,3,10,3,8,5,15,5

    add_credits(student)
        user input: "5,5,5,,4,error,10,3,8,5,15,5"
    returns: False
    saves to student:
    """
    #write your own code here'
    try:
        credit_input = input("Give the credits:")
        credits = credit_input.split(",")
        for credit in range(0, len(credits)):
            credits[credit] = int(credits[credit])
        student.add_credits(credits)
        return True
    except:
        return False

def compare_student_numbers(student1, student2):
    """
    Compare two given Student-objects __student1__ and __student2__, and return the one with a smaller id.
    Use this function in sort_with_credits()!

    You can expect that the are no errors in __student1__ or __student2__.

    RETURNS:
    a Student-object

    EXAMPLE:
    given objects:
    student1, id: 123456
    student2, id: 234567

    compare_student_numbers(student1, student2):
    returns: student1
    """
    #write your own code here
    if student1.get_id() > student2.get_id():
        return student2
    else:
        return student1


def sort_with_credits(student_list):
    """
    Return a sorted list of Student-objects, from __student_list__-list,
    so the credits of the objects are sorted in ascending order.
    If two objects has same amount of credits put them in student number order, use a function compare_student_numbers() to this!

    You can expect that there are no errors in __student_list__.

    RETURNS:
    a list: of Student-objects

    EXAMPLE:
    objects in students:
    object1, sum of credits: 104    id: 123456
    object2, sum of credits: 26     id: 234567
    object3, sum of credits: 254    id: 345678
    object4, sum of credits: 104    id: 456789

    students_by_grade(students)
    returns: [ object2 , object1 , object4 , object3 ]
    """
    #write your own code here
    '''sum_credits = []
    for student in student_list:
        sum_credits.append(sum(student.get_credits()))
    sorted_credits = sorted(sum_credits)'''

    sorted_credits = sorted(student_list, key=lambda Student: Student.get_sum())
    for student1 in sorted_credits:
        for student2 in sorted_credits:
        if student1 == student2:
            result = compare_student_numbers(student1, student2)
            if result == student1:
                sorted_credits.student1, sorted_credits.student2 = sorted_credits.student2, sorted_credits.student1
            else:
                continue
        else:
            continue
    return sorted_list

def main():

    print("The students in the file are:")
    filename = "error_file_1.txt"
    students = create_students(filename)
    print(students)

    print("The student is:")
    student1 = Student("Saku", "111")
    student2 = Student("Sara", "222")
    student = compare_student_numbers(student1, student2)
    print(student)

    student_list = create_students("student_file.txt")
    for student in student_list:
        value = add_credits(student)
        if value:
            print("credits saved")
        else:
            print("something went wrong, no changes made")

    print("The list is:")
    sorted_list = sort_with_credits(student_list)
    for student in sorted_list:
        print(student.get_name())

main()
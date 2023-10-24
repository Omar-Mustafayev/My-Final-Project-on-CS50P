from project import get_prof,add_student,search_student,the_number_of_students
import csv


def test_get_prof():
    assert get_prof("WADADANG") == False
    assert get_prof(12322) == False
    assert get_prof("S") == "S"
    assert get_prof("Teacher") == "Teacher"

def test_add_student():
    assert add_student("something_that_invalid") == "Try again!"
    assert add_student("Omar Mustafayev 125") == "Student added successfully!"

def test_search_student():
    assert search_student("qweacs") == "\nStudent not found:("
    assert search_student(123) == "\nStudent not found:("

def test_the_number_of_students():
    i = 0
    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            i += 1
    assert the_number_of_students() == f"\nThe number of students: **{i}**"
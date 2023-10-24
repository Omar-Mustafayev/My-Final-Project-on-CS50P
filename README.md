# __PROJECT__
#### Video Demo:  <https://youtu.be/5jC2dHxRmfM>

## __Description:__
This project facilitates the university life of teachers and students

Project structure :
 - project.py
 - test_project.py
 - requirements.txt
 - students.csv
 - README.md


## __Used Libraries__

__TABULATE__ : Pretty-print tabular data in Python, a library and a command-line utility. [(Readmore)](https://github.com/astanin/python-tabulate)

__SYS__ : This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. [(Readmore)](https://docs.python.org/3/library/sys.html)

__CSV__ : The csv module in Python provides functionality for reading and writing data in the CSV (Comma-Separated Values) format. [(Readmore)](https://python-adv-web-apps.readthedocs.io/en/latest/csv.html )

__WIKIPEDIA__ : Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia. [(Readmore)](https://wikipedia.readthedocs.io/en/latest/)

__REQUESTS__ : Requests is a simple, yet elegant, HTTP library. [(Readmore)](https://requests.readthedocs.io/en/latest/)


## __Functioning__

The project.py contains 12 functions including the main function.

### __get_prof()__ __function__ :
This function asks the user whether he is a teacher or a student. User can type "Student", "S", "Teacher" or "T" (uppercase or lowercase doesn't matter). If the user types "T" or "Teacher", it invokes "teacher()" function. If the user types "S" or "Student", it invokes "student()" function.

### **Teacher (5 Functions)**:
#### __teacher()__ __function__:
This function asks the user "What do you want to do with your students? ". And calls other functions which are related to the user's request.
#### **__add_student(x)__ __function__**: this function takes one (x) parameter
If "x" contains student's name, surname and id truly, then this function writes "x" to "students.csv" using DictWriter. Else returns "Try again!".
#### **__search_student(y)__ __function__**: this function takes one (y) parameter
Where "y" is student's id. If "y" is in "students.csv", then returns students "First Name","Last Name" and "ID" using "tabulate" package. Else returns "\nStudent not found :("
#### **__show_all_students()__ __function__**:
Shows all students in "students.csv" using "tabulate" package.
#### **__the_number_of_students()__ __function__**:
Returns the number of students in "students.csv".


### **Student (5 Functions)**:
#### **__student()__ __function__**:
This function asks the user "What do you want to do? ". And calls other functions which are related to the user's request.
#### **__search_on_wikipedia(x)__ __function__**: this function takes one (x) parameter
Where "x" should be "Astrophysics", "Mathematics", "Computer Science" or "Chemistry" (actually user don't type or can't see these. User types "AS", "M", "CH" or "CS" as a key in __student()__ __function__). Then prints search results of "x" in [Wikipedia](https://www.wikipedia.org/)
#### **__apodd()__ __function__**:
When user types "APOD" in __student()__ __function__, then this function calls __apodd__ __function__. This function prints description and image url of NASA's [Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html)
#### **__other_func(x)__ __function__**: this function takes one (x) parameter
This function asks the user "What do you want to search for and in which language: ". Then prints search results of "x" in [Wikipedia](https://www.wikipedia.org/)
#### **__sentence(x=0)__ __function__**: this function takes one (x) parameter, where "x" is integer
With this fuction user sets the number of sentences in [Wikipedia](https://www.wikipedia.org/)'s result


### Author: Omar Mustafayev
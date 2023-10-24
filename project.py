from tabulate import tabulate
import csv
from sys import exit
import wikipedia
import requests


def main():
    print("\n\nWELCOME TO STUDENT-TEACHER PROGRAM!")
    print("YOU CAN USE SHORTCUTS!", end="\n\n\n")
    profession = get_prof(input("Are you Teacher or Student? ").title())
    while profession == False:
        profession = get_prof(input("Are you Teacher or Student? ").title())
    if profession in ["Teacher", "T"]:
        teacher()
    elif profession in ["Student", "S"]:
        student()


def get_prof(prof):
        if prof not in ["Student", "Teacher", "S", "T"]:
            return False
        else:
            return prof

def teacher():
    ability_of_teacher = [
        {"Key": "A", "Ability": "Add student to a list"},
        {"Key": "S", "Ability": "Search the student"},
        {"Key": "V", "Ability": "View the list"},
        {"Key": "T", "Ability": "The number of all students"},
        {"Key": "E", "Ability": "Exit program"},
    ]

    while True:
        print("\n"+ tabulate(ability_of_teacher, headers="keys", tablefmt="rounded_outline"))
        ability = input("What do you want to do with your students? ").title()
        if ability == "A":
            print(add_student(input("\nAction: Add student\nPlease type student's (Name, Surname, ID) correctly, that you want to add: ")))

        elif ability == "S":
            print(search_student(input("\nAction: Search Student\nPlease type student's ID correctly, that you want to search: ")))

        elif ability == "V":
            print(show_all_students())

        elif ability == "T":
            print(the_number_of_students())

        elif ability == "E":
            exit()

        else:
            print("Invalid key! Please, try again")


def add_student(x):
    try:
        name, surname, ID = x.split(" ")
        with open("students.csv", "a") as file:
                writer = csv.DictWriter(file, fieldnames=["First", "Last", "ID"])
                writer.writerow({"First": name, "Last": surname, "ID": ID})
                return "Student added successfully!"
    except:
         return "Try again!"

def search_student(y):
            with open("students.csv") as file:
                reader = csv.DictReader(file)
                s = []
                for row in reader:
                    if row["ID"] == y:
                        s.append(row)
                        return tabulate([["First Name", "Last Name", "ID"],[row["First"], row["Last"], row["ID"]],],headers="firstrow",tablefmt="rounded_grid",)
                if len(s) != 1:
                        return "\nStudent not found:("

def show_all_students():
        with open("students.csv") as file:
            reader = csv.DictReader(file)
            papa = []
            for row in reader:
                papa.append([row["First"], row["Last"], row["ID"]])
            return tabulate(papa,headers=["First Name", "Last Name", "ID"],tablefmt="rounded_grid",)

def the_number_of_students():
        i = 0
        with open("students.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                i += 1
        return (f"\nThe number of students: **{i}**")

def student():
    subjects_of_student = [
        {"Key": "AS", "Meaning": "Get information about Astrophysics"},
        {"Key": "M", "Meaning": "Get information about Mathematics"},
        {"Key": "CH", "Meaning": "Get information about Chemistry"},
        {"Key": "CS", "Meaning": "Get information about Computer Science"},
        {"Key": "O", "Meaning": "Look for other things you want"},
        {"Key": "APOD", "Meaning": "Astronomy Picture of the Day "},
        {"Key": "SET", "Meaning": "Set the number of sentences"},
        {"Key": "E", "Meaning": "Exit program"},
    ]


    while True:
        print("\n"+ tabulate(subjects_of_student, headers="keys", tablefmt="rounded_outline"))
        ability = input("What do you want to do? ").upper()
        wikipedia.set_lang("en")

        if ability == "CH":
            print("\n***\n",search_on_wikipedia("Chemistry"),"***\n")

        elif ability == "APOD":
            print("\nTo see image: ",apodd())

        elif ability == "CS":
            print("\n***\n",search_on_wikipedia("Computer Science"),"***\n")

        elif ability == "SET":
            sentence(int(input("How many sentences? ")))

        elif ability == "M":
            print("\n***\n",search_on_wikipedia("Mathematics"),"***\n")

        elif ability == "AS":
            print("\n***\n",search_on_wikipedia("Astrophysics"),"***\n")

        elif ability == "O":
            print("\n***\n",other_func(input("What do you want to search for and in which language: ")),"***\n")

        elif ability == "E":
            exit()

        else:
            print("Invalid key! Please, try again")
def search_on_wikipedia(x):
     return wikipedia.summary(x,sentences=sentencee)

def apodd():
    metadata = requests.get('https://api.nasa.gov/planetary/apod?api_key=MSE0LXrUZNXzCB21H77MBhmYoQoza8G72KwkA8d3')
    print("\nDescription:\n",metadata.json()['explanation'])
    return (metadata.json()['url'])


def other_func(x):
    try:
        requ,language = x.split("_")
        wikipedia.set_lang(language)
        return (wikipedia.summary(requ,sentences=sentencee))
    except:
        return ("Information not found:(")

sentencee=0
def sentence(x=0):
     global sentencee
     sentencee = x



if __name__ == "__main__":
    main()



from os import system
clear = lambda : system("clear")
#----------------------------------------------------------------------------------------------------------------
from json import load
try :
    with open("active_students.txt","r+") as stuinfo :
        active_students = load(stuinfo)
except(FileNotFoundError) : 
    print("found you!")
    active_students = []
#----------------------------------------------------------------------------------------------------------------
import datetime
#----------------------------------------------------------------------------------------------------------------
def check_codemelli(codemelli):
    for student in active_students:
        if student["code_melli"] == codemelli :
            return True
        return False

def check_studentcode(studentcode):
    for student in active_students:
        if student["student_code"] == studentcode :
            return True
        return False


class codemelli_uniqueness(Exception):
    pass

class codemelli_is_10_digits(Exception) :
    pass

class studentcode_uniqueness(Exception):
    pass

class studentcode_is_5_digits(Exception) :
    pass

def add_student():
    clear()
    global active_students 
    student = {}
    
    student["first_name"] = input("Enter student's First Name: ")

    student["last_name"] = input("Enter student's Last Name: ")

    student["birthday"] = input("Enter student's birth date: ").split("/") #-----------------error handling------------
    year, month, day = [int(item) for item in student["birthday"]]
    global birthday
    birthday = datetime.date(year, month, day)

    
    try :
        student["code_melli"] = int(input("Enter student's Code Melli: "))
        if len(str(student["code_melli"])) != 10 : raise codemelli_is_10_digits
        if check_codemelli(student["code_melli"]) : raise codemelli_uniqueness
    except(ValueError) :
        input("\nCode Melli must be numbers.\nPress Enter to return to menu...")
        return False
    except codemelli_is_10_digits :
        input("\nCode Melli  must be 10 digits.\nPress Enter to return to menu...")
        return False
    except codemelli_uniqueness :
        input("\nCode Melli  must be unique.\nPress Enter to return to menu...")
        return False
    
    try :
        student["student_code"] = int(input("Enter Student Code: "))
        if len(str(student["student_code"])) != 5 : raise studentcode_is_5_digits
        if check_studentcode(student["student_code"]) : raise studentcode_uniqueness
    except(ValueError) :
        input("\nStudent Code must be numbers.\nPress Enter to return to menu...")
        return False
    except studentcode_is_5_digits :
        input("\nStudent Code  must be 5 digits.\nPress Enter to return to menu...")
        return False
    except studentcode_uniqueness :
        input("\nStudent Code must be unique.\nPress Enter to return to menu...")
        return False
    
    student["courses"] = [item for item in input("Enter Stusent's Courses (ex. course1-course2-...) : ").split("-")]
    student["grades"] = [int(item) for item in input("Enter Student's Grades: (ex. grade of course1-grade of course2-...) ").split("-")]
    global courses_grades
    courses_grades = dict(zip(student["courses"] , student["grades"]))
    print(courses_grades)
    
    active_students.append(student)
    input("-----------------------------------\nStudent was added successfully!")
#----------------------------------------------------------------------------------------------------------------
def save_students():
    clear()
    from json import dump
    with open("active_students.txt","w+") as stuinfo:
        dump(active_students,stuinfo)
        input("Students has been saved successfully")
#----------------------------------------------------------------------------------------------------------------  
def delete_student():
    clear()
    student_code = input("Enter Student Code to delete: ")
    for student in active_students:
        if student["student_code"] == student_code :
            delete_or_move = input("Enter 'del' to Delete Permanent OR 'move' to Move Student to Graduated: ")
            if delete_or_move == "del" :
                sure = input("Are you sure? (y/n)")
                if sure == "y" :
                    active_students.remove(student)
                    input("\Student has been deleted successfully")
                else :
                    input("Press Enter to return to menu...")
            elif delete_or_move == "move" :
                pass #-------------------------------------------work on it______________________
            else : 
                input("Choose between del or move!")
                return False 
    else :
        print("----------------------------------")
        print("This student doesn't exist!")
        input("----------------------------------")
#----------------------------------------------------------------------------------------------------------------
def find_student():
    clear()
    studentcode = input("Enter Student Code to find the student: ")
    for student in active_students :
        if student["student_code"] == studentcode :
            print("----------------------------------")
            print(f"Firstname : {student['first_name']}")
            print(f"Lastname : {student['last_name']}")
            print(f"Birthday : {student['birthday']}")
            print(f"Code Melli : {student['code_melli']}")
            print(f"Student code : {student['student_code']}")
            print("----------------------------------")
            input("Press Enter...")
            break
    else :
        input("This student IS NOT in active students database !")
#----------------------------------------------------------------------------------------------------------------
def list_students():
    clear()
    for student in active_students :
        print("----------------------------------")
        print(f"Firstname : {student['first_name']}")
        print(f"Lastname : {student['last_name']}")
        print(f"Birthday : {student['birthday']}")
        print(f"Code Melli : {student['code_melli']}")
        print(f"Student code : {student['student_code']}")
    input("----------------------------------\nPress any key ...")

    # import pandas as pd

    # data = pd.read_csv(r'/Users/daryadashti/Documents/Python class/active_students.txt')
    # df = pd.DataFrame(data)

    # print(df)
    from prettytable import PrettyTable
    myTable = PrettyTable(["Firstname", "Lastname", "Birthday", "Code Melli", "Student code"])
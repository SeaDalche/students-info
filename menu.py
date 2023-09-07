import student_operations as stuop

while True :
    stuop.clear()
    print("Hi==================================")
    print("Press A to Add a Student")
    print("Press L to List Students")
    print("Press F to Find a Student")
    print("Press C to Change Courses")
    print("Press D to Delete a Student")
    print("Press S to Save Students")
    print("Press Q to Quit Application")
    print("====================================")
    choice = input("How can i help you? ").upper()
    if choice == "A" :
        stuop.add_student()
    elif choice == "L" :
        stuop.list_students()   
    elif choice == "F" :
        stuop.find_student()
    elif choice == "C" :
        stuop.change_courses()
    elif choice == "D" :
        stuop.delete_student()
    elif choice == "S" :
        stuop.save_students()
    elif choice == "Q" :
        break
    else : print("please choose one option from above:)")

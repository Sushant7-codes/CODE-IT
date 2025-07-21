from os import system

MENU= """
1. Reister a new student
2. Show all students
E. EXIT
"""
EXIT_MSG="""
############################
###Thanks , SEE YA LATER ###
############################
"""

STUDENTS=[]


def registration():
    print("REGISTRATION STARTED...")
    
    name=input("Enter student's name:")
    age=int(input("Enter student's age:"))
    address=input("Enter student's Address:")
    
    new_student={
        "name":name,
        "age":age,
        "address":address
    }
    STUDENTS.append(new_student)
    print("##### REGISTRATION SUCCESSFUL #####")
    
    
def show_all_students():
    for number,student in enumerate(STUDENTS, start=1):
        print(f""" 
              -----------Student No:{number}---------
              ----Name : {student["name"]}
              ----Age  : {student["age"]}
              ----Address: {student["address"]}
              -----------------------------------
              """  
        )


while True:
    print(MENU)
    choice=input("Enter a choice from MENU (1/2/E):")
    
    if choice=="1":
        # dict for registration
        registration()
    
    elif choice=="2":
        #data show
        show_all_students()
        pass
    
    elif choice in "Ee":
        print(EXIT_MSG)
        # exit program
        break
    
    else:
        system("clear")
        #invalid choice
        print("Invalid Choice")
        



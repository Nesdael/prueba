#We import the files we need
from menu import menu
from funciones import *
from crud import *


continuar = "si"
load_students_json(students)
while continuar == "si":
    menu() #print the menu
    opcion = input("Que desea realizar?\n") #asks the user to select an option
    
    #Then it enters these conditionals depending on what the user chooses
    if opcion == "1":
        register_student(students, generate_id)
    elif opcion == "2":
        list_students(students)
    elif opcion == "3":
        search_students(students)
    elif opcion == "4":
        update_students(students)
    elif opcion == "5":
        delete_students(students)
    elif opcion == "6":
        print("leaving the program")
        salir()
        
    else: #If you don't choose a valid option, it arrives here and asks you again, until you choose a correct option.
        print("Select a valid option")
        

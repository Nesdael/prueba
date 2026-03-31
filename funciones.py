from data_students import students
from crud import *

#This function will automatically create an ID
def generate_id(students):
    number = 0
    
    while True:
        number_student_id = str(number).zfill(4)
        
        exists = any(number_student_id in student for student in students)
        
        if not exists:
            return number_student_id
        
        number +=1 #If this sum already exists in the variable, it does so until it finds a free number.

def register_student(students, generate_id):
    
    #counters to avoid using while true
    register_name = 0
    register_age = 0
    register_course_program = 0
    register_state = 0
    
    student_id = generate_id(students)
    
    while register_name == 0:
        
        #We asked for the name here
        name = input("What is the student's name\n")
        
        #validations to ensure it's only letters
        if not name.replace(" ", "").isalpha():
            print("Error: You can only enter letters, try again.")
        else:
            print("Option valid")
            register_name = 1
            
    while register_age == 0:
        try:
            #we ask the age
            age = int(input("What is the student's age?\n"))
             #validations to ensure it's only letters
            if age <= 0:
                print("Error: please, enter a reasonable age.")
                continue
            else:
                print("Added age")
                register_age = 1
        except:
            print("Error: just enter digits")
            
    #Here you are asked if you want a course or a program
    while register_course_program == 0:
        print("=== Type of study ===")
        print("1.Course")
        print("2.Program")
        
        type_study = input("What type of study is the student doing??\n")
        
        if type_study == "1":
            type_study = "course"
            register_course_program = 1
        elif type_study == "2":
            type_study = "program"
            register_course_program = 1
        else:
            print("Select a valid option")
            continue
        
    #The state is recorded here
    while register_state== 0:
        print("=== State ===")
        print("1. Active")
        print("2. Inactive")
        
        state = input("What is the student's status?\n")
        
        if state == "1":
            state = "active"
            register_state = 1
        elif state == "2":
            state = "inactive"
            register_state = 1
        else:
            print("Select a valid option")
            continue
        
    # This is a dictionary, which will be saved in the "students" list  
    new_student = {
        student_id:{
            "name" : name.capitalize(),
            "age" : age,
            "type" : type_study.capitalize(),
            "state" : state.capitalize()
        }
    }

    students.append(new_student)
    save_students_json(students)
    return student_id, new_student

def list_students(students): #Here you will find a list of all registered students.
    if len(students) == 0:
        print("There are no registered students")
        return
    
    for student in students:
        for id, data in student.items():
            print("-" * 20)
            print(f"ID: {id}")
            print(f"Name: {data['name']}")
            print(f"Age: {data['age']}")
            print(f"Type: {data['type']}")
            print(f"State: {data['state']}")
            print("-" * 20)
            
def search_students(students): #Here we are looking for a student with the ID or name
    while True:
        print("How would you like to search?")
        print("1. Id")
        print("2. name")
        option = input("= ").strip()

        if option == "1":
            search = input("What is the ID you want to search for?\n").strip().zfill(4)
            print(f"looking for the id: {search}")
            for student in students:
                for id, data in student.items():
                    if id == search:
                        print(f"ID: {id}")
                        print(f"Name: {data['name']}")
                        print(f"Age: {data['age']}")
                        print(f"Type: {data['type']}")
                        print(f"State: {data['state']}")
                        return
        elif option == "2":
            search = input("What is the name you want to search for?\n").strip().lower()
            print(f"looking for the name: {search}")
            for student in students:
                for id, data in student.items():
                    if data['name'].lower == search:
                        print(f"ID: {id}")
                        print(f"Name: {data['name']}")
                        print(f"Age: {data['age']}")
                        print(f"Type: {data['type']}")
                        print(f"State: {data['state']}")
                        return
        else:
            print("Select a valid option")
            continue
              
def update_students(students): # This updates student data
    follow = "si"
    while follow == "si":
        read_register_json(students)
        student_id = input("What is the student ID you wish to update?\n").zfill(4)
        for student in students:
            if student_id in student:
                print("What do you want to update?")
                print("1. Name")
                print("2. Age")
                print("3. Type of study ")
                print("4. State")
                print("5. Return to menu")

                option = input("Choose an option\n")

                if option == "1":
                    name = 0
                    while name == 0:
                        new_name = input("update name: ").capitalize()
                        if not new_name.replace(" ", "").isalpha():
                            print("Error: You can only enter letters, try again.")
                            continue
                        else:
                            print("Option valid")
                            name = 1        
                    update_students_json(students, student_id, {"name": new_name})   
                    follow = "no" 
                elif option == "2":
                    age = 0
                    while age == 0:
                        try:
                            new_age = int(input("update age: "))
                            if new_age <= 0:
                                print("Error: please, enter a reasonable age.")
                                continue
                            else:
                                print("Updated age")
                                age = 1
                                follow = "no"
                        except:
                               print("Error: just enter digits")    
                               continue      
                    update_students_json(students, student_id, {'age': new_age})                                                
                elif option == "3":
                    type_study = 0
                    print("1.Course")
                    print("2.Program")
                    while type_study == 0:
                        new_type_study = input("What type of study is the student doing??\n")
                        if new_type_study == "1":
                            new_type_study = "course"
                            type_study = 1
                        elif new_type_study == "2":
                            new_type_study = "program"
                            type_study = 1
                        else:
                            print("Select a valid option")
                            continue
                    update_students_json(students, student_id, {'type': new_type_study})
                    follow = "no" 
                elif option == "4":
                    state = 0
                    while state == 0:
                        print("=== State ===")
                        print("1. Active")
                        print("2. Inactive")

                        new_state = input("What is the student's status?\n")

                        if new_state == "1":
                            new_state = "active"
                            state = 1
                            follow = "no"
                        elif new_state == "2":
                            new_state = "inactive"
                            state = 1
                            follow = "no"
                        else:
                            print("Select a valid option")
                            continue
                    update_students_json(students, student_id, {'state': new_state})

                elif option == "5":
                    follow = "no"
                else:
                    print("Select a valid option")
                    continue
    print(f"Cliente {student_id} actualizado correctamente")       
            
def delete_students(students): # This removes one piece of data.
    read_register_json(students)
    student_id = input("Ingrese el ID del cliente a eliminar: ").zfill(4)
    for student in students:
        for id in student:
            if id in student_id:           
                confirmation = input(f"Esta seguro que desea eliminar al cliente {student_id}? (s/n): ")

                if confirmation.lower() == "s":
                    result = delete_students_json(students, student_id)
                    if result:
                        print(f"Cliente {id} eliminado correctamente")
                    else:
                        print("Cliente no encontrado")
                else:
                    print("Operacion cancelada")               
    
    
def salir():
    exit()
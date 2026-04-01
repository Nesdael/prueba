import os
import json
from data_students import students
# We import the files and libraries we need

FILE_DATA = 'data'
ARCHIVE_JSON = os.path.join(FILE_DATA, "data.json")

def create_file(): # This function creates a folder if it doesn't exist.
    if not os.path.exists(FILE_DATA):
        os.makedirs(FILE_DATA)
        
def read_register_json(students): #This function reads the JSON file
    if not os.path.exists(ARCHIVE_JSON):
        return []
    with open(ARCHIVE_JSON, 'r', encoding= 'utf-8') as archive:
        return json.load(archive)
    
def load_students_json(students): #This function loads the JSON file that has already been created
    try:
        with open(ARCHIVE_JSON, 'r', encoding= 'utf-8') as archive:
            data = json.load(archive)
            for student in data:
                students.append(student)
    except FileNotFoundError: #If no file has been created yet, let it pass.
        pass
    
def save_students_json(students): #This function saves the elements we have added to the list, which will later be saved as JSON.
    create_file()
    read_register_json(students)
    with open(ARCHIVE_JSON, 'w', encoding= 'utf-8') as archive:
         json.dump(students, archive, indent=4)
         
#This function updates and then saves it with the save function        
def update_students_json(students, student_id, new_data):
    read_register_json(students)
    for student in students:
        if student_id in student:
            student[student_id].update(new_data)
            save_students_json(students)
            return True
    return False
    
#This function removes a user from the JSON and then saves it.
def delete_students_json(students, student_id):
    read_register_json(students)
    for student in students:
        if student_id in student:
            students.remove(student)
            save_students_json(students)
            return True
    return False
    
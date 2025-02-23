"""
This PoC will focus on file handling
where we manage employee records by
      reading from,
      writing to,
      updating, and
      deleting employee details in a file.

We will use a CSV file to store and manage the employee data.



Features of the PoC:
Add a new employee.
View all employees.
Update an employee record.
Delete an employee record.
Search for an employee.



    Steps:
    We will use a CSV file (employees.csv) to store employee data.
    Each employee will have attributes like ID, Name, Department, Salary.
    Python's csv module will help us read and write the data to/from the CSV file.

"""

import csv

#function to dispalpy employee menu
def display_menu():
    print("1. Add a new employee")
    print("2. view all employees")
    print("3. update an employee record")
    print("4. delete employee record")
    print("5. search for an employee")
    print("6. Exit")
file_path= "/inputdatasets/employee.csv"
#fucntion to add ean employee
def add_employee():
    with open(file_path,mode='a',newline='') as file:
        writer=csv.writer(file)
        emp_id=input("enter an employee id")
        name=input("enter a employee name")
        salary=input("enter employee salry")
        dept=input("emter empl dept")

        #wrirting a new row
        writer.writerow([emp_id,name,salary,dept])
        print("Employee details successfully added")
def view_allemployees():
    try:
         with open(file_path,mode='r') as file:
            reader=csv.reader(file)
            print("\n employee records are : ")
            for rows in reader:
                print(f"ID:{rows[0]},Name:{rows[1]},Salary:{rows[2]},Dept:{rows[3]}")
    except FileNotFoundError:
        print("No records found add an employee")

def update_employee():
    empl=[]
    emp_id=input("enter empid to update")

    found=False


    with open(file_path,mode='r') as file:
          reader=csv.reader(file)
          emplist=list(reader)

    #updating the record now
    for row in emplist:
        if row[0]==emp_id:
            row[1] = input(f"Enter new name for {row[1]}: ")
            row[2] = input(f"Enter new department for {row[2]}: ")
            row[3] = input(f"Enter new salary for {row[3]}: ")
            found = True
            break
    # Writing the updated records back to the file

    if found:
        with open(file_path,mode='w',newline='') as file:
            writer=csv.writer(file)
            writer.writerows(emplist)
        print("updated the records successfully")
    else:
        print(f"Employee with ID {emp_id} not found.")


def delete_employee():
    employees=[]
    emp_id=input("enter employee ID to delete: ")
    found=False
    # Reading all records to a list
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        employees = list(reader)
    for row in employees:
        if row[0]==emp_id:
            employees.remove(emp_id)
            Found=True
            break
        # Writing the updated records back to the file
    if found:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(employees)
        print("Employee record deleted successfully.")
    else:
        print(f"Employee with ID {emp_id} not found.")


# Function to search for an employee
def search_employee():
    emp_id = input("Enter employee ID to search: ")
    found = False

    # Searching for the employee record
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == emp_id:
                    print(f"Employee Found: ID: {row[0]}, Name: {row[1]}, Department: {row[2]}, Salary: {row[3]}")
                    found = True
                    break
            if not found:
                print(f"Employee with ID {emp_id} not found.")
    except FileNotFoundError:
        print("No records found. Add employees first.")


# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        view_allemployees()
    elif choice == '3':
        update_employee()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        search_employee()
    elif choice == '6':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")




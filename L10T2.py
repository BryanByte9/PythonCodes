#Example List for running.
employee_dict =[
    {'Name':'John','Workplace':'LUT','Age':25},
    {'Name':'Jack','Workplace':'Finnair','Age':18},
    {'Name':'Robin','Workplace':'JBL','Age':32},
    {'Name':'Annie','Workplace':'LUT','Age':24},
    {'Name':'Niels','Workplace':'Microsoft','Age':45},
]

def remove_employee(employee_list):
    try:
        #Print all Employees first
        print("List of Employees:")
        i = 1
        for person in employee_list:
            print(f"{i}) Name: {person['Name']}, Workplace: {person['Workplace']}, Age: {person['Age']}")
            i = i+1
        #Ask the index for employee to be removed
        index = int(input("Enter the number of the employee to remove:\n"))
        print(f"Removed employee: {employee_list[index-1]['Name']}")
        employee_list.remove(employee_list[index-1])
    except:
        print("Invalid input. Please enter a number.")

def modify_employee(employee_list):
    try:
        #Print all Employees first
        print("List of Employees:")
        i = 1
        for person in employee_list:
            print(f"{i}) Name: {person['Name']}, Workplace: {person['Workplace']}, Age: {person['Age']}")
            i = i+1
        #Ask which field to modify
        index = int(input("Enter the number of the employee to modify:\n"))
        modify_item = int(input("""Enter the field to modify:
1) Workplace
2) Age\n"""))
        if modify_item == 1:
            new_workplace = input("Enter new value for Workplace:\n")
            employee_list[index-1]['Workplace'] = new_workplace
        elif modify_item == 2:
            new_age = int(input("Enter new value for Age:\n"))
            employee_list[index-1]['Age'] = new_age
        else:
            print("Invalid input. Please enter a number.")
    except:
        print("Invalid input. Please enter a number.")

def print_employee(employee_list):
    print("List of Employees:")
    i = 1
    for person in employee_list:
        print(f"Name: {person['Name']}, Workplace: {person['Workplace']}, Age: {person['Age']}")
        i = i + 1

def menu():
    choice=input(("""Menu:
1) Remove an employee
2) Modify employee data
3) Print all employees
0) Exit
Enter your choice:\n"""))
    return choice

while True:
    try:
        choice = menu()
        choice = int(choice)
        if choice == 1:
            remove_employee(employee_dict)
        elif choice == 2:
            modify_employee(employee_dict)
        elif choice == 3:
            print_employee(employee_dict)
        elif choice == 0:
            print("See you again!")
            break
    except:
        print("Invalid input. Please enter a number.")
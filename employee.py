import empclass
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'employeeDB.dat'


def main():
    EmpList = load_employee()
    choice = 0
    
    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(EmpList)
        elif choice == ADD:
            add(EmpList)
        elif choice == CHANGE:
            change(EmpList)
        elif choice == DELETE:
            delete(EmpList)
    save_employee(EmpList)

def load_employee():
    try:
        input_file = open(FILENAME, 'rb')
        dct_employee = pickle.load(input_file)
        input_file.close()
    except IOError:
        dct_employee = {}
    return dct_employee


def get_menu_choice():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Look up a employee')
    print('2. Add a new empployee')
    print('3. Change an existing employee')
    print('4. Delete a employee')
    print('5. Quit')
    print()

    choice = int(input('Enter your choice: '))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))
    return choice


def look_up(EmpList):
    ID_number = input('Enter Employee ID Number: ')
    print(EmpList.get(ID_number, 'That ID is not found.'))


def add(EmpList):
    ID_number = input('Employee ID Number: ')
    name = input('Employee Name: ')
    department = input('Department: ')
    title = input('Job Title: ')
    entry = empclass.Employee(ID_number, name, department, title)

    if ID_number not in EmpList:
        EmpList[ID_number] = entry
        print('The entry has been added.')
    else:
        print('That ID Number already exists.')


def change(EmpList):
    ID_number = input('Enter a ID number: ')

    if ID_number in EmpList:
        name = input('Enter the name: ')
        department = input('Enter the new department: ')
        title = input('Enter the new Job Title: ')
        entry = empclass.Employee(ID_number,name, department, title)

        EmpList[ID_number] = entry
        print('Information updated.')
    else:
        print('That ID_number is not found.')


def delete(EmpList):
    ID_number = input('Enter a ID_number: ')
    if ID_number in EmpList:
        del EmpList[ID_number]
        print('Entry deleted.')
    else:
        print('That ID_number is not found.')

def save_employee(EmpList):
    output_file = open(FILENAME, 'wb')
    pickle.dump(EmpList, output_file)
    output_file.close()

main()

    

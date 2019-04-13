class Employee:
    def __init__(self, IDnumber, name, department, title):
        self.__IDnumber = IDnumber
        self.__name = name
        self.__department = department
        self.__title = title

    def set_name(self, name):
        self.__name = name

    def set_ID(self, IDnumber):
        self.__IDnumber = IDnumber

    def set_dept(self, department):
        self.__department = department

    def set_title(self, title):
        self.__title = title

    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__IDnumber

    def get_dept(self):
        return self.__department

    def get_title(self):
        return self.__title

    def __str__(self):
        return "IDNumber: " + self.__IDnumber + \
               "\nName: " + self.__name + \
               "\ndepartment: " + self.__department + \
               "\ntitle: " + self.__title
    

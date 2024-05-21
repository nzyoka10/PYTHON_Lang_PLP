# 
print('\n ----- Employee Class ----- ')
# 

class Employee:
    def __init__(self, emp_id, emp_name, emp_age, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_age = emp_age
        self.emp_department = emp_department

    # function to display Employee information
    def display_employee_info(self):
        print(f"Emp ID : {self.emp_id}")
        print(f"Emp Name : {self.emp_name}")
        print(f"Emp Age : {self.emp_age}")
        print(f"Emp department : {self.emp_department}")

emp = Employee(1, "Kenya Kwanza", 40, "ICT")
emp.display_employee_info()

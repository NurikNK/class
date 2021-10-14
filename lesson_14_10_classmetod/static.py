"""
@classmethod
@staticmethod
@property
"""


class Employee:
    number_of_employees = 0

    def __init__(self,first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        Employee.number_of_employees += 1

    @classmethod
    def get_number_of_employees(cls):
        return Employee.number_of_employees


# emp_1 =Employee("Alex", "Doe", 500)
# emp_2 =Employee("Alex", "Doe", 500)
# print(emp_1.first_name)
# print(Employee.number_of_employees)
# emp_1.number_of_employees = 10
# print(emp_1.__dict__)
# print(Employee.__dict__)
# print(Employee.get_number_of_employees())






class Employee:
    number_of_employees = 0

    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._pay = 0
        Employee.number_of_employees += 1

    @property
    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def pay(self):
        print("working getter")
        return self._pay

    @pay.setter
    def pay(self, pay):
        print("working setter")
        self._pay = pay

    @pay.deleter
    def pay(self):
        del self._pay
        print("Some logic before instance 'pay' attribute deletion")

    @classmethod
    def get_number_of_employees(cls):
        return Employee.number_of_employees

    @staticmethod
    def is_workday(day):
        if day == 6 or day == 7:
            return False
        return True


# emp_1 =Employee("Alex", "Doe")
# emp_2 =Employee("Alex", "Doe")
# # print(emp_1.first_name)
# print(Employee.number_of_employees)
# emp_1.number_of_employees = 10
# print(emp_1.__dict__)
# print(Employee.__dict__)
# print(Employee.get_number_of_employees())
# print(Employee.is_workday(6))
# print(emp_1.is_workday(5))
# print(Employee.number_of_employees)
# print(emp_1.pay)
# print(emp_1.fullname)

# print(emp_1.pay)
# emp_1.pay = 6000
# del emp_1.pay




class Employee:
    number_of_employees = 0

    def __init__(self,first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self._pay = pay
        Employee.number_of_employees += 1

    @property
    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def pay(self):
        print("working getter")
        return self._pay

    @pay.setter
    def pay(self, pay):
        print("working setter")
        self._pay = pay

    @pay.deleter
    def pay(self):
        del self._pay
        print("Some logic before instance 'pay' attribute deletion")

    @classmethod
    def get_number_of_employees(cls):
        return Employee.number_of_employees

    @classmethod
    def from_string(cls, emp_str):
        f_name, l_name, salary = emp_str.split('-')
        return cls(f_name, l_name, float(salary))

    @staticmethod
    def is_workday(day):
        if day == 6 or day == 7:
            return False
        return True


emp_1 =Employee("Alex", "Doe", 50)
emp_2 =Employee("Alex", "Doe", 58)
emp_3 =Employee("Alex", "Doe", 588)

emp_str_1 = "john- Doe-70000"
emp_str_2 = "john- Doet-80000"
emp_str_3 = "john- Does-90000"

emp_1 = Employee.from_string(emp_str_1)
print(emp_1.fullname)

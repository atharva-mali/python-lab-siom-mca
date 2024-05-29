# Python Method Overriding
class Employee:
    def message(self):
        print("This message is from Employee Class")

class Company(Employee):
    def message(self):
        print("This Company Class is inherited from Employee")

emp=Employee()
emp.message()
comp=Company()
comp.message()
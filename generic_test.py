from typing import Mapping, TypeVar

class Employee:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Employee(name:{self.name})"

class Accountant(Employee): ...
class TeamLead(Employee): ...


EmployeeType = TypeVar("EmployeeType",Employee,str) # Generic

def notify_by_email(employees: set[EmployeeType], overrides: Mapping[str, str]) -> list[EmployeeType]:
    return list(employees)

employee_1 = Employee("Emp1")
employee_2 = Employee("Emp2")
employee_3 = Employee("Emp3")

# output = notify_by_email({employee_1,employee_2},{"test":"test"})
# print(output)

# output = notify_by_email({"employee_1","employee_2"},{"test":"test"})
# print(output)

# output1 = notify_by_email({employee_1,"employee_2"},{"test":"test"})
# print(output1)

#output1 = notify_by_email({10,20,30},{"test":"test"})
#print(output1)

employee_4 = Accountant("Emp4")
employee_5 = Accountant("Emp5")
employee_6 = TeamLead("Emp6")

output2 = notify_by_email({employee_4,employee_5,employee_6},{"test":"test"})
print(output2)
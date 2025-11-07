# Jonathan Sonnek
# November 6 2025
# Program #4 Employee Class:

# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.
class Employee:
    def __init__(self, name, ID_Number, department, job_title):
        self.name = name
        self.ID_Number = ID_Number
        self.department = department
        self.job_title = job_title
    def print_data(self):
        print(self.name, self.ID_Number, self.department, self.job_title)
# Create and display objects
def main():
    employee1 = Employee("Susan Meyers", "47899", "Accounting", "Vice President")
    employee1.print_data()
    employee2 = Employee("Mark Jones", "39119", "IT", "Programmer")
    employee2.print_data()
    employee3 = Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")
    employee3.print_data()
main()
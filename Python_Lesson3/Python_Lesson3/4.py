class Employee:
    # Creating members to calculate Average salary and keep track of count of employees
    counter = 0
    salary_sum = 0

    # Constructor for Intializing the name, family salary and department
    def __init__(self, n, f, s, d):
        self.name = n
        self.family = f
        self.salary = s
        self.department = d
        Employee.counter += 1
        Employee.salary_sum += s

    # Function of calculating the average salary of all employees
    def get_avg_sal(self):
        average_sal = self.salary_sum / self.counter
        print("The average salary is: " + str(average_sal))
        return

    # Function to display employee Information
    def display(self):
        print("Name:" + self.name, "Family:" + self.family, "Salary:" + str(self.salary),
              "Department:" + self.department)


class FulltimeEmployee(Employee):

    # Inheriting the properties of Employee during initialization
    def __init__(self, n, f, s, d):
        Employee.__init__(self, n, f, s, d)


print("#" * 50)
e1 = Employee("Saran", "Akkiraju", 7000, "CS")
e1.display()
print("*" * 50)
e2 = Employee("Shantan", "Akkiraju", 6000, "CS")
e2.display()
print("*" * 50)
e3 = Employee("Shreeya", "Tataji", 5000, "CS")
e3.display()
print("*" * 50)
e4 = FulltimeEmployee("Ramu", "Akkiraju", 8000, "CS")
e4.display()
print("*" * 50)
Employee.get_avg_sal(Employee)
print("#" * 50)
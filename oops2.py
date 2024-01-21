class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        print(self.salary)


kg = Employee("Kaustubh", "5 CR")
print(kg.name)
print(kg.salary)

kg.getSalary()
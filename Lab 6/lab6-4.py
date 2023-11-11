class Employee:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Name: {self.name}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name)
        self.salary = salary
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Position: Manager\nSalary: ${self.salary}\nDepartment: {self.department}")

    def assign_task(self, task):
        print(f"Manager {self.name} assigns the task: {task}")

class Engineer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name)
        self.salary = salary
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Position: Engineer\nSalary: ${self.salary}\nProgramming Language: {self.programming_language}")

    def write_code(self):
        print(f"Engineer {self.name} is writing code.")

class Salesperson(Employee):
    def __init__(self, name, salary, sale_goal):
        super().__init__(name)
        self.salary = salary
        self.sale_goal = sale_goal

    def display_info(self):
        super().display_info()
        print(f"Position: Salesperson\nSalary: ${self.salary}\nSale Goal: ${self.sale_goal}")

    def make_sale(self, amount):
        if amount >= self.sale_goal:
            print(f"Salesperson {self.name} made a sale of ${amount}. Goal achieved!")
        else:
            print(f"Salesperson {self.name} made a sale of ${amount}. Goal not met.")


manager = Manager("John Manager", 80000, "Marketing")
manager.display_info()
manager.assign_task("Develop marketing strategy")
print("\n")
engineer = Engineer("Alice Engineer", 75000, "Python")
engineer.display_info()
engineer.write_code()
print("\n")
salesperson = Salesperson("Bob Salesperson", 70000, 100000)
salesperson.display_info()
salesperson.make_sale(120000)
salesperson.make_sale(80000)

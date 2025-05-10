class Employee():
    def __init__(self, first_name, last_name, salary=0):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, increase=5000):
        self.salary += increase
        return self.salary


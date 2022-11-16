class Employee:
    """Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first.capitalize()} {self.last.capitalize()}'


if __name__ == '__main__':
    employee = Employee("Suresh", "Sigera")
    print(employee.fullname)

import unittest
from src.employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('saral', 'gyaan')
        emp_2 = Employee('udit', 'vashisht')
        self.assertEqual(emp_1.email, 'saralgyaan@email.com')
        self.assertEqual(emp_2.email, 'uditvashisht@email.com')

        emp_1.first = "first"
        emp_2.first = "second"

        self.assertEqual(emp_1.email, 'firstgyaan@email.com')
        self.assertEqual(emp_2.email, 'secondvashisht@email.com')

    def test_fullname(self):
        emp_1 = Employee('saral', 'gyaan')
        emp_2 = Employee('udit', 'vashisht')
        self.assertEqual(emp_1.fullname, 'Saral Gyaan')
        self.assertEqual(emp_2.fullname, 'Udit Vashisht')

        emp_1.first = "first"
        emp_2.first = "second"

        self.assertEqual(emp_1.fullname, 'First Gyaan')
        self.assertEqual(emp_2.fullname, 'Second Vashisht')


if __name__ == '__main__':
    unittest.main()

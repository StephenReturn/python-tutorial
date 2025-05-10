from company import Employee
import unittest
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Stephen", "Wang")
        # self.employee.firstName = "Stephen"
        # self.employee.lastName = "Wang"
        self.employee.salary = 2000
    def test_default_raise(self):
        self.assertEqual(self.employee.give_raise(), 7000)
    def test_custom_raise(self):
        self.assertEqual(self.employee.give_raise(10000), 12000)




if __name__ == "__main__":
    unittest.main()
import unittest
from employee import employee_details


class TestEmployeeDetails(unittest.TestCase):
    def test_output_type(self):
        self.assertIsInstance(employee_details('Marius', 32, 'mciurea@vodafone.com', 5000, 21), str)

    def test_working_days_not_int(self):
        self.assertRaises(TypeError, employee_details, 'Marius', 32, 'mciurea@vodafone.com', 5000, '21')

    def test_devision_by_zero_error(self):
        self.assertRaises(ZeroDivisionError, employee_details, 'Marius', 32, 'mciurea@vodafone.com', 5000, 0)

    def test_output(self):
        self.assertEqual(employee_details('Maria', 30, 'maria@company.com', 10000, 22), 'Welcome Maria. Your age is 30 years old.Your email address: maria@company.com and hourly income: ' + str(10000/(22*8)))


if __name__ == '__main__':
    unittest.main()

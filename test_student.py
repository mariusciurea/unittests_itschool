import os
import unittest
from student import Student
from unittest.mock import patch, MagicMock

unittest.TestLoader.sortTestMethodsUsing = None


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')
        student = Student('Marius', 'Ciurea', 'upb', 1910709282211)
        student.save_student_info()

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')
        print(os.listdir('.'))
        os.remove('ciurea_1910709282211.txt')
        print(os.listdir('.'))

    def setUp(self) -> None:
        print('setup here')
        self.s1 = Student('Marius', 'Ciurea', 'upb', 1910709282211)
        self.s2 = Student('Dan', 'Chivu', 'upb', 1890709282211)

    def tearDown(self) -> None:
        print('tear down here\n')
        del self.s1
        del self.s2

    def test_email(self):
        print('test_email')
        # s1 = Student('Marius', 'Ciurea', 'upb', 1910709282211)
        # s2 = Student('Dan', 'Chivu', 'upb', 1890709282211)

        self.assertEqual(self.s1.email, 'marius.ciurea@upb.com')
        self.assertEqual(self.s2.email, 'dan.chivu@upb.com')

        self.s1.lastname = 'Popescu'
        self.s2.lastname = 'Cirstea'

        self.assertEqual(self.s1.email, 'marius.popescu@upb.com')
        self.assertEqual(self.s2.email, 'dan.cirstea@upb.com')

    def test_file_path(self):
        print('test_file_path')
        # s1 = Student('Marius', 'Ciurea', 'upb', 1910709282211)
        # s2 = Student('Dan', 'Chivu', 'upb', 1890709282211)

        self.assertEqual(self.s1.info_path, 'ciurea_1910709282211.txt')
        self.assertEqual(self.s2.info_path, 'chivu_1890709282211.txt')

        self.s1.lastname = 'Popescu'
        self.s2.lastname = 'Cirstea'

        self.assertEqual(self.s1.info_path, 'popescu_1910709282211.txt')
        self.assertEqual(self.s2.info_path, 'cirstea_1890709282211.txt')

    def test_cnp(self):
        print('test_cnp')
        # s1 = Student('Marius', 'Ciurea', 'upb', 1910709282211)
        # s2 = Student('Dan', 'Chivu', 'upb', 1890709282211)

        self.assertIsInstance(self.s1.cnp, int)
        self.assertIsInstance(self.s2.cnp, int)
        with self.assertRaises(ValueError):
            Student('Marius', 'Ciurea', 'upb', '1910709282211')
        with self.assertRaises(ValueError):
            Student('Marius', 'Ciurea', 'upb', 123)

    def test_file_content(self):
        with open(self.s1.info_path, 'r') as fr:
            data = fr.read()
        self.assertTrue(data)

    @patch('student.requests.get')
    def test_get_student_classes(self, mock_requests):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {'1910709282211': {'Classes': '123'}}
        mock_requests.return_value = mock_response
        classes = self.s1.get_student_classes()
        self.assertEqual(classes, '123')

        mock_response.ok = True
        mock_response.json.return_value = {'1890709282211': {'Classes': '123'}}
        mock_requests.return_value = mock_response
        self.assertEqual(self.s2.get_student_classes(), '123')


if __name__ == '__main__':
    unittest.main()

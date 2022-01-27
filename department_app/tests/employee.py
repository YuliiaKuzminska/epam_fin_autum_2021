"""
Defines test cases for employee model.
"""
import unittest
from datetime import datetime
from department_app.models.employee import Employee


class EmployeeModelTests(unittest.TestCase):
    """
    Employee model test cases.
    """

    def test_true_if_object_the_same(self):
        """
        Test Employee model.
        :return: None
        """
        actual = Employee(
                forename='Mike',
                surname='Redknapp',
                birthdate=datetime.strptime('2000/01/15', '%Y/%m/%d').date(),
                salary=10000,
            )
        expected = Employee(
                forename='Mike',
                surname='Redknapp',
                birthdate=datetime.strptime('2000/01/15', '%Y/%m/%d').date(),
                salary=10000,
            )

        self.assertEqual(actual, expected)

    def test_false_if_object_not_the_same(self):
        """
        Test Employee model.
        :return: None
        """
        actual = Employee(
                forename='Mike',
                surname='Redknapp',
                birthdate=datetime.strptime('2000/01/15', '%Y/%m/%d').date(),
                salary=10000,
            )
        expected = Employee(
                forename='Klim',
                surname='Redknapp',
                birthdate=datetime.strptime('2000/01/15', '%Y/%m/%d').date(),
                salary=10000,
            )

        self.assertNotEqual(actual, expected)

    def test_exception_when_wrong_object_type(self):
        """
        Test Employee model.
        :return: None
        """
        actual_1 = Employee(
                forename=1,
                surname='Redknapp',
                birthdate=datetime.strptime('2000/01/15', '%Y/%m/%d').date(),
                salary=10000,
            )

        actual_2 = Employee(
                forename='Mike',
                surname='Redknapp',
                birthdate=datetime.strptime('2000/01/15', '%Y/%m/%d').date(),
                salary="asdasd",
            )

        actual_3 = Employee(
                forename='Mike',
                surname='Redknapp',
                birthdate=10,
                salary=10000,
            )

        self.assertRaises(TypeError, actual_1)
        self.assertRaises(TypeError, actual_2)
        self.assertRaises(TypeError, actual_3)

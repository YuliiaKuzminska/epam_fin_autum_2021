"""
Defines test cases for department model.
"""
import unittest
from department_app.models.department import Department


class DepartmentModelTests(unittest.TestCase):
    """
    Department model test cases.
    """

    def test_true_if_object_the_same(self):
        """
        Tests department model.
        :return: None
        """
        actual = Department("Department of state")
        expected = Department("Department of state")

        self.assertEqual(actual, expected)

    def test_false_if_object_not_the_same(self):
        """
        Tests department model.
        :return: None
        """
        actual = Department("Department of state")
        expected = Department("Department of department")

        self.assertNotEqual(actual, expected)

    def test_exception_when_wrong_object_type(self):
        """
        Tests department model.
        :return: None
        """
        actual_1 = Department(1)
        actual_2 = Department(list())
        actual_3 = Department(True)

        self.assertRaises(TypeError, actual_1)
        self.assertRaises(TypeError, actual_2)
        self.assertRaises(TypeError, actual_3)

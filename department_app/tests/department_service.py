"""
Defines test cases for department service.
"""
import unittest
from department_app.service.department_service import *


class DepartmentServiceTests(unittest.TestCase):
    """
    Department service test cases(get_all_departments_service()).
    """

    def test_1_get_all(self):
        """
        Test to receive all departments.
        :return: None
        """
        expected_list = [
            Department("Sales Department"),
            Department("Development Department"),
            Department("Testing Department")
        ]
        actual_list = get_all_departments_service()

        self.assertEqual(expected_list, actual_list)
        self.assertEqual(len(get_all_departments_service()), 3)

    def test_2_get_by_id(self):
        """
        Test to get department by id(get_department_by_id_service(id)).
        :return: None
        """
        expected_department = get_department_by_id_service(1)
        expected_department_id = get_department_by_id_service(1).id

        actual_department = Department("Sales Department")

        self.assertEqual(expected_department, actual_department)
        self.assertEqual(expected_department_id, 1)

    def test_3_add(self):
        """
        Test for adding a Department(add_department_service()).
        :return: None
        """
        expected_list = [
            Department("Sales Department"),
            Department("Development Department"),
            Department("Testing Department"),
            Department("Dep_4")
        ]

        add_department_service("Dep_4")

        actual_list = get_all_departments_service()

        self.assertEqual(len(get_all_departments_service()), 4)
        self.assertEqual(expected_list, actual_list)

    def test_4_update(self):
        """
        Department Update Test(get_department_by_id_service(id), new name).
        :return: None
        """
        self.assertEqual(get_department_by_id_service(4), Department("Dep_4"))

        update_department_service(4, 'Dep_444')

        self.assertEqual(get_department_by_id_service(4), Department("Dep_444"))

    def test_5_get_average_salary(self):
        """
        Tests to get department average salary(get_department_average_salary_service(Department)).
        :return: None
        """
        departments = get_all_departments_service()
        expected_salary_list = [14000.0, 9500.0, 12700.0, 0]
        actual_avg_salary_list = [get_department_average_salary_service(dep) for dep in departments]

        self.assertEqual(actual_avg_salary_list, expected_salary_list)

    def test_6_delete(self):
        """
        Department deletion test.
        :return: None
        """
        expected_list = [
            Department("Sales Department"),
            Department("Development Department"),
            Department("Testing Department"),
            Department("Dep_444")
        ]
        actual_list = get_all_departments_service()

        self.assertEqual(actual_list, expected_list)

        expected_list.remove(Department("Dep_444"))
        delete_department_service(4)
        actual_list = get_all_departments_service()

        self.assertEqual(actual_list, expected_list)

    def test_7_to_dict(self):
        """
        Dictionary representation of the testing department.
        :return: None
        """
        department = departments_to_dict(1)
        self.assertEqual(department['id'], 1)
        self.assertEqual(department['name'], 'Sales Department')
        self.assertEqual(department['employees_count'], 3)
        self.assertEqual(department['average_salary'], 14000)
        self.assertEqual(len(department['employees']), 3)

"""
Defines test cases for employee service.
"""
import unittest
from datetime import datetime, date

from department_app.models.employee import Employee
from department_app.service.employee_service import add_employee_service, update_employee_service, get_employee_by_id_service, \
    get_by_birthdate_service, get_all_employees_service, delete_employee_service, employee_to_dict, get_all_employees_for_department


class EmployeeServiceTests(unittest.TestCase):
    """
    Employee service test cases.
    """

    def test_1_get_all(self):
        """
        Tests to get all employees.
        :return: None
        """
        expected_employees = 9
        actual_employees = len(get_all_employees_service())

        self.assertEqual(expected_employees, actual_employees)

    def test_2_get_all_for_department(self):
        """
        Tests to get all employees for the department.
        :return: None
        """
        expected_employees = 3
        actual_employees = len(get_all_employees_for_department(1))

        self.assertEqual(expected_employees, actual_employees)

    def test_3_get_by_id(self):
        """
        Tests to get employee by id.
        :return: None
        """
        expected_employee = Employee('David', 'Campbel', date(2001, 1, 30), 15000)
        actual_employee = get_employee_by_id_service(1)

        self.assertEqual(expected_employee, actual_employee)

    def test_4_get_by_birthdate(self):
        """
        Tests to get employee with birthdate in mentioned period.
        :return: None
        """
        date_from = datetime.strptime('2000/01/01', '%Y/%m/%d')
        date_to = datetime.strptime('2004/09/07', '%Y/%m/%d')
        self.assertEqual(len(get_by_birthdate_service(date_from, date_to)), 4)

    def test_5_add(self):
        """
        Tests to add_department employee.
        :return: None
        """
        add_employee_service(
            forename='Mike',
            surname='Redknapp',
            department_id=1,
            birthdate=datetime.strptime('2000/01/15', '%Y/%m/%d').date(),
            salary=18000
        )
        self.assertEqual(len(get_all_employees_service()), 10)

    def test_6_update(self):
        """
        Tests to update_department_service employee.
        :return: None
        """
        birthdate = datetime.strptime('2001/02/13', '%Y/%m/%d').date()
        update_employee_service(
            employee_id=10,
            forename='Klim',
            surname='Barton',
            department_id=1,
            birthdate=birthdate,
            salary=20000
        )
        self.assertEqual(get_employee_by_id_service(10).forename, 'Klim')
        self.assertEqual(get_employee_by_id_service(10).surname, 'Barton')
        self.assertEqual(get_employee_by_id_service(10).department_id, 1)
        self.assertEqual(get_employee_by_id_service(10).birthdate, birthdate)
        self.assertEqual(get_employee_by_id_service(10).salary, 20000)

    def test_7_delete(self):
        """
       Tests to delete employee.
        :return: None
        """
        delete_employee_service(10)
        self.assertEqual(len(get_all_employees_service()), 9)

    def test_8_to_dict(self):
        """
        Tests employee dictionary representation.
        :return: None
        """
        employee = employee_to_dict(1)
        self.assertEqual(employee['forename'], 'David')
        self.assertEqual(employee['surname'], 'Campbel')
        self.assertEqual(employee['department'], 'Sales Department')
        self.assertEqual(employee['birthdate'], '2001-01-30')
        self.assertEqual(employee['salary'], 15000)

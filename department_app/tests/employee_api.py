"""
Defines test cases for employee API.
"""
import json
import unittest
from datetime import date

from department_app import app
from department_app.models.employee import Employee

HOST = 'http://127.0.0.1:5000'
client = app.test_client()


class EmployeeApiTests(unittest.TestCase):
    """
    Employee API test cases.
    """

    def test_1_get_search_api(self):
        """
        Tests to search employees with birthdate in mentioned period.
        :return: None
        """
        with client:
            response = client.get(f'{HOST}/api/employees/search')
            employees_1 = json.loads(response.data)

            response = client.get(f'{HOST}/api/employees/search?date_from=2000/01/01&date_to=2004/03/30')
            employees_2 = json.loads(response.data)

            self.assertEqual(employees_1['message'], 'Incorrect date')
            self.assertEqual(len(employees_2), 4)

    def test_2_get_list_api(self):
        """
        Test for the return of all employees.
        :return: None
        """
        with client:
            response = client.get(f'{HOST}/api/employees')
            employees = json.loads(response.data)

            self.assertEqual(len(employees), 9)

    def test_3_post_list_api(self):
        """
        The test is to check the addition of the new employee.
        :return: None
        """
        with client:
            response = client.post(f'{HOST}/api/employees')
            employees_1 = json.loads(response.data)

            response = client.post(f'{HOST}/api/employees', data={
                'forename': 'Mike',
                'surname': 'Redknapp',
                'birthdate': '2000/20/12',
                'salary': '123456',
                'department': 'Sales Department'
            })
            employees_2 = json.loads(response.data)

            response = client.post(f'{HOST}/api/employees', data={
                'forename': 'Mike',
                'surname': 'Redknapp',
                'birthdate': '2000/05/15',
                'salary': '123456',
                'department': 'Department of State'
            })
            employees_3 = json.loads(response.data)

            response = client.post(f'{HOST}/api/employees', data={
                'forename': 'Mike',
                'surname': 'Redknapp',
                'birthdate': '2000/01/21',
                'salary': 'Aaa100001Bbb',
                'department': 'Sales Department'
            })
            employees_4 = json.loads(response.data)

            response = client.post(f'{HOST}/api/employees', data={
                'forename': 'Mike',
                'surname': 'Redknapp',
                'birthdate': '2000/01/21',
                'salary': '123456',
                'department': 'Sales Department'
            })
            employees_5 = json.loads(response.data)

            self.assertEqual(employees_1['message'], 'Incorrect request')
            self.assertEqual(employees_2['message'], 'Incorrect birthdate')
            self.assertEqual(employees_3['message'], 'Incorrect department')
            self.assertEqual(employees_4['message'], 'Incorrect salary')
            self.assertEqual(employees_5[0]['forename'], 'Mike')

    def test_4_get_api(self):
        """
        Test for the presence of a employee in the DB.
        :return: None
        """
        with client:
            response = client.get(f'{HOST}/api/employee/1')
            employee_1 = json.loads(response.data)

            response = client.get(f'{HOST}/api/employee/11')
            employee_2 = json.loads(response.data)

            self.assertEqual(employee_1['forename'], 'David')
            self.assertEqual(employee_2['message'], 'Employee not found')

    def test_5_put_api(self):
        """
        Tests for edit employee.
        :return: None
        """
        with client:
            response = client.put(f'{HOST}/api/employee/11', data={'salary': '2000'})
            employee_1 = json.loads(response.data)

            response = client.put(f'{HOST}/api/employee/10', data={'birthdate': '1900/20/01'})
            employee_2 = json.loads(response.data)

            response = client.put(f'{HOST}/api/employee/10', data={'department': 'Dep_4'})
            employee_3 = json.loads(response.data)

            response = client.put(f'{HOST}/api/employee/10', data={'salary': 'salary'})
            employee_4 = json.loads(response.data)

            response = client.put(f'{HOST}/api/employee/10', data={
                'forename': 'Klim',
                'surname': 'Barton',
                'birthdate': '2001/02/22',
                'salary': '20000',
                'department': 'Development Department'
            })
            employee_5 = json.loads(response.data)

            self.assertEqual(employee_1['message'], 'Employee not found')
            self.assertEqual(employee_2['message'], 'Incorrect birthdate')
            self.assertEqual(employee_3['message'], 'Incorrect department')
            self.assertEqual(employee_4['message'], 'Incorrect salary')
            self.assertEqual(employee_5[0]['forename'], 'Klim')

    def test_6_delete_api(self):
        """
        Tests for delete employee.
        :return: None
        """
        with client:
            actual_1 = json.loads(client.get(f'{HOST}/api/employee/10').data)
            expected_1 = {
                'birthdate': '2001-02-22',
                'department': 'Development Department',
                'forename': 'Klim',
                'id': 10,
                'salary': 20000,
                'surname': 'Barton'
            }

            self.assertEqual(actual_1, expected_1)

            client.delete(f'{HOST}/api/employee/10')

            response = client.delete(f'{HOST}/api/employee/10')
            expected = json.loads(response.data)

            self.assertEqual(expected['message'], 'Employee not found')

"""
Defines test cases for department API.
"""
import json
import unittest
from department_app import app

client = app.test_client()
HOST = 'http://127.0.0.1:5000'


class DepartmentApiTests(unittest.TestCase):
    """
    Department API test cases.
    """

    def test_1_get_list_api(self):
        """
        Test for the return of all departments
        :return: None
        """
        with client:
            response = client.get(f'{HOST}/api/departments')
            expected_json = json.loads(response.data)
            expected_length = len(expected_json)
            expected_name_1, expected_name_2, expected_name_3 = [i.get('name') for i in expected_json]

            actual_length = 3
            actual_name_1 = "Sales Department"
            actual_name_2 = "Development Department"
            actual_name_3 = "Testing Department"

            self.assertEqual(actual_length, expected_length)
            self.assertEqual(actual_name_1, expected_name_1)
            self.assertEqual(actual_name_2, expected_name_2)
            self.assertEqual(actual_name_3, expected_name_3)

    def test_2_post_list_api(self):
        """
        The test is to check the addition of the new department
        :return: None
        """
        with client:
            response = client.post(f'{HOST}/api/departments', data=None)
            departments_1 = json.loads(response.data)

            response = client.post(f'{HOST}/api/departments', data={'name': 'Dep_4'})
            departments_2 = json.loads(response.data)

            response = client.post(f'{HOST}/api/departments', data={'name': 'Dep_4'})
            departments_3 = json.loads(response.data)

            self.assertEqual(departments_1['message'], 'Incorrect request')
            self.assertEqual(departments_2[0]["name"], "Dep_4")
            self.assertEqual(departments_3['message'], 'Department already exists')

    def test_3_get_api(self):
        """
        Test for the presence of a department in the database
        :return: None
        """
        with client:
            response = client.get(f'{HOST}/api/department/1')
            expected_1 = json.loads(response.data)

            response = client.get(f'{HOST}/api/department/5')
            expected_2 = json.loads(response.data)

            self.assertEqual(expected_1['name'], 'Sales Department')
            self.assertEqual(expected_2['message'], 'Department not found')

    def test_4_put_api(self):
        """
        Tests for edit department.
        :return: None
        """
        with client:
            response = client.put(f'{HOST}/api/department/5', data={'name': 'Dep_5'})
            expected_1 = json.loads(response.data)

            response = client.put(f'{HOST}/api/department/4')
            expected_2 = json.loads(response.data)

            response = client.put(f'{HOST}/api/department/4', data={'name': 'Dep_5'})
            expected_3 = json.loads(response.data)

            response = client.put(f'{HOST}/api/department/4', data={'name': 'Sales Department'})
            expected_4 = json.loads(response.data)

            self.assertEqual(expected_1['message'], 'Department not found')
            self.assertEqual(expected_2['message'], 'Incorrect request')
            self.assertEqual(expected_3[0]['name'], 'Dep_5')
            self.assertEqual(expected_4['message'], 'Department already exists')

    def test_5_delete_api(self):
        """
        Tests for delete department.
        :return: None
        """
        with client:

            response = client.get(f'{HOST}/api/department/4')
            expected_1 = json.loads(response.data)["name"]

            self.assertEqual(expected_1, "Dep_5")

            client.delete(f'{HOST}/api/department/4')

            response = client.delete(f'{HOST}/api/department/4')
            expected = json.loads(response.data)

            self.assertEqual(expected['message'], 'Department not found')

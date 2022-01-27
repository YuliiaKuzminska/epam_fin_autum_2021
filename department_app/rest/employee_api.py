"""
Employee REST API.
"""
from datetime import datetime
from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from department_app.service.department_service import get_department_by_id_service
from department_app.service.employee_service import *

MESSAGE = "message"
EMP_NOT_FOUND = "Employee not found"
DELETED_EMPLOYEE = 'Employee has been successfully deleted'
INCORRECT_DEPARTMENT = "Incorrect department"
INCORRECT_SALARY = "Incorrect salary"
INCORRECT_BIRTHDATE = "Incorrect birthdate"
INCORRECT_DATE = "Incorrect date"
INCORRECT_REQUEST = "Incorrect request"


class EmployeeApi(Resource):
    """
    Employee API.
    """

    def get(self, employee_id):
        """
        GET request handler for employee API.
        :param employee_id: employee id
        :return: employee json representation or error message and status code
        """
        try:
            return jsonify(employee_to_dict(employee_id))
        except AttributeError:
            return make_response({MESSAGE: EMP_NOT_FOUND}, 404)

    def put(self, employee_id):
        """
        PUT request handler for employee API.
        :param employee_id: employee id
        :return: employee json representation or error message and status code
        """
        employee = get_employee_by_id_service(employee_id)
        if not employee:
            return make_response({MESSAGE: EMP_NOT_FOUND}, 404)
        department_name = get_department_by_id_service(employee.department_id).name
        parser = reqparse.RequestParser()
        parser.add_argument('forename')
        parser.add_argument('surname')
        parser.add_argument('birthdate')
        parser.add_argument('salary')
        parser.add_argument('department')
        args = parser.parse_args()
        forename = args['forename'] if args['forename'] else None
        surname = args['surname'] if args['surname'] else None
        department = args['department'] if args['department'] else department_name
        try:
            birthdate = datetime.strptime(args['birthdate'], '%Y/%m/%d') \
                if args['birthdate'] else None
        except ValueError:
            return make_response({MESSAGE: INCORRECT_BIRTHDATE}, 400)
        salary = args['salary'] if args['salary'] else employee.salary
        dep = Department.query.filter_by(name=department).first()
        if not dep:
            return make_response({MESSAGE: INCORRECT_DEPARTMENT}, 400)
        try:
            salary = int(salary)
        except ValueError:
            return make_response({MESSAGE: INCORRECT_SALARY}, 400)
        update_employee_service(
            employee_id=employee_id,
            forename=forename,
            surname=surname,
            birthdate=birthdate,
            salary=salary,
            department_id=dep.id
        )
        return jsonify(employee_to_dict(employee.id), 201)

    def delete(self, employee_id):
        """
        DELETE request handler for employee API.
        :param employee_id: employee id
        :return: message and status code
        """
        if not get_employee_by_id_service(employee_id):
            return make_response({MESSAGE: EMP_NOT_FOUND}, 404)
        delete_employee_service(employee_id)
        return make_response({MESSAGE: DELETED_EMPLOYEE}, 204)


class EmployeeSearchApi(Resource):
    """
    Employee search API.
    """

    def get(self):
        """
        GET request handler for employee search API.
        :return: employee list json representation or error message and status code
        """
        parser = reqparse.RequestParser()
        parser.add_argument('date_from')
        parser.add_argument('date_to')
        args = parser.parse_args()
        try:
            date_from = datetime.strptime(args['date_from'], '%Y/%m/%d')
            date_to = datetime.strptime(args['date_to'], '%Y/%m/%d')
        except (ValueError, TypeError):
            return make_response({MESSAGE: INCORRECT_DATE}, 400)
        employees = get_by_birthdate_service(date_from, date_to)
        return jsonify([employee_to_dict(employee.id) for employee in employees])


class EmployeeListApi(Resource):
    """
    Employee list API.
    """

    def get(self):
        """
        GET request handler for employee list API.
        :return: employee list json representation
        """
        employees = get_all_employees_service()
        return jsonify([employee_to_dict(employee.id) for employee in employees])

    def post(self):
        """
        POST request handler for employee list API.
        :return: employee list json representation or error message and status code
        """
        parser = reqparse.RequestParser()
        parser.add_argument('forename')
        parser.add_argument('surname')
        parser.add_argument('birthdate')
        parser.add_argument('salary')
        parser.add_argument('department')
        args = parser.parse_args()
        forename = args['forename']
        surname = args['surname']
        birthdate = args['birthdate']
        salary = args['salary']
        department = args['department']
        if not (forename and surname and department and birthdate and salary):
            return make_response({MESSAGE: INCORRECT_REQUEST}, 400)
        try:
            birthdate = datetime.strptime(birthdate, '%Y/%m/%d')
        except ValueError:
            return make_response({MESSAGE: INCORRECT_BIRTHDATE}, 400)
        dep = Department.query.filter_by(name=department).first()
        if not dep:
            return make_response({MESSAGE: INCORRECT_DEPARTMENT}, 400)
        try:
            salary = int(salary)
        except ValueError:
            return make_response({MESSAGE: INCORRECT_SALARY}, 400)
        add_employee_service(
            forename=forename,
            surname=surname,
            birthdate=birthdate,
            salary=salary,
            department_id=dep.id
        )
        return jsonify({
            'forename': forename,
            'surname': surname,
            'birthdate': datetime.strftime(birthdate, '%Y-%m-%d'),
            'salary': salary,
            'department': department

        },
            201
        )

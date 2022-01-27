"""
Department REST API.
"""
from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from department_app.service.department_service import *

MESSAGE = "message"
DEP_NOT_FOUND = "Department not found"
DEP_ALREADY_EXIST = "Department already exists"
INCORRECT_REQUEST = "Incorrect request"
DELETED_DEPARTMENT = "Department has been successfully deleted"


class DepartmentApi(Resource):
    """
    Department API.
    """

    def get(self, department_id):
        """
        GET request handler for department API.
        :param department_id: department id
        :return: department json representation or error message and status code
        """
        try:
            department = get_department_by_id_service(department_id)
            return jsonify(departments_to_dict(department.id))
        except AttributeError:
            return make_response({MESSAGE: DEP_NOT_FOUND}, 404)

    def put(self, department_id):
        """
        PUT request handler for department API.
        :param department_id: department id
        :return: department json representation or error message and status code
        """
        if not get_department_by_id_service(department_id):
            return make_response({MESSAGE: DEP_NOT_FOUND}, 404)
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()
        name = args['name']
        if not name:
            return make_response({MESSAGE: INCORRECT_REQUEST}, 400)
        for department in get_all_departments_service():
            if name == department.name:
                return make_response({MESSAGE: DEP_ALREADY_EXIST}, 406)
        update_department_service(department_id=department_id, name=name)
        return jsonify(departments_to_dict(department_id), 201)

    def delete(self, department_id):
        """
        DELETE request handler for department API.
        :param department_id: department id
        :return: message and status code
        """
        if not get_department_by_id_service(department_id):
            return make_response({MESSAGE: DEP_NOT_FOUND}, 404)
        delete_department_service(department_id)
        return make_response({MESSAGE: DELETED_DEPARTMENT}, 204)


class DepartmentListApi(Resource):
    """
    Department list API.
    """

    def get(self):
        """
        GET request handler for department list API.
        :return: department list json representation
        """
        departments = get_all_departments_service()
        return jsonify([departments_to_dict(department.id) for department in departments])

    def post(self):
        """
        POST request handler for department list API.
        :return: department json representation or error message and status code
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()
        name = args['name']
        if not name:
            return make_response({MESSAGE: INCORRECT_REQUEST}, 400)
        for department in get_all_departments_service():
            if name == department.name:
                return make_response({MESSAGE: DEP_ALREADY_EXIST}, 406)
        add_department_service(name)
        department = Department.query.filter_by(name=name).first()
        return jsonify(departments_to_dict(department.id), 201)


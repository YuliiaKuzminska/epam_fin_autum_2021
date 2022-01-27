"""
Department service.
"""
from department_app import db
from department_app.models.department import Department
from department_app.service.employee_service import employee_to_dict

"""
Department services.
"""


def add_department_service(name):
    """
    Adds department to db.
    :param name: department name
    :return: None
    """
    department = Department(name)
    db.session.add(department)
    db.session.commit()


def update_department_service(department_id, name=None):
    """
    Updates department in db.
    :param department_id: department id
    :param name: department name
    :return: None
    """
    if name:
        department = Department.query.get_or_404(department_id)
        department.name = name
        db.session.commit()


def get_department_by_id_service(department_id):
    """
    Returns department from db.
    :param department_id: department_id
    :return: department
    """
    return Department.query.filter_by(id=department_id).first()


def get_department_average_salary_service(department):
    """
    Returns department average salary from db
    :param department: department
    :return: department average salary
    """
    average_salary = 0
    if department.employees:
        for employee in department.employees:
            average_salary += employee.salary
        average_salary /= len(department.employees)
    return round(average_salary, 2)


def get_all_departments_service():
    """
    Returns all departments from db.
    :return: list of all departments
    """
    return Department.query.all()


def delete_department_service(department_id):
    """
    Deletes department from db.
    :param department_id: department id
    :return: None
    """
    department = Department.query.get_or_404(department_id)
    db.session.delete(department)
    db.session.commit()


def departments_to_dict(department_id):
    """
    Returns dictionary representation of department.
    :param department_id: department id
    :return: department dictionary representation
    """
    department = get_department_by_id_service(department_id)
    return {
        'id': department.id,
        'name': department.name,
        'employees_count': len(department.employees),
        'average_salary': get_department_average_salary_service(department),
        'employees': [employee_to_dict(employee.id)
                      for employee in department.employees]
    }

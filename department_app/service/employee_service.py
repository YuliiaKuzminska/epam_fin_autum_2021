"""
Employee service.
"""
from department_app import db
from department_app.models.department import Department
from department_app.models.employee import Employee


def add_employee_service(forename, surname, birthdate, department_id, salary):
    """
    Adds employee to db.
    :param forename: employee first name
    :param surname: employee Surname
    :param birthdate: employee birthdate
    :param salary: employee salary
    :param department_id: employee department id
    :return: None
    """
    employee = Employee(
        forename=forename,
        surname=surname,
        birthdate=birthdate,
        salary=salary,
        department=department_id
    )
    db.session.add(employee)
    db.session.commit()


def update_employee_service(employee_id, forename=None, surname=None, birthdate=None, salary=None, department_id=None):
    """
    Updates employee into db.
    :param employee_id: employee id
    :param forename: employee first name
    :param surname: employee Surname
    :param birthdate: employee birthdate
    :param salary: employee salary
    :param department_id: employee department id
    :return: None
    """
    employee = Employee.query.get_or_404(employee_id)
    if forename:
        employee.forename = forename
    if surname:
        employee.surname = surname
    if birthdate:
        employee.birthdate = birthdate
    if salary:
        employee.salary = salary
    if department_id:
        employee.department_id = department_id
    db.session.add(employee)
    db.session.commit()


def get_employee_by_id_service(employee_id):
    """
    Returns employee from db.
    :param employee_id: employee id
    :return: employee
    """
    return Employee.query.filter_by(id=employee_id).first()


def get_by_birthdate_service(date_from, date_to):
    """
    Returns all employees with birthdate in mentioned period from db.
    :param date_from: start_date
    :param date_to: end_date
    :return: list of all employees with birthdate in mentioned period
    """
    return Employee.query.filter(Employee.birthdate.between(date_from, date_to)).all()


def get_all_employees_service():
    """
    Returns all employees from db.
    :return: list of all employees
    """
    return Employee.query.all()


def delete_employee_service(employee_id):
    """
    Deletes employee in db.
    :param employee_id: employee id
    :return: None
    """
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()


def employee_to_dict(employee_id):
    """
    Returns employee dictionary representation.
    :param employee_id: employee id
    :return: employee dictionary representation
    """
    employee = get_employee_by_id_service(employee_id)
    return {
        'id': employee.id,
        'forename': employee.forename,
        'surname': employee.surname,
        'birthdate': employee.birthdate.strftime('%Y-%m-%d'),
        'salary': employee.salary,
        'department': Department.query.get_or_404(employee.department_id).name
    }


def get_all_employees_for_department(department_id):
    """
    Returns all employees in the department from database.
    :param department_id: department id
    :return: list of all employees in the department
    """
    return Employee.query.filter_by(department_id=department_id).all()

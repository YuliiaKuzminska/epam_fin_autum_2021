"""
Defines employee web application view.
"""
from datetime import datetime
import requests
from flask import redirect, render_template, url_for
from department_app import app
from config import HOST
from department_app.views.form import SearchForm, EmployeeForm


@app.route('/employees/', methods=['GET'])
def show_employees():
    """
    Returns rendered template to show all employees.
    :return: rendered template to show all employees
    """
    url = f'{HOST}api/employees'
    employees = requests.get(url).json()
    return render_template('employees.html', employees=employees)


@app.route('/employee/<int:employee_id>', methods=['GET'])
def show_employee(employee_id):
    """
    Returns rendered template to show employee.
    :param employee_id: employee id
    :return: rendered template to show employee
    """
    url = f'{HOST}api/employee/{employee_id}'
    employee = requests.get(url).json()
    return render_template('employee.html', employee=employee)


@app.route('/search/', methods=['GET', 'POST'])
def search():
    """
    Returns rendered template to search employees.
    :return: rendered template to search employees
    """
    form = SearchForm()
    if form.validate_on_submit():
        date_from = datetime.strftime(form.date_from.data, '%Y/%m/%d')
        date_to = datetime.strftime(form.date_to.data, '%Y/%m/%d')
        url = f'{HOST}api/employees/search'
        querystring = {'date_from': date_from, 'date_to': date_to}
        employees = requests.get(url, params=querystring).json()
        return render_template('employees.html', employees=employees)
    return render_template('search.html', form=form)


@app.route('/employees/add/', methods=['GET', 'POST'])
def add_employee():
    """
    Returns rendered template to add_department employee.
    :return: rendered template to add_department employee
    """
    EmployeeForm.update_departments_list()
    form = EmployeeForm()
    if form.validate_on_submit():
        url = f'{HOST}api/employees'
        requests.post(url, data={
            'forename': form.forename.data,
            'surname': form.surname.data,
            'birthdate': datetime.strftime(form.birthdate.data, '%Y/%m/%d'),
            'salary': form.salary.data,
            'department': form.department.data,
        }).json()
        return redirect(url_for('show_employees'))
    return render_template('add_employee.html', form=form)


@app.route('/employees/edit/<int:employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    """
    Returns rendered template to edit employee.
    :param employee_id: employee id
    :return: rendered template to edit employee
    """
    url = f'{HOST}api/employee/{employee_id}'
    employee = requests.get(url).json()
    EmployeeForm.update_departments_list()
    form = EmployeeForm(obj=employee)
    if form.validate_on_submit():
        url = f'{HOST}api/employee/{employee_id}'
        requests.put(url, data={
            'forename': form.forename.data,
            'surname': form.surname.data,
            'birthdate': datetime.strftime(form.birthdate.data, '%Y/%m/%d'),
            'salary': form.salary.data,
            'department': form.department.data
        }).json()
        return redirect(url_for('show_employees'))
    form.forename.data = employee['forename']
    form.surname.data = employee['surname']
    form.birthdate.data = datetime.strptime(employee['birthdate'], '%Y-%m-%d')
    form.salary.data = employee['salary']
    form.department.data = employee['department']
    return render_template('edit_employee.html', form=form, employee=employee)


@app.route('/employees/delete/<int:employee_id>', methods=['GET'])
def delete_employee(employee_id):
    """
    Returns rendered template to delete employee.
    :param employee_id: employee id
    :return: rendered template to delete employee
    """
    url = f'{HOST}api/employee/{employee_id}'
    requests.delete(url)
    return redirect(url_for('show_employees'))

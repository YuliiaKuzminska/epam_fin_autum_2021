import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired

from config import HOST


class DepartmentForm(FlaskForm):
    """
    User form to manage departments.
    """
    name = StringField('Department name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SearchForm(FlaskForm):
    """
    User form to search employees.
    """
    date_from = DateField('Birthdate From', validators=[DataRequired()])
    date_to = DateField('Birthdate To', validators=[DataRequired()]) if date_from is not None else date_from
    submit = SubmitField('Submit')


class EmployeeForm(FlaskForm):
    """
    User form to manage employees.
    """

    forename = StringField('Forename', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    birthdate = DateField('Birthdate', validators=[DataRequired()])
    salary = IntegerField('Salary', validators=[DataRequired()])
    department = SelectField(choices=[''])
    submit = SubmitField('Submit')

    @classmethod
    def update_departments_list(cls):
        """
        Updates department list from database.
        :return: None
        """
        url = f'{HOST}api/departments'
        departments = requests.get(url).json()
        cls.department = SelectField(choices=[department['name'] for department in departments])

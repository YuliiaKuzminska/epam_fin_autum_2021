"""
Employee model.
"""
from department_app import db


class Employee(db.Model):
    """
    Employee model.
    """

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    forename = db.Column(db.String(32), nullable=False)
    surname = db.Column(db.String(32), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Integer)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))

    def __init__(self, forename, surname, birthdate, salary=0, department=None,):
        """
        Constructor.
        :param forename: employee first name
        :param surname: employee Surname
        :param birthdate: employee birthdate
        :param salary: employee salary
        :param department: employee department id
        """
        self.forename = forename
        self.surname = surname
        self.birthdate = birthdate
        self.salary = salary
        self.department_id = department

    def __repr__(self):
        """
        :return: employee string representation
        """
        return f'Employee: {self.forename}, ' \
               f'{self.surname}, ' \
               f'{self.birthdate}, ' \
               f'{self.salary}'\
               f'{self.department}, '

    def __eq__(self, other):
        """
        :return: compares two employees and returns bool
        """
        return self.forename == other.forename \
               and self.surname == other.surname \
               and self.birthdate == other.birthdate \
               and self.salary == other.salary

    def __hash__(self):
        """
        :return: hash sum of the employee
        """
        return hash((self.forename, self.surname, self.birthdate, self.salary))
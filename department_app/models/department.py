"""
Department model.
"""
from department_app import db


class Department(db.Model):
    """
    Department model.
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, unique=True)
    employees = db.relationship(
        'Employee', cascade="all,delete", backref=db.backref('department', lazy=True), lazy=True
    )

    def __init__(self, name, employees=None):
        """
        Constructor.
        :param name: department name
        :param employees: department employees
        """
        self.name = name
        self.employees = employees if employees else list()

    def __repr__(self):
        """
        :return: department string representation
        """
        return f'Department: {self.name}'

    def __eq__(self, other):
        """
        :return: compares two departments and returns bool
        """
        return self.name == other.name

    def __hash__(self):
        """
        :return: hash sum of the department
        """
        return hash(self.name)


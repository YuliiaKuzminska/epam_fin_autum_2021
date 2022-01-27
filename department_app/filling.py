"""
Filling db with/
"""
from datetime import date
from department_app import db
from department_app.models.department import Department
from department_app.models.employee import Employee


def create_objects():
    """
    Creates departments and employees that will add_department to db.
    :return: None
    """
    dep_1 = Department('Sales Department')
    dep_2 = Department('Development Department')
    dep_3 = Department('Testing Department')

    empl_1 = Employee('David', 'Campbel', date(2001, 1, 30), 15000)
    empl_2 = Employee('John', 'Duncan', date(2002, 1, 30), 13000)
    empl_3 = Employee('Fill', 'Gaspacho', date(2003, 1, 30), 14000)
    empl_4 = Employee('Oko', 'Dzen', date(2004, 1, 30), 7500)
    empl_5 = Employee('Bill', 'Murray', date(2005, 1, 30), 9900)
    empl_6 = Employee('Lena', 'Grasp', date(2006, 1, 30), 11100)
    empl_7 = Employee('Roman', 'Polansky', date(2007, 1, 30), 12800)
    empl_8 = Employee('Kate', 'Varus', date(2008, 1, 30), 16500)
    empl_9 = Employee('Abu', 'Silpo', date(2009, 1, 30), 8800)

    return (dep_1, dep_2, dep_3),\
           (empl_1, empl_2, empl_3, empl_4, empl_5, empl_6, empl_7,empl_8, empl_9)


def filling():
    """
    Adding departments and employees to the database.
    :return: A tuple of tuples of departments and employees.
    """
    db.drop_all()
    db.create_all()

    creates_objects = create_objects()
    dep_1, dep_2, dep_3 = creates_objects[0]

    dep_1.employees = [i for i in creates_objects[1][:3]]
    dep_2.employees = [i for i in creates_objects[1][3:6]]
    dep_3.employees = [i for i in creates_objects[1][6:]]

    db.session.add_all((dep_1, dep_2, dep_3))

    db.session.commit()
    db.session.close()

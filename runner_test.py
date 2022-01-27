"""
Initializes tests.
"""
import unittest
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import LocalTestConfiguration
from department_app.filling import *
from department_app.tests.department import DepartmentModelTests
from department_app.tests.department_service import DepartmentServiceTests
from department_app.tests.department_api import DepartmentApiTests
from department_app.tests.department_view import DepartmentViewTests
from department_app.tests.employee import EmployeeModelTests
from department_app.tests.employee_service import EmployeeServiceTests
from department_app.tests.employee_api import EmployeeApiTests
from department_app.tests.employee_view import EmployeeViewTests


if __name__ == '__main__':
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = 'SECRET_KEY'
    app.config.from_object(LocalTestConfiguration)
    api = Api(app)
    db = SQLAlchemy(app)
    app_context = app.app_context()
    app_context.push()
    filling()

    appTestSuite = unittest.TestSuite()
    appTestSuite.addTest(unittest.makeSuite(DepartmentModelTests))
    appTestSuite.addTest(unittest.makeSuite(DepartmentServiceTests))
    appTestSuite.addTest(unittest.makeSuite(DepartmentApiTests))
    appTestSuite.addTest(unittest.makeSuite(DepartmentViewTests))
    appTestSuite.addTest(unittest.makeSuite(EmployeeModelTests))
    appTestSuite.addTest(unittest.makeSuite(EmployeeServiceTests))
    appTestSuite.addTest(unittest.makeSuite(EmployeeApiTests))
    appTestSuite.addTest(unittest.makeSuite(EmployeeViewTests))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(appTestSuite)

    db.session.remove()
    db.drop_all()

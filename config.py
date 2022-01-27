import os
from dotenv import load_dotenv

load_dotenv()
# user = os.environ.get('MYSQL_USER')
# password = os.environ.get('MYSQL_PASSWORD')
# server = os.environ.get('MYSQL_SERVER')
# database = os.environ.get('MYSQL_DATABASE')

user = 'root'
password = 'root'
server = '127.0.0.1'
database = 'epam123'
base_direction = os.path.abspath(os.path.dirname(__file__))
local_test_db_location = os.path.join(base_direction, 'department_app', 'db', 'local_database.db')

HOST = 'http://127.0.0.1:5000/'


class BaseConfiguration:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False


class Configuration(BaseConfiguration):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{user}:{password}@{server}/{database}'


class LocalTestConfiguration(BaseConfiguration):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{local_test_db_location}'



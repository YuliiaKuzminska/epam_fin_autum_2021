from setuptools import setup, find_packages

setup(
    project_name="Department Application",
    version="0.1",
    project_description="A simple CRUD web application for manage departments and employees",
    url="https://github.com/YuliiaKuzminska/epam_fin_autum_2021",
    author="Yulii Kuzminska",
    email="yuliia.nikolaevna86@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask=2.0.2",
        "Flask-Bcrypt=0.7.1",
        "Flask-Login=0.5.0",
        "Flask-Mail=0.9.1",
        "Flask-Migrate=3.1.0",
        "Flask-RESTful=0.3.9",
        "Flask-SQLAlchemy=2.5.1",
        "Flask-WTF=1.0.0",
        "Jinja2=3.0.3",
        "SQLAlchemy=1.4.27",
        "SQLAlchemy-Utils=0.37.9",
        "Werkzeug=2.0.2",
        "WTForms=3.0.0",
        "WTForms-SQLAlchemy=0.3",
    ]
)

# Task 1
# Use SQLalchemy to create classes, and map those to tables in hr.db,
# which we used in previous lessons for homework tasks.

# Task 2
# Use SQLalchemy for querying
# Use your implementation of SQLalchemy classes from the previous task to perform queries from SQL homework tasks
# (Lessons 37-38). Pick 10+ queries from the previous homework and create separate functions.

# Task 3
# Write tests for functions
# Write tests for your solution for Task 2, using pytests or unittest modules.

from sqlalchemy import create_engine, Column, String, Integer, Numeric, MetaData, func, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///hr.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Employees(Base):
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    hire_date = Column(Integer)
    job_id = Column(String)
    salary = Column(Integer)
    commission_pct = Column(Integer)
    manager_id = Column(Integer)
    department_id = Column(Integer)
    Avg_Salary = Column(Integer)


class Departments(Base):
    __tablename__ = 'departments'
    department_id = Column(Integer, primary_key=True)
    depart_name = Column(String)
    manager_id = Column(Integer)
    location_id = Column(Integer)

class Jobs(Base):
    __tablename__ = 'jobs'
    job_id = Column(Integer, primary_key=True)
    job_title = Column(String)
    min_salary = Column(Numeric)
    max_salary = Column(Numeric)


class Locations(Base):
    __tablename__ = 'locations'
    location_id = Column(Integer, primary_key=True)
    street_address = Column(String)
    postal_code = Column(String)
    city = Column(String)
    state_province = Column(String)
    country_id = Column(String)


# display the first name, last name, department number, and department name for each employee
def get1():
    for first_name, last_name, salary, department_id, depart_name in session.query(
            Employees.first_name, Employees.last_name,
            Employees.salary, Employees.department_id, Departments.depart_name)\
            .join(Departments, Employees.department_id == Departments.department_id):
        print(first_name, last_name, salary, department_id, depart_name)


# SELECT first_name, last_name FROM employees
def get2():
    for employee in session.query(Employees.first_name, Employees.last_name):
        print(employee.first_name, employee.last_name)


# SELECT DISTINCT department_id FROM employees
def get3():
    employees = session.query(Employees.department_id).distinct()
    for employee in employees:
        print(employee.department_id)


# SELECT first_name, last_name, email, phone_number,
#         hire_date, salary  FROM employees ORDER BY first_name
def get4():
    employees = session.query(Employees).order_by(Employees.first_name)
    for employee in employees:
        print(f'{employee.first_name} / {employee.last_name} / {employee.email} / '
              f'{employee.phone_number} / {employee.hire_date} / {employee.salary}')


# SELECT first_name, last_name, salary, salary*0.12 as PF  FROM employees
def get5():
    employees = session.query(Employees.first_name, Employees.last_name, (Employees.salary * 0.12).label('PF'))
    for employee in employees:
        print(f'{employee.first_name} / {employee.last_name} / {employee.PF} / ')


# SELECT MIN(salary), MAX(salary) FROM employees
def get6():
    employees = session.query(func.min(Employees.salary).label('min_sal'), func.max(Employees.salary).label('max_sal'))
    for employee in employees:
        print(f'minimal salary: {employee.min_sal} maximal salary: {employee.max_sal}')


# write a query in SQL to display the full name (first and last name),
# and salary of those employees who work in any department located in London
def get7():
    for first_name, last_name, city in session.query(
            Employees.first_name, Employees.last_name, Locations.city) \
            .join(Departments, Employees.department_id == Departments.department_id)\
            .join(Locations, Locations.location_id == Departments.location_id).filter(Locations.city == 'London'):
        print(first_name, last_name, city)


# Roma, Venice, Seattle, Singapore etc...
def get7_1(dest='London'):
    employees = session.query(Employees.first_name, Employees.last_name, Locations.city) \
            .join(Departments, Employees.department_id == Departments.department_id)\
            .join(Locations, Locations.location_id == Departments.location_id).filter(Locations.city == dest)
    for employee in employees:
        print(f'First name: {employee.first_name} * Last name: {employee.last_name} * City: {employee.city}')


# write a query in SQL to display the first name, last name, department number, and department name,
# for all employees for departments 80 or 40
def get8():
    employees = session.query(
        Employees.first_name, Employees.last_name, Departments.department_id, Departments.depart_name)\
        .join(Departments, Employees.department_id == Employees.department_id)\
        .filter(or_(Departments.department_id == 80, Departments.department_id == 40))
    for employee in employees:
        print(f'First name: {employee.first_name} * Last name: {employee.last_name} '
              f'* Department ID: {employee.department_id} * Department Name: {employee.depart_name}')


# write a query in SQL to display the job title, full name (first and last name ) of the employee,
# and the difference between the maximum salary for the job and the salary of the employee
def get9():
    employees = session.execute('''SELECT employees.first_name, employees.last_name, jobs.job_title , 
    jobs.max_salary-employees.salary as dif FROM employees LEFT JOIN jobs ON employees.job_id=jobs.job_id ''')
    for employee in employees:
        print(f'First name: {employee.first_name} * Last name: {employee.last_name} '
              f'* Job title: {employee.job_title} * Difference on salary: {employee.dif}')


# write a query in SQL to display the job title and the average salary of employees
def get10():
    jobs = session.query(Jobs.job_title, func.round((Jobs.max_salary - Jobs.min_salary)/2).label('AVG'))
    for job in jobs:
        print(job)


get10()


## need meta

# meta = MetaData()
# users_table = Table('users', meta,
#     Column('id', Integer, primary_key=True),
#     Column('name', String(50))
# )
# engine = create_engine('sqlite:///file.db')
# meta.bind = engine


# def get2():
#    with engine.connect() as connection:
#        result = connection.execute(Employees.select())
#        for row in result:
#            print(row)


#    def __init__(self, name, fullname, password):
#        self.name = name
#        self.fullname = fullname
#        self.password = password

#    def __repr__(self):
#        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)
# session.commit()
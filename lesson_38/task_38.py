# write a query in SQL to display the first name of all employees including the first name of their manager





# write a query in SQL to display the department name and the number of employees in each department

import sqlite3
try:
    conn = sqlite3.connect('hr.db')
except Exception:
    print('OOps')
# write a query in SQL to display the first name, last name, department number, and department name for each employee


def get_data1():
    cursor = conn.cursor()
    q = cursor.execute('''SELECT employees.first_name, employees.last_name, departments.department_id, 
        departments.depart_name FROM employees LEFT JOIN departments ON 
        departments.department_id=employees.department_id''')
    for row in q:
        print(row)
    q.close()

# write a query in SQL to display the first and last name, department, city, and state province for each employee


def get_data2():
    cursor = conn.cursor()
    q = cursor.execute('''SELECT employees.first_name, employees.last_name, 
        departments.depart_name, locations.city, locations.state_province FROM employees LEFT JOIN departments ON 
        departments.department_id=employees.department_id INNER JOIN locations ON locations.location_id=departments.location_id''')
    for row in q:
        print(row)
    q.close()
# write a query in SQL to display the first name, last name, department number, and department name,
# for all employees for departments 80 or 40


def get_data3():
    cursor = conn.cursor()
    q = cursor.execute('''SELECT employees.first_name, employees.last_name,departments.department_id, 
        departments.depart_name  FROM employees LEFT JOIN departments ON 
        departments.department_id=employees.department_id WHERE departments.department_id=80 OR departments.department_id=40''')
    for row in q:
        print(row)
    q.close()
# write a query in SQL to display all departments including those where does not have any employee


def get_data4():
    cursor = conn.cursor()
    q = cursor.execute('''SELECT depart_name  FROM departments ''')
    for row in q:
        print(row)
    q.close()
# write a query in SQL to display the job title, full name (first and last name ) of the employee,
# and the difference between the maximum salary for the job and the salary of the employee


def get_data5():
    cursor = conn.cursor()
    q = cursor.execute('''SELECT employees.first_name, employees.last_name, jobs.job_title , jobs.max_salary-employees.salary
        FROM employees LEFT JOIN jobs ON 
        employees.job_id=jobs.job_id ''')
    for row in q:
        print(row)
    q.close()
# write a query in SQL to display the job title and the average salary of employees


def get_data6():
    cursor = conn.cursor()
    q = cursor.execute('''SELECT job_title, max_salary-min_salary/2  FROM jobs ''')
    for row in q:
        print(row)
    q.close()
# write a query in SQL to display the full name (first and last name),
# and salary of those employees who work in any department located in London

def get_data7():
    cursor = conn.cursor()
    q = cursor.execute('''SELECT employees.first_name, employees.last_name, employees.salary, locations.city 
    FROM employees LEFT JOIN departments ON 
    departments.department_id=employees.department_id LEFT JOIN locations ON locations.location_id=departments.location_id 
    WHERE locations.city='London' ''')
    for row in q:
        print(row)
    q.close()


get_data7()


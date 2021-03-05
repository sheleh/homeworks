# As a solution to HW, create a file named: task2.sql with all SQL queries:
#
# write a query to display the names (first_name, last_name) using alias name
# "First Name", "Last Name" from the table of employees;

# write a query to get the unique department ID from the employee table

# write a query to get all employee details from the employee table ordered by first name, descending

# write a query to get the names (first_name, last_name), salary, PF of all the employees
# (PF is calculated as 12% of salary)

# write a query to get the maximum and minimum salary from the employees table

# write a query to get a monthly salary (round 2 decimal places) of each and every employee

import sqlite3
try:
    conn = sqlite3.connect('hr.db')
except Exception:
    print('OOps')


def show_all():
    try:
        cursor = conn.cursor()
        q = cursor.execute('''SELECT first_name, last_name FROM employees''')
    except sqlite3.OperationalError:
        print('database not found')
    else:
        for row in q:
            print(row)
        q.close()


def get_id():
    try:
        cursor = conn.cursor()
        q = cursor.execute('''SELECT DISTINCT department_id FROM employees ''')
    except sqlite3.OperationalError:
        print('database not found')
    else:
        for row in q:
            print(row)
        q.close()


def get_employee_details():
    try:
        cursor = conn.cursor()
        q = cursor.execute('''SELECT first_name, last_name, email, phone_number, 
        hire_date, salary  FROM employees ORDER BY first_name''')
    except sqlite3.OperationalError:
        print('database not found')
    else:
        for row in q:
            print(row)
        q.close()


def get_pf():
    try:
        cursor = conn.cursor()
        q = cursor.execute('''SELECT first_name, last_name, salary, salary*0.12 as PF  FROM employees''')
    except sqlite3.OperationalError:
        print('database not found')
    else:
        for row in q:
            print(row)
        q.close()


def get_min_max_salary():
    try:
        cursor = conn.cursor()
        q = cursor.execute('''SELECT MIN(salary), MAX(salary) FROM employees''')
    except sqlite3.OperationalError:
        print('database not found')
    else:
        print(q.fetchone())
        q.close()


def get_monthly_salary():
    try:
        cursor = conn.cursor()
        q = cursor.execute('''SELECT last_name, salary/12,2 FROM employees''')
    except sqlite3.OperationalError:
        print('database not found')
    else:
        for row in q:
            print(row)
        q.close()
        cursor = conn.cursor()
        q2 = cursor.execute('''SELECT round(AVG(salary)/12,2) FROM employees''')  # можно также в try обернуть
        print(f'Average monthly salary of all employees is : {q2.fetchone()}')


if __name__ == '__main__':
    print('==names and last names==')
    show_all()
    print('==ids==')
    get_id()
    print('==employees details==')
    get_employee_details()
    print('==personal fees==')
    get_pf()
    print('==minimum and maximum salaries==')
    get_min_max_salary()
    print('==monthly salary==')
    get_monthly_salary()
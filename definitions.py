import os
import sqlite3

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) #root
CONNECTION = sqlite3.connect('employees.db')
CURSOR = CONNECTION.cursor()

CREATE_EMPLOYEES = os.path.join(ROOT_DIR, 'sql_scripts/create_employees.sql')  
INSERT_EMPLOYEES = os.path.join(ROOT_DIR, 'sql_scripts/insert_employees.sql')  

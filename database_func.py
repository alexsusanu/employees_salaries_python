from definitions import CONNECTION, CURSOR

def read_sql_script(sql_file, *args)
    f = open('sql_scripts/create.sql', 'r')
    sql_file = f.read()
    f.close()
    CURSOR.execute(sql_file, *args)




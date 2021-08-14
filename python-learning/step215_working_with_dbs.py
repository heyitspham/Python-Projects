
import sqlite3


conn = sqlite3.connect('step215_working_with_dbs.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        persons_fname TEXT, \
        persons_lname TEXT, \
        persons_email TEXT \
        )")
    conn.commit()
conn.close()

"""
conn = sqlite3.connect('step215_working_with_dbs.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(persons_fname, persons_lname, persons_email) \
        VALUES \
        (?, ?, ?)", \
        ('Bob', 'Smith', 'bsmith@gmail.com')
        )
    cur.execute("INSERT INTO tbl_persons(persons_fname, persons_lname, persons_email) \
        VALUES \
        (?, ?, ?)", \
        ('Sarah', 'Jones', 'sjones@gmail.com')
        )
    cur.execute("INSERT INTO tbl_persons(persons_fname, persons_lname, persons_email) \
        VALUES \
        (?, ?, ?)", \
        ('Sally', 'May', 'sallymay@gmail.com')
        )
    cur.execute("INSERT INTO tbl_persons(persons_fname, persons_lname, persons_email) \
        VALUES \
        (?, ?, ?)", \
        ('Kevin', 'Bacon', 'kbacon@gmail.com')
        )
    conn.commit()
conn.close()
"""

conn = sqlite3.connect('step215_working_with_dbs.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT persons_fname, persons_lname, persons_email FROM tbl_persons WHERE persons_fname = 'Sarah'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0], item[1], item[2])
    print(msg)
    

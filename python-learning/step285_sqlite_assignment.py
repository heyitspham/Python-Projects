"""
# PART 1
import sqlite3
connection = sqlite3.connect("step285_sqlite_assignment.db")
c = connection.cursor()
c.execute("CREATE TABLE tbl_people (FirstName TEXT, LastName TEXT, Age INT)")

# PART2
c.execute("INSERT INTO tbl_people VALUES ('Ron', 'Obvious', 42)")
connection.commit()
connection = sqlite3.connect(':memory:')
c.execute("DROP TABLE IF EXISTS tbl_people")

# PART 3
connection.close()
with sqlite3.connect("step285_sqlite_assignment.db") as connection:
    # Perform any SQL operations using connection here

# PART 4
with sqlite3.connect("step285_sqlite_assignment.db") as connection:
    c = connection.cursor()
            c.executescript(""DROP TABLE IF EXISTS tbl_people;
                            CREATE TABLE tbl_people (FirstName TEXT, LastName TEXT, Age INT);
                            INSERT INTO tbl_people VALUES ('Ron', 'Obvious', '42');
                            "")
peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
c.executemany("INSERT INTO tbl_people VALUES (?, ?, ?)", peopleValues)

# PART 5
import sqlite3

# Get Personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))

# Execute insert statement for supplied person data
with sqlite3.connect('step285_sqlite_assignment.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO tbl_people VALUES ('"+ firstName +"', '"+ lastName +"', " +str(age) +")"
    c.execute(line)

# PART 6
import sqlite3

# Get Personal data from user and insert into a tuple
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)

# Execute insert statement for supplied person data
with sqlite3.connect('step285_sqlite_assignment.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO tbl_people VALUES (?, ?, ?)", personData)
    c.execute("UPDATE tbl_people SET Age=? WHERE firstName=? AND lastName=?",
              (45, 'Luigi', 'Vercotti'))

# PART 7
import sqlite3

with sqlite3.connect('step285_sqlite_assignment.db') as connection:
    c = connection.cursor()
    c.execute("SELECT firstName, lastName FROM tbl_people WHERE Age > 30")
    for row in c.fetchall():
        print (row)
"""

# PART 8
import sqlite3

with sqlite3.connect('step285_sqlite_assignment.db') as connection:
    c = connection.cursor()
    c.execute("SELECT firstName, lastName FROM tbl_people WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)


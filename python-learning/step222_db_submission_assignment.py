import sqlite3


conn = sqlite3.connect('step222_db_submission_assignment.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList \
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        fileList_fileName TEXT)"
        )
    conn.commit()
conn.close()


conn = sqlite3.connect('step222_db_submission_assignment.db')
# Tuple of names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
# Loop through each object in the tuple to find the names that end in y.
for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            # The value for each row will be one name out of the tuple therefore (x,)
            # will denote a one element tuple for each name ending with 'txt'.
            cur.execute("INSERT INTO tbl_fileList (fileList_fileName) VALUES (?)", (x,))
            print(x)
conn.close()

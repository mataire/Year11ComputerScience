import sqlite3

conn = sqlite3.connect("players")
cursor = conn.cursor()

sqlCommand = """

        CREATE TABLE if not exists tblplayers
        (idnum INTEGER,
        firstname TEXT,
        surname TEXT,
        age INTEGER,
        primary key (idnum)
        ) """

cursor.execute(sqlCommand)
print("Player Table Created ")
conn.commit() #writing to hard disk
conn.close() #closes database


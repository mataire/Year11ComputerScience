import sqlite3

conn = sqlite3.connect("players")
cursor = conn.cursor()

more = True

while more:
    players = []
    idnum= int(input("ID Number "))
    firstname = input("Enter Firstname ")
    surname = input("Enter Surname ")
    age = int(input("Entrer Age "))
    players.append(idnum)
    players.append(firstname)
    players.append(surname)
    players.append(age)
    cursor.execute("INSERT INTO tblplayers VALUES (?,?,?,?)", players)
    
    print("Record Inserted ")
    conn.commit()
    mp = input("More Players? y/n ").lower()
    if mp == "n":
        more = False
conn.close()
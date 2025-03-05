import sqlite3

conn = sqlite3.connect("starfleet.db")
cursor = conn.cursor()
# task1
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
""")
# task2
cursor.executemany("""
    INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

# task3
cursor.execute("""
    UPDATE Roster
    SET Name = 'Ezri Dax'
    WHERE Name = 'Jadzia Dax'
""")

# task4
cursor.execute("""
    SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
""")
bajorans = cursor.fetchall()

for name, age in bajorans:
    print(f"Name: {name}, Age: {age}")

conn.commit()
conn.close()

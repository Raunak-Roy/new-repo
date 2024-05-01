import sqlite3
conn = sqlite3.connect("sqlite3.db")

conn.execute('''
            craete table student(
                st_id INT PRIMARY KEY,
                name VARCHAR(20),
                class VARCHAR(10)
                )
''')

conn.close()

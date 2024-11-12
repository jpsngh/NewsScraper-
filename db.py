
import sqlite3

# Connect to SQLite and create a database file
conn = sqlite3.connect('news.db')

# Create a cursor object using the connection
cursor = conn.cursor()

# Create a new table named 'friends'
cursor.execute('''
    CREATE TABLE friends (
        ID    INTEGER,
        name TEXT,
        age INTEGER,
        hobby TEXT,
        phone TEXT
    )
''')

# Save (commit) the changes
conn.commit()

# Close the connection to the database
conn.close()
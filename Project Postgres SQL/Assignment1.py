import sqlite3

# Connect to the SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Create the "Ages" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ages (
        name VARCHAR(128),
        age INTEGER
    )
''')

# Make sure the table is empty
cursor.execute('DELETE FROM Ages')

# Insert rows into the "Ages" table
cursor.execute("INSERT INTO Ages (name, age) VALUES ('Mara', 28)")
cursor.execute("INSERT INTO Ages (name, age) VALUES ('Otto', 33)")
cursor.execute("INSERT INTO Ages (name, age) VALUES ('Fyn', 31)")
cursor.execute("INSERT INTO Ages (name, age) VALUES ('Neshawn', 17)")

# Run the SQL command to get the hexadecimal values and find the first row
cursor.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X LIMIT 1")
result = cursor.fetchone()

# Display the output
if result:
    print("The first row in the resulting record set:", result[0])

# Commit the changes and close the connection
conn.commit()
conn.close()
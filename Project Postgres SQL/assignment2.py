import sqlite3

# Function to create or connect to the database
def create_connection():
    conn = sqlite3.connect('email_counts.sqlite')
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER)''')
    conn.commit()
    return conn

# Function to update or insert counts into the database
def update_counts(conn, org):
    cur = conn.cursor()
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

    conn.commit()

# Main program
file_name = input('Enter file name: ')
if len(file_name) < 1:
    file_name = 'mbox.txt'

try:
    file_handle = open(file_name)
except FileNotFoundError:
    print('File not found:', file_name)
    quit()

conn = create_connection()

for line in file_handle:
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        domain = email.split('@')[1]
        update_counts(conn, domain)

# Retrieve and print the counts
cur = conn.cursor()
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC')

print('Counts:')
for row in cur.fetchall():
    print(row[0], row[1])

# Close the database connection
conn.close()

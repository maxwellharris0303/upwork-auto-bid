import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="songs_db"
)

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM feedback")

# Fetch and print the data
rows = cursor.fetchall()
for row in rows:
    print(row)

# Insert a new record
sql = "INSERT INTO feedback (track_id, feedback) VALUES (%s, %s)"
values = ("sdfwer342w3r", 3.1)
cursor.execute(sql, values)
conn.commit()

print(f"{cursor.rowcount} record(s) inserted")

# Close the cursor and connection
cursor.close()
conn.close()

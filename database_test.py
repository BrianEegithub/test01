import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')
conn.commit()

# Function to add a user
def add_user(name, age):
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    print(f"User {name} added.")

# Function to get all users
def get_users():
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    print("All users:")
    for row in rows:
        print(row)

# Function to update a user's age by name
def update_user(name, new_age):
    cursor.execute('UPDATE users SET age = ? WHERE name = ?', (new_age, name))
    conn.commit()
    print(f"User {name} updated.")

# Function to delete a user by name
def delete_user(name):
    cursor.execute('DELETE FROM users WHERE name = ?', (name,))
    conn.commit()
    print(f"User {name} deleted.")

# Example usage
add_user("Alice", 30)
add_user("Bob", 24)
get_users()
update_user("Alice", 31)
delete_user("Bob")
get_users()

# Close the database connection
conn.close()

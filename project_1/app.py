import sqlite3
 
 # Connect to database
connection = sqlite3.connect('users.db')
cursor = connection.cursor()
 
 # Creating a table
cursor.executescript('''
     CREATE TABLE IF NOT EXISTS users(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         username TEXT UNIQUE NOT NULL,
         password TEXT NOT NULL
     );
     
     CREATE TABLE IF NOT EXISTS tasks(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         description TEXT NOT NULL,
         user_id INTEGER NOT NULL,
         FOREIGN KEY (user_id) REFERENCES users(id)
     );
 ''')
 
 
 
try:
    username = "feliko"
    password = "nguchi"
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    connection.commit()
 
    print("User added successfully")
except sqlite3.IntegrityError:
    print("User already exists")
 
 
connection.commit()
connection.close()
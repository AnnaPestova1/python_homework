import sqlite3

# **Task 1: Create a New SQLite Database**

conn = sqlite3.connect("../db/magazines.db")
print("Database created and connected successfully.")

# **Task 3: Populate Tables with Data**
conn.execute("PRAGMA foreign_keys = 1")

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO Publishers (name) VALUES (?)", (name, ))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

   

def add_magazine(cursor, name, publisher_name):
    cursor.execute("SELECT * FROM Publishers WHERE name = ?", (publisher_name,)) 
    results = cursor.fetchall()
    if len(results) > 0:
        publisher_id = results[0][0]
    else:
        print(f"There was no publisher named {publisher_name}.")
        return
    try:
        cursor.execute("INSERT INTO Magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_subscriber(cursor, name, address):
    cursor.execute("SELECT * FROM Subscribers WHERE name = ? AND address=?", (name,address))
    results = cursor.fetchall()
    if len(results) == 0:
        cursor.execute("INSERT INTO Subscribers (name, address) VALUES (?, ?)", (name, address))
    else:
        print(f"subscriber {name} with the address {address} is already in the database.")
        return

    
        

def add_subscription(cursor, expiration_date, subscriber_name, magazine_name):
    cursor.execute("SELECT * FROM Subscribers WHERE name = ?", (subscriber_name,)) 
    results = cursor.fetchall()
    if len(results) > 0:
        subscriber_id = results[0][0]
    else:
        print(f"There was no subscriber named {subscriber_name}.")
        return
    cursor.execute("SELECT * FROM Magazines WHERE name = ?", (magazine_name,))
    results = cursor.fetchall()
    if len(results) > 0:
        magazine_id = results[0][0]
    else:
        print(f"There was no magazine named {magazine_name}.")
        return
    cursor.execute("SELECT * FROM Subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
    results = cursor.fetchall()
    if len(results) > 0:
        print(f"Subscriber {subscriber_name} is already subscribed in magazine {magazine_name}.")
        return
    else:
        cursor.execute("INSERT INTO Subscriptions (expiration_date, subscriber_id, magazine_id) VALUES (?, ?, ?)", (expiration_date, subscriber_id, magazine_id))


cursor = conn.cursor()

# **Task 2: Define Database Structure**

# Create tables
# Publishers
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Publishers (
    publisher_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
    )
""")

# Magazines
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Magazines (
    magazine_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,      
    publisher_id INTEGER,
    FOREIGN KEY (publisher_id) REFERENCES Publishers(publisher_id)
    )
""")
    
# Subscribers
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscribers (
    subscriber_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL
    )
""")

# Subscriptions
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscriptions (
    subscription_id INTEGER PRIMARY KEY,
    expiration_date TEXT NOT NULL,
    subscriber_id INTEGER,
    magazine_id INTEGER,
    FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id),
    FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id)
    )
""")

print("Tables created successfully.")

# **Task 4: Write SQL Queries**
# Insert sample data into tables

add_publisher(cursor, 'Hearst',)
add_publisher(cursor, 'A.G. Sulzberger',)
add_publisher(cursor, 'National Geographic Partners',)
add_magazine(cursor, 'Popular Mechanics', 'Hearst')
add_magazine(cursor, 'Veranda', 'Hearst')
add_magazine(cursor, 'The New York Times', 'A.G. Sulzberger')
add_magazine(cursor, 'National Geographic', 'National Geographic Partners')
add_subscriber(cursor, 'Jane Doe', '123 Main Street, New Town, USA, 12345')
add_subscriber(cursor, 'John Doe', '321 Main Street, New Town, USA, 12345')
add_subscriber(cursor, 'Vasilii Pupkin', '1234 Main Street, New Town, USA, 12345')
add_subscription(cursor, '05/01/2026', 'Jane Doe', 'The New York Times')
add_subscription(cursor, '06/01/2026', 'John Doe', 'National Geographic')
add_subscription(cursor, '07/01/2026', 'Vasilii Pupkin', 'Popular Mechanics')

conn.commit() 

cursor.execute("SELECT * FROM Subscribers")
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute("SELECT * FROM Magazines ORDER BY name")
result = cursor.fetchall()
for row in result:
    print(row)

cursor.execute("SELECT Magazines.name, Publishers.name FROM Publishers INNER JOIN Magazines ON Magazines.publisher_id=Publishers.publisher_id WHERE Publishers.name='Hearst'")
result = cursor.fetchall()
for row in result:
    print(row)
conn.close()


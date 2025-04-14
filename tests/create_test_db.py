# tests/create_test_db.py
import sqlite3
import os

def create_test_db():
    # Create a temporary directory for the test database
    test_dir = os.path.join(os.getcwd(), 'tests')
    os.makedirs(test_dir, exist_ok=True)

    # Create a test database
    test_db_path = os.path.join(test_dir, 'db.sqlite')

    # Create a connection to the test database
    conn = sqlite3.connect(test_db_path)

    # Create a cursor
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''CREATE TABLE IF NOT EXISTS test_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        value INTEGER NOT NULL
    )''')

    # Insert some test data
    cursor.execute('''INSERT INTO test_table (name, value) VALUES (?, ?)''', ('Test', 10))
    cursor.execute('''INSERT INTO test_table (name, value) VALUES (?, ?)''', ('Test2', 20))

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()

    print(f"Test database created at: {test_db_path}")

if __name__ == "__main__":
    create_test_db()

import sqlite3

def inspect_db():
    # Connect to the SQLite database
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()

    # List tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:", tables)

    # Query the rules table if it exists
    if ('rules',) in tables:
        cursor.execute("SELECT * FROM rules")
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)
    else:
        print("The 'rules' table does not exist.")

    # Close the connection
    conn.close()

if __name__ == '__main__':
    inspect_db()
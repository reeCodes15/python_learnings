import mysql.connector

# Establishing a connection to the database
try:
    connection = mysql.connector.connect(
        host="localhost",          # The server hosting the MySQL database
        user="root",               # Your MySQL username (root in this case)
        password="",  # Your MySQL password
        database="study"           # The database to connect to
    )

    if connection.is_connected():
        print("Successfully connected to the database!")

        # You can now create a cursor object and interact with the database
        cursor = connection.cursor()

        # Example query: Fetch all rows from the 'users' table
        cursor.execute("SELECT * FROM users")

        # Fetching and printing the results
        rows = cursor.fetchall()
        for row in rows:
            print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Closing the cursor and connection after the operation is done
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed.")
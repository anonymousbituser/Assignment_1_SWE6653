# Create relational database that is sql based, lightweight and can be embedded into a python application.
import sqlite3


# SQL_lite-based set of functions that will be used to store our sensor data types into a relational database
def setup_database():  # Configure database
    # Create tables/setup database
    try:
        connection = sqlite3.connect('datasets.db')  # Creates connection to database
        cursor = connection.cursor()
        # Create string table for sensor data
        cursor.execute('CREATE TABLE IF NOT EXISTS table_values (row_num INTEGER PRIMARY KEY, name TEXT, address TEXT, id_number REAL)')
        connection.commit()  # Push changes to database
        connection.close()

    except sqlite3.OperationalError as e:
        print(e)


# Grabs data from MCU and stores it into specific table within the database
def write_database(names, addresses, ids):
    connection = sqlite3.connect('datasets.db')  # Creates connection to database
    cursor = connection.cursor()  # Handle used to operate the database

    # Store new data to database
    cursor.execute("INSERT INTO table_values (name, address, id_number) VALUES (?,?,?)", (names, addresses, ids, ))
    connection.commit()  # Push changes to database
    connection.close()  # End connection for next client


def read_data_db():  # Reads data from the database
    connection = sqlite3.connect('datasets.db')  # Creates connection to database
    cursor = connection.cursor()  # Cursor used to make all operations with the database

    # Grab the most recent dataset inside of the database - we want our UI to show the most recent data.
    cursor.execute('SELECT name FROM table_values')
    names = cursor.fetchall()
    cursor.execute('SELECT address FROM table_values')
    addresses = cursor.fetchall()
    cursor.execute('SELECT id_number FROM table_values')
    ids = cursor.fetchall()
    connection.close()  # Close connection

    print(names, addresses, ids)
    return names, addresses, ids
    # return get_temperature, get_rpm


def delete_row_db(delete_index):  # Deletes a specific row in the database
    connection = sqlite3.connect('datasets.db')  # Creates connection to database
    cursor = connection.cursor()  # Cursor used to make all operations with the database
    delete_command = 'DELETE FROM table_values WHERE row_num = ' + delete_index
    cursor.execute(delete_command)
    connection.commit()  # Push changes to database
    connection.close()  # Close connection

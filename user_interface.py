from flask import Flask, render_template, request
from Assignment_1_SWE6653.database import *

app = Flask(__name__)   # Class handle to call Flask API


# Decorator function - wraps a function for Flask to operate - maps url to return value
@app.route('/')
def main_page():  # Initializes the main web page - calls in template html file and passes thru flask
    names, addresses, ids = read_data_db()  # Grab initial values from database
    return render_template("webpage.html", names=names, addresses=addresses, ids=ids)


@app.route("/add_click/", methods=['POST'])
def add_data_button_click():  # Method used to add data from webpage to database.
    # Update all html items
    #  - Read database, update html variables
    # TODO:
    #  - Add data from textbox to database - append
    # Grab HTML values from webpage
    name = request.form.get("name")
    addr = request.form.get("address")
    id = request.form.get("id")

    # Save data to database
    write_database(name, addr, id)
    # Grab data from database
    names, addresses, ids = read_data_db()
    # Render data to html file
    return render_template("webpage.html", names=names, addresses=addresses, ids=ids)


# Deletes an element from the database
@app.route("/remove_click/", methods=['POST'])
def del_data_button_click():  # Method used to perform specific operations when add data button is pressed.

    unique_delete_id = request.form.get("id")  # Grabs the index value and tells database which element to delete
    print("unique delete id = ", unique_delete_id)
    delete_row_db(unique_delete_id)  # Takes the specific row requested for deletion from webpage and removes from the
    # database

    names, addresses, ids = read_data_db()
    return render_template("webpage.html", names=names, addresses=addresses, ids=ids)
# Used to for testing/troubleshooting purposes


if __name__ == '__main__':
    setup_database()  # Initializes the database
    app.run(debug=True)  # Main entry point - start webserver

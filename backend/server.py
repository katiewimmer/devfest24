import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, session, g, redirect, Response, abort, url_for
from datetime import datetime
import re
from sqlalchemy.exc import IntegrityError
import mysql.connector

# MySQL server connection parameters
db_config = {
    'host': '127.0.0.1',               # MySQL server IP or domain
    'user': 'devfestgroup',                    # MySQL username
    'password': '1234',                    # MySQL password (replace with the actual password)
    'database': 'devfest24',       # Name of the database
    'port': 3306                       # MySQL server port (default is 3306)
}

try:
    # Establish a connection to the MySQL server
    connection = mysql.connector.connect(**db_config)

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()
    
    
    # Example: Insert a new row into the "community" table (excluding comID)
    insert_query = """
    INSERT INTO community (townName, stateAbrv, population) 
    VALUES (%s, %s, %s)
    """
    values = ('Windham', 'NH', 1000)  # Replace with actual values
    cursor.execute(insert_query, values)

    # Commit the changes to the database
    connection.commit()

    # Example: Select all rows from the "community" table
    cursor.execute("SELECT * FROM community")
    results = cursor.fetchall()
    for row in results:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
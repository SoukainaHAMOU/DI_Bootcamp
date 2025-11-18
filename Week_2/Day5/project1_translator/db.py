from psycopg2 import Error
from psycopg2 import connect
from dotenv import load_dotenv
import os
"""
Code idea	            Real-life analogy

Import libraries	    |    Bring the tools you need to work
load_dotenv()	        |    Look at the secret paper with passwords
get_connection()	    |    Use the password to open the door to the database
except Error	        |    If the key is wrong, show an error
close_connection()	    |    Close the door when you leave
"""

load_dotenv()

def get_connection():    
    try:
        connection = connect(
            dbname=os.getenv("NAME"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            host=os.getenv("HOST"),
            #port=os.getenv("PORT")
        )
        print("Connected successfully!")
        return connection
    except Error as e:
        print("Connection failed:", e)
        return None
    
def close_connection(connection):
    if connection:
        connection.close()
        print("Connection closed.")
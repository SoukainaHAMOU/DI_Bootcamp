import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import Error
from psycopg2 import sql

# Load environment variables from .env
load_dotenv()



# Build connection URL
DB_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}?sslmode=require&channelyh_binding=require"


def get_connection():
    """
    Establish and return a PostgreSQL connection using environment variables.
    """
    try:
        connection = psycopg2.connect(
        name=os.getenv("NAME"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        #sslmode='require'
        )
        print("Connected successfully!")
        return connection
    except Exception as e:
        print("Connection failed:", e)
        return None

def close_connection(connection):
    """
    Close the given PostgreSQL connection.
    """
    if connection:
        connection.close()
        print("Connection closed.")
# # Example usage
# if __name__ == "__main__":
#     conn = get_connection()
#     if conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT version();")
#         print("PostgreSQL version:", cursor.fetchone())
#         cursor.close()
#         conn.close()

import mysql.connector

def get_connection():
    """Create and return a connection to the MySQL database"""
    conn = mysql.connector.connect(
        host="YOUR HOST IP",
        port= YOUR PORT NUMBER,
        user="YOUR DATABASE USERNAME",
        password="YOUR DATABASE PASSWORD",
        database="YOUR DATABASE NAME"
    )
    return conn

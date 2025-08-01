# File: MySQLServer.py

import mysql.connector

connection = None

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='richm@2003'  
    )
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
finally:
    if connection and connection.is_connected():
        cursor.close()
        connection.close()

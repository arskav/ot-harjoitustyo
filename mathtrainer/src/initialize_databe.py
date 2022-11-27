import os
import sqlite3


def get_database_connection(db_file):

    connection = None    
    connection = sqlite3.connect(db_file)       
    return connection

def create_usertable(connection):

    cursor = connection.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS users;
    """)

    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    user TEXT NOT NULL,
    started TEXT,
    finished TEXT,
    correct_total INTEGER,
    tries_total INTEGER
    );   """

    cursor.execute(sql_create_users_table)

    connection.commit()

if __name__ == '__main__':

    database = "../data/userdata.sqlite"
    
    connection = get_database_connection(database)

    create_usertable(connection)

    

    


import sqlite3

DATABASE_USERS = "./data/userdata.sqlite"
DATABASE_SESSIONS = "./data/sessiondata.sqlite"


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


def create_sessiontable(connection):

    cursor = connection.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS Sessions;
    """)

    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS Sessions (
    id INTEGER PRIMARY KEY,
    user TEXT NOT NULL,
    practise INTEGER NOT NULL,
    correct INTEGER,
    tries INTEGER,
    level INTEGER,
    correct_at_level INTEGER,
    tries_at_level INTEGER
    );   """

    cursor.execute(sql_create_users_table)

    connection.commit()


if __name__ == '__main__':

    my_connection = sqlite3.connect(DATABASE_USERS)

    create_usertable(my_connection)

    my_connection = sqlite3.connect(DATABASE_SESSIONS)

    create_sessiontable(my_connection)

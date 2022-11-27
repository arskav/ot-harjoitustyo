import sqlite3

DATABASE = "../data/userdata.sqlite"


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

    my_connection = sqlite3.connect(DATABASE)

    create_usertable(my_connection)

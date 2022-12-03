import sqlite3
from repositories.session_repository import session_repository

DATABASE_USERS = "../data/userdata.sqlite"
DATABASE_SESSIONS = "../data/sessiondata.sqlite"


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

    # Testausta
    """
    session_repository.insert_new_session("arska", 1)

    session_repository.insert_new_session("arska", 2)

    session_repository.insert_new_session("arska", 3)

    session_repository.insert_new_session("ratja", 1)

    session_repository.insert_new_session("ratja", 2)

    session_repository.insert_new_session("Minna", 1)

    session_repository.insert_new_session("arska2", 1)

    session_repository.insert_new_session("arska2", 2)

    session_repository.insert_new_session("arska2", 3)


    print(session_repository.find_all_sessions())   

    session_repository.update_session("arska", 2, 10, 20, 4, 3, 4)

    session_repository.update_session("arska", 2, 10, 20, 5, 3, 4)

    session_repository.update_session("Minna", 1, 100, 20, 5, 3, 4)

    print(session_repository.find_all_sessions())

    print(session_repository.find_sessions_of_practise(1, "user"))

    print(session_repository.find_sessions_of_practise(1, "tries"))

    print(session_repository.find_sessions_of_practise(1, "level_and_user"))

    print(session_repository.find_session_of_user("arska", 2))
    """

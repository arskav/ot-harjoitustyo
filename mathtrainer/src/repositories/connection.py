import sqlite3

def get_database_connection(db_file):

    connection = None
    connection = sqlite3.connect(db_file)
    return connection

def database_updating(connection, sql_command, parameters_as_tuple):

    cursor = connection.cursor()

    cursor.execute(sql_command, parameters_as_tuple)

    connection.commit()


def database_searching(connection, sql_command, parameters_as_tuple):

    cursor = connection.cursor()

    if parameters_as_tuple == ():

        cursor.execute(sql_command)

    else:

        cursor.execute(sql_command, parameters_as_tuple)

    return cursor

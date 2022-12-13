"""Tietokantayhteyden luominen tiedostoon, erilaiset tallennukset tietokantaan,
tiedon haku tietokannasta."""
import sqlite3

def get_database_connection(db_file):
    """Tietokantayhteyden luominen

    Args:
        db_file: tiedoston nimi.

    Returns:
        yhteys
    """

    connection = None
    connection = sqlite3.connect(db_file)
    return connection

def database_updating(connection, sql_command, parameters_as_tuple):
    """Tiedon lisääminen tai päivittäminen tietokantaan.

    Args:
        connection: yhteys.
        sql_command (string): SQL-kielen komento
        parameters_as_tuple: SQL-komennon parametrit.
    """

    cursor = connection.cursor()

    cursor.execute(sql_command, parameters_as_tuple)

    connection.commit()


def database_searching(connection, sql_command, parameters_as_tuple):
    """Tiedon haku tietokannasta.

    Args:
        connection: yhteys.
        sql_command (string): SQL-kielen komento
        parameters_as_tuple: SQL-komennon parametrit.

    Returns:
        haetut tiedot.
    """

    cursor = connection.cursor()

    if parameters_as_tuple == ():

        cursor.execute(sql_command)

    else:

        cursor.execute(sql_command, parameters_as_tuple)

    return cursor

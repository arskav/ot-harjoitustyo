"""Käyttäjätietojen eli luokan MathTrainerUser olion tietojen tallentaminen
ja käsittely tietokannassa.
"""
from config import DATABASE_USERS
from repositories.connection import get_database_connection,\
    database_updating, database_searching

class UserRepository:
    """Käyttäjätietoihin liittyvistä tietokantaoperaatioista vastaava luokka
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: yhteys tietokannan sisältävään tiedostoon.
        """

        self._connection = connection

    def insert_new_user(self, username):
        """uden käyttäjätunnuksen lisääminen tietokantaan.

        Args:
            username (string): käyttäjätunnus.
        """

        sql_command = """
        INSERT INTO Users (user, started, finished, correct_total, tries_total)
        VALUES(?,?,?,?,?)
        """

        parameters = (username, '', '', 0, 0,)

        database_updating(self._connection, sql_command, parameters)

    def update_user(self, username, new_started, new_finished, new_correct, new_tries):
        """Käyttäjätietojen päivitys tietokantaan.

        Args:
            username (string): käyttäjätunnus.
            new_started (string): aloitetut harjoitukset merkkijonoina.
            new_finished (string): loppuun tehdyt harjoitukset merkkijonoina.
            new_correct (int): oikeiden vastausten päivitetty lkm.
            new_tries (int): yritysten päivitetty lkm.
        """

        sql_command = """
        UPDATE Users SET started = ?, finished = ?, correct_total = ?, tries_total = ?
        WHERE user = ?
        """

        parameters = (new_started, new_finished, new_correct, new_tries, username,)

        database_updating(self._connection, sql_command, parameters)

    def find_all_users(self):
        """Haetaan kaikki käyttäjätunnukset tietokannasta.

        Returns:
            Käyttäjätunnukset.
        """

        sql_command = """
        SELECT user FROM Users ORDER BY user COLLATE NOCASE
        """

        cursor = database_searching(self._connection, sql_command, ())

        rows = cursor.fetchall()

        return rows

    def find_all_users_with_practises(self):
        """Haetaan käyttäjätunnukset ja käyttäjät harjoitustiedot tietokannasta.

        Returns:
            Käyttäjätiedot.
        """


        sql_command = """
        SELECT * FROM Users ORDER BY user COLLATE NOCASE
        """

        cursor = database_searching(self._connection, sql_command, ())

        rows = cursor.fetchall()

        return rows


    def find_user(self, username):
        """Haetaan yksittäisen käyttäjän tiedot tietokannasta.

        Args:
            username (string): käyttäjätunnus.

        Returns:
            Haettua käyttäjätunnusta vastaavat tiedot.
        """

        sql_command = """
        SELECT * FROM Users WHERE user = ?
        """

        parameters = (username,)

        cursor = database_searching(self._connection, sql_command, parameters)

        row = cursor.fetchone()

        return row


user_repository = UserRepository(get_database_connection(DATABASE_USERS))

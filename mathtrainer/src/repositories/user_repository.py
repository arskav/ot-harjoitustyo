import sqlite3
# Tämä tiedosto pitää siistiä, nyt toistetaan samaa koodia, vain SQL-käsky vaihtelee


def get_database_connection(db_file):

    connection = None
    connection = sqlite3.connect(db_file)
    return connection


class UserRepository:
    """Käyttäjätietoihin liittyvistä tietokantaoperaatioista vastaava luokka
    """

    def __init__(self, connection):

        self._connection = connection

    def insert_new_user(self, username):

        cursor = self._connection.cursor()

        datarow = (username, '', '', 0, 0,)

        cursor.execute(
            "INSERT INTO Users (user, started, finished, correct_total, tries_total)"
            " VALUES(?,?,?,?,?)",
            datarow
        )

        self._connection.commit()

    def update_user(self, username, new_started, new_finished, new_correct, new_tries):

        cursor = self._connection.cursor()

        cursor.execute(
            "UPDATE Users SET started = ?, finished = ?, correct_total = ?, tries_total = ?"
            "WHERE user = ?",
            (new_started, new_finished, new_correct, new_tries, username,)
        )

        self._connection.commit()

    def find_all_usernames(self):

        cursor = self._connection.cursor()

        cursor.execute("SELECT user FROM Users ORDER BY user COLLATE NOCASE")

        rows = cursor.fetchall()

        return rows

    def print_all_usernames(self):

        print("\nKaikki käyttäjätunnukset:")

        rows = self.find_all_usernames()

        for item in set(rows):
            print(item[0])

    def find_all_users_with_practises(self):

        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Users ORDER BY user COLLATE NOCASE")

        rows = cursor.fetchall()

        return rows

    def print_all_users_with_practises(self):
        # Tulostus siistittävä, nyt lähinnä testauksen apuna

        rows = self.find_all_users_with_practises()

        for item in set(rows):
            print(item[1], "aloitetut harjoitukset", item[2],
                  ", tehty loppuun", item[3], ", oikeita", item[4], "/", item[5])


    def find_all_users(self):

        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Users")

        rows = cursor.fetchall()

        return rows

    def find_user(self, username):

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM Users WHERE user = ?",
            (username,)
        )

        row = cursor.fetchone()

        return row


DATABASE = "./data/userdata.sqlite"

user_repository = UserRepository(get_database_connection(DATABASE))

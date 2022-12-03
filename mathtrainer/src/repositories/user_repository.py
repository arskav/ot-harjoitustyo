import sqlite3


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

        cursor.execute("SELECT user FROM Users")

        rows = cursor.fetchall()

        return rows


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


DATABASE = "../data/userdata.sqlite"  # muuta

user_repository = UserRepository(get_database_connection(DATABASE))

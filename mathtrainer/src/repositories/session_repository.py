import sqlite3


def get_database_connection(db_file):

    connection = None
    connection = sqlite3.connect(db_file)
    return connection


class SessionRepository:
    """Harjoitustietoihin liittyvistä tietokantaoperaatioista vastaava luokka
    """

    def __init__(self, connection):

        self._connection = connection

    def insert_new_session(self, username, practise, correct, tries, level, correct_at_level, tries_at_level):

        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO Sessions (user, practise, correct, tries, level, correct_at_level, tries_at_level)"
            " VALUES(?,?,?,?,?, ?, ?)",
            (username, practise, correct, tries, level, correct_at_level, tries_at_level,)
        )

        self._connection.commit()

    def update_session(self, username, practise, correct, tries, level, correct_at_level, tries_at_level):

        cursor = self._connection.cursor()

        cursor.execute(
            "UPDATE Sessions SET correct = ?, tries = ?, level = ?, correct_at_level = ?, tries_at_level = ?"
            "WHERE user = ? AND practise = ?",
            (correct, tries, level, correct_at_level,
             tries_at_level, username, practise)
        )

        self._connection.commit()

    def find_all_sessions(self):

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM Sessions ORDER BY user COLLATE NOCASE, practise")

        rows = cursor.fetchall()

        return rows

    def find_session_of_user(self, username, practise, level):
        # viimeisin taso
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM Sessions WHERE user = ? AND practise = ? AND level = ?",
            (username, practise, level,)
        )
        row = cursor.fetchone()

        return row[3], row[4], row[6], row[7]

    def find_sessions_of_practise(self, practise, ordered):

        cursor = self._connection.cursor()

        if ordered == "tries":

            cursor.execute(
                "SELECT * FROM Sessions WHERE practise = ? ORDER BY tries DESC",
                (practise,)
            )

        elif ordered == "level_and_user":

            cursor.execute(
                "SELECT * FROM Sessions WHERE practise = ? ORDER BY level DESC, user COLLATE NOCASE",
                (practise,)
            )

        else:

            cursor.execute(
                "SELECT * FROM Sessions WHERE practise = ? ORDER BY user COLLATE NOCASE",
                (practise,)
            )

        row = cursor.fetchall()

        return row


DATABASE_SESSIONS = "../data/sessiondata.sqlite"  # Muuta

session_repository = SessionRepository(
    get_database_connection(DATABASE_SESSIONS))

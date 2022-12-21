from config import DATABASE_SESSIONS

from repositories.connection import get_database_connection,\
    database_updating, database_searching

class SessionRepository:
    """Harjoitustietoihin liittyvistä tietokantaoperaatioista vastaava luokka
    """

    def __init__(self, connection):

        self._connection = connection

    def insert_new_session(self, session):

        sql_command = """
        INSERT INTO Sessions
        (user, practise, correct, tries, level, correct_at_level, tries_at_level)
        VALUES(?,?,?,?,?,?,?)
        """

        parameters = (session.user(), session.practise(), session.correct(), session.tries(),\
             session.level(), session.correct_at_level(), session.tries_at_level(),)

        database_updating(self._connection, sql_command, parameters)

    def update_session(self, session):

        sql_command = """
        UPDATE Sessions
        SET correct = ?, tries = ?, correct_at_level = ?, tries_at_level = ?
        WHERE user = ? AND practise = ? AND level = ?
        """

        parameters= (session.correct(), session.tries(), session.correct_at_level(),\
            session.tries_at_level(), session.user(), session.practise(), session.level(),)

        database_updating(self._connection, sql_command, parameters)

    def  find_all_sessions(self):

        sql_command = """
        SELECT * FROM Sessions ORDER BY user COLLATE NOCASE, practise
        """

        cursor = database_searching(self._connection, sql_command, ())

        return cursor.fetchall()


    def find_all_sessions_of_user(self, username):

        sql_command = """
        SELECT * FROM Sessions WHERE user = ? ORDER BY practise, level
        """

        parameters = (username,)

        cursor = database_searching(self._connection, sql_command, parameters)

        return cursor.fetchall()


    def find_all_sessions_of_practise(self, practise):

        sql_command = """
        SELECT * FROM Sessions WHERE practise = ?
        ORDER BY user COLLATE NOCASE, level
        """

        parameters = (practise,)

        cursor = database_searching(self._connection, sql_command, parameters)

        return cursor.fetchall()


    def find_session_of_user(self, username, practise):
        # Valitaan se, jonka taso level korkein

        sql_command = """
        SELECT * FROM Sessions WHERE user = ? AND practise = ? ORDER BY level DESC
        """
        parameters = (username, practise,)

        cursor = database_searching(self._connection, sql_command, parameters)

        row = cursor.fetchone()

        if row is None:

            return None, None, None, None, None

        # palauttaa correct, tries, level, correct_at_level, tries_at_level
        return row[3], row[4], row[5], row[6], row[7]


    def delete_all_sessions_of_user(self, username):
        """Poistetaan kaikki käyttäjätunnukseen liittyvät
        harjoitussessiot.

        Args:
            username (string): käyttäjätunnus, jonka sessioiden
                tiedot poistetaan.
        """

        sql_command = """
        DELETE FROM Sessions WHERE user = ?
        """
        parameters = (username,)

        database_updating(self._connection, sql_command, parameters)


session_repository = SessionRepository(
    get_database_connection(DATABASE_SESSIONS))

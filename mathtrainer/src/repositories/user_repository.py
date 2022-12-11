from repositories.connection import get_database_connection,\
    database_updating, database_searching

def output(item):

    string = item[1] + " "


    if item[2] == '':

        string += "ei aloitettuja harjoituksia."

    else:

        string += "aloitetut harjoitukset: "
        string += item[2]

        if item[3] == '':

            string += ", ei loppuun tehtyjä harjoituksia"

        else:

            string += ", tehdyt harjoitukset: "
            string += item[3]

        string += f". oikein/yritykset: {item[4]}/{item[5]}"

    return string


class UserRepository:
    """Käyttäjätietoihin liittyvistä tietokantaoperaatioista vastaava luokka
    """

    def __init__(self, connection):

        self._connection = connection

    def insert_new_user(self, username):

        sql_command = """
        INSERT INTO Users (user, started, finished, correct_total, tries_total)
        VALUES(?,?,?,?,?)
        """

        parameters = (username, '', '', 0, 0,)

        database_updating(self._connection, sql_command, parameters)

    def update_user(self, username, new_started, new_finished, new_correct, new_tries):

        sql_command = """
        UPDATE Users SET started = ?, finished = ?, correct_total = ?, tries_total = ?
        WHERE user = ?
        """

        parameters = (new_started, new_finished, new_correct, new_tries, username,)

        database_updating(self._connection, sql_command, parameters)

    def find_all_users(self):

        sql_command = """
        SELECT user FROM Users ORDER BY user COLLATE NOCASE
        """

        cursor = database_searching(self._connection, sql_command, ())

        rows = cursor.fetchall()

        return rows

    def print_all_users(self):

        print("\nKaikki käyttäjätunnukset:")

        rows = self.find_all_users()

        for item in set(rows):
            print(item[0])

    def find_all_users_with_practises(self):

        sql_command = """
        SELECT * FROM Users ORDER BY user COLLATE NOCASE
        """

        cursor = database_searching(self._connection, sql_command, ())

        rows = cursor.fetchall()

        return rows

    def print_all_users_with_practises(self):

        rows = self.find_all_users_with_practises()

        for item in set(rows):

            print(output(item))


    def find_user(self, username):

        sql_command = """
        SELECT * FROM Users WHERE user = ?
        """

        parameters = (username,)

        cursor = database_searching(self._connection, sql_command, parameters)

        row = cursor.fetchone()

        return row


DATABASE = "./data/userdata.sqlite"

user_repository = UserRepository(get_database_connection(DATABASE))

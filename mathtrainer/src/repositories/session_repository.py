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



    # def print_all_sessions(self):

    #     rows = self.find_all_sessions()

    #     if len(rows) == 0:

    #         print("Ei suorituksia.")

    #         return

    #     for item in rows:
    #         print(f"Käyttäjätunnus: {item[1]}")
    #         print(f"Harjoituksessa {item[2]} oikein {item[3]}, yrityksiä {item[4]}, "
    #               f"{item[5]}. tasolla: {item[6]} oikein {item[7]} yrityksestä.")
    #         print('-' * 50)

    #     return

    def find_all_sessions_of_user(self, username):

        sql_command = """
        SELECT * FROM Sessions WHERE user = ? ORDER BY practise, level
        """

        parameters = (username,)

        cursor = database_searching(self._connection, sql_command, parameters)

        return cursor.fetchall()


    # def print_all_sessions_of_user(self, username):

    #     rows = self.find_all_sessions_of_user(username)

    #     if len(rows) == 0:

    #         print("Ei suorituksia.")

    #         return


    #     print("Käyttäjätunnuksen", username, "harjoitustulokset:")

    #     print('-' * 50)

    #     for item in rows:
    #         print(f"Harjoituksessa {item[2]} oikein {item[3]}, yrityksiä {item[4]}, "
    #               f"{item[5]}. tasolla {item[6]} oikein {item[7]} yrityksestä.")
    #         print('-' * 50)

    #     return

    def find_all_sessions_of_practise(self, practise):

        sql_command = """
        SELECT * FROM Sessions WHERE practise = ?
        ORDER BY user COLLATE NOCASE, level
        """

        parameters = (practise,)

        cursor = database_searching(self._connection, sql_command, parameters)

        return cursor.fetchall()

    # def print_all_sessions_of_practise(self, practise):

    #     rows = self.find_all_sessions_of_practise(practise)

    #     if len(rows) == 0:

    #         print("Ei suorituksia.")

    #         return

    #     print("Harjoituksen", practise, "käyttäjäkohtaiset tulokset:")

    #     print('-' * 50)

    #     for item in rows:
    #         print("Käyttäjällä", item[1])
    #         print(f"oikein {item[3]}, yrityksiä {item[4]}, "
    #               f"{item[5]}. tasolla {item[6]} oikein {item[7]} yrityksestä.")
    #         print('-' * 50)

    #     return

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

    # def print_statistics_of_practise(self, practise):

    #     data = self.find_all_sessions_of_practise(practise)

    #     data_of_levels = {}

    #     max_level = 0

    #     for item in data:
    #         if item[5] not in data_of_levels:
    #             data_of_levels[item[5]] = {'corrects': item[6], 'tries': item[7]}
    #             if item[5] > max_level:
    #                 max_level = item[5]
    #         else:
    #             data_of_levels[item[5]]['corrects'] += item[6]
    #             data_of_levels[item[5]]['tries'] += item[7]



    #     statistics = PrettyTable()

    #     statistics.field_names = ['taso', 'oikein', 'yrityksiä', 'osuus']

    #     if max_level > 0:

    #         for i in range(max_level):

    #             corrects = data_of_levels[i+1]['corrects']
    #             tries = data_of_levels[i+1]['tries']
    #             try:
    #                 percentage = str(round(100 * corrects / tries))+"%"
    #             except ZeroDivisionError:
    #                 percentage = "-"

    #             statistics.add_row([str(i+1), str(corrects), str(tries), percentage])

    #     else:

    #         print("\nEi suorituksia.")

    #         return(data_of_levels)

    #     print(statistics)

    #     #Testausta varten
    #     return(data_of_levels)

session_repository = SessionRepository(
    get_database_connection(DATABASE_SESSIONS))

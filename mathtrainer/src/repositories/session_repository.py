import sqlite3
#Tämä tiedosto pitää siistiä, nyt toistetaan samaa koodia, vain SQL-käsky vaihtelee

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
            (username, practise, correct, tries,
             level, correct_at_level, tries_at_level,)
        )

        self._connection.commit()

    def update_session(self, username, practise, correct, tries, level, correct_at_level, tries_at_level):

        cursor = self._connection.cursor()

        cursor.execute(
            "UPDATE Sessions SET correct = ?, tries = ?, correct_at_level = ?, tries_at_level = ?"
            "WHERE user = ? AND practise = ? AND level = ?",
            (correct, tries, correct_at_level,
             tries_at_level, username, practise, level)
        )

        self._connection.commit()

    def find_all_sessions(self):

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM Sessions ORDER BY user COLLATE NOCASE, practise")

        rows = cursor.fetchall()

        return rows

    def print_all_sessions(self):

        rows = self.find_all_sessions()

        for item in rows:
            print(f"Käyttäjätunnus: {item[1]}")
            print(f"Harjoituksessa {item[2]} oikein {item[3]}, yrityksiä {item[4]}, "
                  f"{item[5]}. tasolla: {item[6]} oikein {item[7]} yrityksestä.")
            print('-' * 50)

    def find_all_sessions_of_user(self, username):

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM Sessions WHERE user = ? ORDER BY practise, level", (username,))

        rows = cursor.fetchall()

        return rows

    def print_all_sessions_of_user(self, username):

        rows = self.find_all_sessions_of_user(username)

        print("Käyttäjätunnuksen", username, "harjoitustulokset:")

        print('-' * 50)

        for item in rows:
            print(f"Harjoituksessa {item[2]} oikein {item[3]}, yrityksiä {item[4]}, "
                  f"{item[5]}. tasolla {item[6]} oikein {item[7]} yrityksestä.")
            print('-' * 50)

    def find_all_sessions_of_practise(self, practise):

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM Sessions WHERE practise = ?  ORDER BY user COLLATE NOCASE, level", (practise,))

        rows = cursor.fetchall()

        return rows

    def print_all_sessions_of_practise(self, practise):

        rows = self.find_all_sessions_of_practise(practise)

        print("Harjoituksen", practise, "käyttäjäkohtaiset tulokset:")

        print('-' * 50)

        for item in rows:
            print("Käyttäjällä", item[1])
            print(f"oikein {item[3]}, yrityksiä {item[4]}, "
                  f"{item[5]}. tasolla {item[6]} oikein {item[7]} yrityksestä.")
            print('-' * 50)

    def find_all_sessions_of_practise(self, practise):

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM Sessions WHERE practise = ? ORDER BY level, user COLLATE NOCASE",
            (practise,)
            )

        row = cursor.fetchall()

        return row

    def find_session_of_user(self, username, practise):
        # viimeisin taso
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM Sessions WHERE user = ? AND practise = ? ORDER BY level DESC",
            (username, practise,)
        )
        #Valitaan se, jonka taso level korkein
        row = cursor.fetchone()

        #palauttaa correct, tries, level, correct_at_level, tries_at_level
        return row[3], row[4], row[5],row[6], row[7]



DATABASE_SESSIONS = "../data/sessiondata.sqlite"  # Muuta

session_repository = SessionRepository(
    get_database_connection(DATABASE_SESSIONS))

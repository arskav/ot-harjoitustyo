from prettytable import PrettyTable
#pip install prettytable poetry add prettytable
from repositories.session_repository import session_repository as default_session_repository
from repositories.user_repository import user_repository as default_user_repository

class PrintingService:
    """Tietokannoista tulostamista vastaava luokka."""

    def __init__(self,
        session_repository=default_session_repository,
        user_repository=default_user_repository
   ):
        """Luokan konstruktori.

        Args:
            session_repository (SessionRepository, optional): Luokan MathTrainerSession
                tietokantaoperaatiot. Defaults to default_session_repository.
            user_repository (UserRepository, optional): Luokan MathTrainerUser
                tietokantaoperaatiot. Defaults to default_user_repository.
        """
        self._session_repository = session_repository
        self._user_repository = user_repository

    def print_all_sessions(self):
        """Tulostaa kaikki harjoitussessiot."""

        rows = self._session_repository.find_all_sessions()

        if len(rows) == 0:

            print("Ei suorituksia.")

            return

        for item in rows:
            print(f"Käyttäjätunnus: {item[1]}")
            print(f"Harjoituksessa {item[2]} oikein {item[3]}, yrityksiä {item[4]}, "
                  f"{item[5]}. tasolla: {item[6]} oikein {item[7]} yrityksestä.")
            print('-' * 50)

        return

    def print_all_sessions_of_user(self, username):
        """Tulostaa käyttäjän harjoitussessiot.

        Args:
            username (string): käyttäjätunnus.
        """

        rows =  self._session_repository.find_all_sessions_of_user(username)

        if len(rows) == 0:

            print("Ei suorituksia.")

            return


        print("Käyttäjätunnuksen", username, "harjoitustulokset:")

        print('-' * 50)

        for item in rows:
            print(f"Harjoituksessa {item[2]} oikein {item[3]}, yrityksiä {item[4]}, "
                  f"{item[5]}. tasolla {item[6]} oikein {item[7]} yrityksestä.")
            print('-' * 50)

        return

    def print_all_sessions_of_practise(self, practise):
        """Tulostaa harjoituksen kaikki harjoitussessiot.

        Args:
            practise (int): harjoituksen numero.
        """

        rows =  self._session_repository.find_all_sessions_of_practise(practise)

        if len(rows) == 0:

            print("Ei suorituksia.")

            return

        print("Harjoituksen", practise, "käyttäjäkohtaiset tulokset:")

        print('-' * 50)

        for item in rows:
            print("Käyttäjällä", item[1])
            print(f"oikein {item[3]}, yrityksiä {item[4]}, "
                  f"{item[5]}. tasolla {item[6]} oikein {item[7]} yrityksestä.")
            print('-' * 50)

        return

    def print_statistics_of_practise(self, practise):
        """Tulostaa tilastotietoa harjoituksen suorituksista.

        Args:
            practise (int): harjoituksen numero.
        """

        data =  self._session_repository.find_all_sessions_of_practise(practise)

        data_of_levels = {}

        max_level = 0

        for item in data:
            if item[5] not in data_of_levels:
                data_of_levels[item[5]] = {'corrects': item[6], 'tries': item[7]}
                if item[5] > max_level:
                    max_level = item[5]
            else:
                data_of_levels[item[5]]['corrects'] += item[6]
                data_of_levels[item[5]]['tries'] += item[7]



        statistics = PrettyTable()

        statistics.field_names = ['taso', 'oikein', 'yrityksiä', 'osuus']

        if max_level > 0:

            for i in range(max_level):

                corrects = data_of_levels[i+1]['corrects']
                tries = data_of_levels[i+1]['tries']
                try:
                    percentage = str(round(100 * corrects / tries))+"%"
                except ZeroDivisionError:
                    percentage = "-"

                statistics.add_row([str(i+1), str(corrects), str(tries), percentage])

        else:

            print("\nEi suorituksia.")

            return data_of_levels

        print(statistics)

        #Testausta varten
        return data_of_levels


    def print_all_users(self):
        """Kaikkien käyttäjätunnusten tulostus."""

        rows =  self._user_repository.find_all_users()

        print()

        print("Kaikki käyttäjätunnukset:")

        for item in rows:
            print(item[0])


    def print_all_users_with_practises(self):
        """Tulostetaan käyttäjien tiedot."""

        def output(item):
            """Merkkijonon muodostaminen tulostusta varten.

            Args:
                item (list): tietokannasta palautettu rivi.

            Returns:
                string: merkkijono tulostusta varten.
            """

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




        rows =  self._user_repository.find_all_users_with_practises()

        for item in rows:

            print(output(item))



printing_service = PrintingService()

import os

from entities.definitions import COMMANDS,  COMMANDS_ADMIN, MAXLEVELS

from entities.user import MathTrainerUser

from entities.session import MathTrainerSession

from services.utilities import string_to_list

from repositories.user_repository import user_repository

from repositories.session_repository import session_repository

from ui.admin import MathTrainerAdmin


class MathTrainer:
    """Sovelluksen käyttöliittymästä vastaava luokka."""

    def show_main_menu(self, trainee):
        """Näyttää käyttäjän tiedot ja päävalikon.

        Args:
            trainee (MathTrainerUsr): käyttäjä.
        """

        print(trainee)

        for command in COMMANDS:

            print(command, ":", COMMANDS[command])


    def action(self, trainee, choice):
        """Päävalikosta valitun toimenpiteen suorittaminen.

        Args:
            trainee (MathTrainerUser): käyttäjä.
            choice (int): valinta.
        """

        if choice == "O":

            self._help()

        elif choice == "Y":

            mathtrainer_admin = MathTrainerAdmin()
            mathtrainer_admin._start()

        else:

            self.begin_practising(int(choice), trainee)


    def begin_practising(self, drill, trainee):
        """Harjoituksen tekemisen aloitus.

        Args:
            drill (int): harjoitus
            trainee (MathTrainerUser): käyttäjä.
        """

        if drill not in trainee.practise_finished():

            if drill in trainee.practise_started():

                correct, tries, level, correct_at_level, tries_at_level = session_repository.find_session_of_user(
                    trainee.username(), drill)

                session = MathTrainerSession(
                    trainee.username(), drill, level)
                session.set_corrects_and_tries(correct, tries,correct_at_level, tries_at_level )
            else:
                trainee.practise_started_append(drill)
                session = MathTrainerSession(
                    trainee.username(), drill, 1)
                session.to_database_new()
            session.begin_practise(trainee)

        else:

            self._all_done(drill)

    def _all_done(self, drill):
        """Ilmoitus, jos harjoitus tehty loppuun.

        Args:
            drill (int): harjoitus.
        """
        os.system('clear')
        print(f"Olet tehnyt kaikki tehtävät harjoituksissa {drill}.")
        print("Jos haluat tehdä tämän harjoituksen tehtäviä uudelleen, valitse uusi käyttäjätunnus.")
        input("Jatka >> ")

    def shutdown(self, trainee):
        """Ohjelman lopetus.

        Args:
            trainee (MathTrainerUser): käyttäjä.
        """
        os.system('clear')
        print("Lopetetaan ohjelman suoritus.")
        print("Käyttäjän tiedot:")
        print(trainee)

    def _help(self):
        """Ohjeiden tulostaminen,"""
        os.system('clear')
        print("Valintasi: O")
        print("Laskutehtävien suorituksen voi keskeyttää antamalla laskun vastaukseksi tyhjän.")
        print()
        print("Osassa tehtävissä on 'laskin' käytössä:")
        print("Kirjoita alkuun = ja sitten laskutoimituksia +, -, *, / sisältävä lauseke.")
        print("Esimerkiksi =2*(3+4) tai = (4 - 2) / -2.")
        print()
        print("Jos haluat tehdä uudelleen jonkin jo tekemäsi harjoituksen,"
        "valitse uusi käyttäjätunnus.")
        print()
        print("Kehotteeseen Jatka >> voi vastata Enterillä.")
        print()


    def problems_with_databases(self):
        """Tarkistaa, onko sovelluksen käyttämät tietokannat luotu.

        Returns:
            string: virheilmoitus.
        """

        problems = False

        try:

            user_repository.find_user('admin')

        except Exception as e:

            print(e)

            problems = True

        try:

            session_repository.find_all_sessions_of_user('admin')

        except Exception as e:

            print(e)

            problems =  True


        return problems


    def login(self):
        """Sisäänkirjautuminen.

        Returns:
            MathTrainerUser: käyttäjä, tiedot alustettu tai
            string; virheilmoitus.
        """

        os.system('clear')

        username = input("Anna käyttäjätunnus (vähintään viisi merkkiä) ")

        while len(username) < 5:
            print("Liian lyhyt käyttäjätunnus, oltava vähintään 5 merkkiä")
            username = input("Anna käyttäjätunnus (vähintään viisi merkkiä) ")

        if user_repository.find_user(username) is None:

            print("Uusi käyttäjätunnus.")

            trainee = MathTrainerUser(username, [], [], 0, 0)

            user_repository.insert_new_user(username)

        else:

            print("Rekisteröity käyttäjätunnus.")
            print("jos et ole itse rekisteröinyt tätä tunnusta,")
            print("keskeytä ohjelman käyttö päävalikossa X")
            print("ja kirjaudu uudelleen eri tunnuksella.")
            input("Jatka >> ")


            userdata = user_repository.find_user(username)

            started = string_to_list(userdata[2])

            finished = string_to_list(userdata[3])

            corrects = userdata[4]

            tries = userdata[5]

            trainee = MathTrainerUser(
                username, started, finished, corrects, tries)


        return trainee

import os

from entities.definitions import COMMANDS,  COMMANDS_ADMIN, MAXLEVELS
# Vakiot, joita käytetään päävalikon esittämiseen, ja harjoituskokonaisuuksien tasojen lukumäärä
# tiedostoa päivitetään aina lisättäessä uusi harjoituskokonaisuus

from entities.user import MathTrainerUser
# yksittäistä käyttäjää kuvaava luokka

from entities.session import MathTrainerSession
# meneillään olevaa harjoitusta kuvaava luokka

from services.utilities import string_to_list

from repositories.user_repository import user_repository
# Käyttäjätietohin liittyvä tietokantaoperaatiot

from repositories.session_repository import session_repository
# Harjoituksen tietoihin liittyvät tietokantaoperaatiot

from ui.admin import MathTrainerAdmin
# Hallinnointi

class MathTrainer:

    def show_main_menu(self, trainee):

        print(trainee)

        for command in COMMANDS:

            print(command, ":", COMMANDS[command])


    def action(self, trainee, choice):

        if choice == "O":

            self._help()

        elif choice == "Y":

            mathtrainer_admin = MathTrainerAdmin()
            mathtrainer_admin._start()

        else:

            self.begin_practising(int(choice), trainee)


    def begin_practising(self, drill, trainee):
        # drill harjoituksen numero, trainee käyttäjä

        if drill not in trainee.practise_finished():
            # Käyttäjä ei ole tehnyt harjoitusta loppuun
            if drill in trainee.practise_started():

                correct, tries, level, correct_at_level, tries_at_level = session_repository.find_session_of_user(
                    trainee.username(), drill)
                # Haetaan käyttäjän trainee.username() harjoitusta drill vastaavan korkeimman level tiedot tietokannasta
                session = MathTrainerSession(
                    trainee.username(), drill, level)
                session.set_corrects_and_tries(correct, tries,correct_at_level, tries_at_level )
            else:
                # 1. harjoituskerta
                trainee.practise_started_append(drill)
                session = MathTrainerSession(
                    trainee.username(), drill, 1)
                session.to_database_new()
            session.begin_practise(trainee)
            # Aloitetaan tai jatketaan harjoitusta

        else:
            # Käytetyllä käyttäjätunnuksella on jo tehty kaikki harjoituksen tehtävät
            self._all_done(drill)

    def _all_done(self, drill):
        os.system('clear')
        print(f"Olet tehnyt kaikki tehtävät harjoituksissa {drill}.")
        print("Jos haluat tehdä tämän harjoituksen tehtäviä uudelleen, valitse uusi käyttäjätunnus.")
        input("Jatka >> ")

    def shutdown(self, trainee):
        os.system('clear')
        print("Lopetetaan ohjelman suoritus.")
        print("Käyttäjän tiedot:")
        print(trainee)

    def _help(self):
        os.system('clear')
        print("Valintasi: O")
        print("Laskutehtävien suorituksen voi keskeyttää antamalla laskun vastaukseksi tyhjän.")
        print()
        print("Osassa tehtävissä on 'laskin' käytössä:")
        print("Kirjoita alkuun = ja sitten laskutoimituksia +, -, *, / sisältävä lauseke.")
        print("Esimerkiksi =2*(3+4) tai = (4 - 2) / -2.")
        print()
        print("Kehotteeseen Jatka >> voi vastata Enterillä.")
        print()

    def problems_with_databases(self):

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

import os

from entities.definitions import DESCRIPTION, COMMANDS, MAXLEVELS
# Vakiot, joita käytetään päävalikon esittämiseen, ja harjoituskokonaisuuksien tasojen lukumäärä
# tiedostoa päivitetään aina lisättäessä uusi harjoituskokonaisuus

from entities.user import MathTrainerUser
# yksittäistä käyttäjää kuvaava luokka

from entities.session import MathTrainerSession
# meneillään olevaa harjoitusta kuvaava luokka

from services.utilities import string_to_list, string_to_dict

from repositories.user_repository import user_repository
# Käyttäjätietohin liittyvä tietokantaoperaatiot

from repositories.session_repository import session_repository
# Harjoituksen tietoihin liittyvät tietokantaoperaatiot


class MathTrainer:
    # Käyttöliittymää vastaava luokka
    def mainmenu(self):

        trainee = self._login()
        # kirjaudutaan järjestelmään uutena tai vanhana käyttäjänä
        # harjoituksen tekijan tiedot luokan MathTrainerUse mukaisesti

        while True:
            self._show_main_menu(trainee)
            # Näytetään valikko

            choice = input("Valinta: ").upper()
            if not choice in COMMANDS:
                # Tarkistetaan, tunnistetaanko annettu komento
                os.system('clear')
                print(choice, "on virheellinen komento")
                print("Valitse uudelleen")
            elif choice == "X":
                self._shutdown(trainee)
                # Lopetetaan istunto.
                break
            elif choice == "Y":
                self._maintenance()
            else:
                self._action(trainee, choice)
                # Valitaan jokin harjoituksista tai tulostetaan ohjeet

    def _show_main_menu(self, trainee):
        # Päävalikko
        print(trainee)
        # Näytetään käyttäjän tiedot

        for command in COMMANDS:
            print(command, ":", COMMANDS[command])

    def _show_admin_menu(self):

        print("1:   kaikki käyttäjänimet")
        print("2:   kaikki suoritukset")
        print("3:   kaikki annetun käyttäjän suoritukset")
        print("4:   kaikki annetun harjoituksen suoritukset")
        print("muu: palataan päävalikkoon")


    def _maintenance(self):

        print("TODO Kysytään salasanaa")

        self._show_admin_menu()

        ans = input("Valintasi ")

        if ans not in ['1', '2', '3', '4']:
            return

        if ans == '1':
            print("Kaikki käyttäjätunnukset")
            print(user_repository.find_all_usernames())
            input("Enter paluu päävalikkoon.")

        if ans == '2':
            print("Kaikki suoritukset")
            print(session_repository.find_all_sessions())
            input("Enter paluu päävalikkoon.")

        return

    def _action(self, trainee, choice):
        # Ohjeet tai jokin harjoituksista
        if choice == "O":
            # Ohjeita
            self._help()
        else:
            self.begin_practising(int(choice), trainee)
            # Aloitetaan harjoitus

    def begin_practising(self, drill, trainee):
        # drill harjoituksen numero, trainee käyttäjä

        if drill not in trainee.practise_finished():
            # Käyttäjä ei ole tehnyt harjoitusta loppuun
            if drill in trainee.practise_started():

                level = trainee.practise_level(drill)

                correct, tries, correct_at_level, tries_at_level = session_repository.find_session_of_user(trainee.username(), drill, level)

                session = MathTrainerSession(
                    trainee.username(), drill, correct, tries, level, MAXLEVELS[drill],correct_at_level, tries_at_level)
            else:
                # 1. harjoituskerta
                trainee.practise_started_append(drill)
                session = MathTrainerSession(
                    trainee.username(), drill, 0, 0, 1, MAXLEVELS[drill], 0, 0)
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
        input("Enter paluu päävalikkoon.")

    def _shutdown(self, trainee):
        os.system('clear')
        print("Lopetetaan ohjelman suoritus.")
        print("Käyttäjän tiedot:")
        print(trainee)

    def _help(self):
        os.system('clear')
        print("Valintasi: O")
        print("TODO tarvittavia ohjeita")

    def _login(self):

        os.system('clear')

        username = input("Anna käyttäjätunnus (vähintään viisi merkkiä) ")

        while len(username) < 5:
            print("Liian lyhyt käyttäjätunnus, oltava vähintään 5 merkkiä")
            username = input("Anna käyttäjätunnus (vähintään viisi merkkiä) ")

        if user_repository.find_user(username) is None:

            print("Uusi käyttäjätunnus.")

            trainee = MathTrainerUser(username, {}, [], 0, 0)

            # Tallennetaan uusi käyttäjä tietokantaan.
            user_repository.insert_new_user(username)

        else:

            print("Rekisteröity käyttäjätunnus.")
            print("jos et ole itse rekisteröinyt tätä tunnusta,")
            print("keskeytä ohjelman käyttö päävalikossa X")
            print("ja kirjaudu uudelleen eri tunnuksella.")
            input("Jatka Enter ")

            # Etsitään rekisteröityneen käyttäjän tiedot tietokannasta.
            userdata = user_repository.find_user(username)

            started = string_to_dict(userdata[2])

            finished = string_to_list(userdata[3])

            corrects = userdata[4]

            tries = userdata[5]

            trainee = MathTrainerUser(
                username, started, finished, corrects, tries)

        return trainee

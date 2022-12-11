import os

from entities.definitions import DESCRIPTION, COMMANDS, MAXLEVELS
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
        print("2:   kaikki käyttäjät harjoitustietoineen")
        print("3:   kaikki suoritukset")
        print("4:   kaikki annetun käyttäjän suoritukset")
        print("5:   kaikki annetun harjoituksen suoritukset")
        print("muu: palataan päävalikkoon")

    def _maintenance(self):

        print("TODO Kysytään salasanaa")

        self._show_admin_menu()

        ans = input("Valintasi ")
        print("\n")

        while ans in ['1', '2', '3', '4', '5']:

            if ans == '1':
                user_repository.print_all_users()

            if ans == '2':
                user_repository.print_all_users_with_practises()

            if ans == '3':
                session_repository.print_all_sessions()

            if ans == '4':
                username = input("Käyttäjä, jonka tiedot annetaan > ")
                session_repository.print_all_sessions_of_user(username)

            if ans == '5':
                practise = input("Harjoitus, jonka tiedot annetaan > ")
                session_repository.print_all_sessions_of_practise(practise)

            print("\n")
            input("Enter paluu valikkoon.")

            self._show_admin_menu()

            ans = input("Valintasi ")

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
        input("Enter paluu päävalikkoon.")

    def _shutdown(self, trainee):
        os.system('clear')
        print("Lopetetaan ohjelman suoritus.")
        print("Käyttäjän tiedot:")
        print(trainee)

    def _help(self):
        os.system('clear')
        print("Valintasi: O")
        print("Lskutehtävien suorituksen voi keskeyttää antamalla laskun vastaukseksi tyhjän.")
        print()
        print("Osassa tehtävissä on 'laskin' käytössä:")
        print("Kirjoita alkuun = ja sitten laskutoimituksia +, -, *, / sisältävä lauseke.")
        print("Esimerkiksi =2*(3+4) tai = (4 - 2) / -2.")
        print()
        print("Kehotteeseen Jatka >> voi vastata Enterillä.")
        print()

    def _login(self):

        os.system('clear')

        username = input("Anna käyttäjätunnus (vähintään viisi merkkiä) ")

        while len(username) < 5:
            print("Liian lyhyt käyttäjätunnus, oltava vähintään 5 merkkiä")
            username = input("Anna käyttäjätunnus (vähintään viisi merkkiä) ")

        if user_repository.find_user(username) is None:

            print("Uusi käyttäjätunnus.")

            trainee = MathTrainerUser(username, [], [], 0, 0)

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

            started = string_to_list(userdata[2])

            finished = string_to_list(userdata[3])

            corrects = userdata[4]

            tries = userdata[5]

            trainee = MathTrainerUser(
                username, started, finished, corrects, tries)

        return trainee

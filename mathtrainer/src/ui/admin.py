import os
from entities.definitions import COMMANDS_ADMIN
from repositories.user_repository import user_repository
from repositories.session_repository import session_repository
from services.printing_from_databases import printing_service


class MathTrainerAdmin:

    def _show_admin_menu(self):

        for command in COMMANDS_ADMIN:

            print(command, ":", COMMANDS_ADMIN[command])

    def _start(self):

        os.system('clear')

        while True:

            self._show_admin_menu()

            choice = input("Valinta: ")

            if not choice in COMMANDS_ADMIN:

                print(choice, "on virheellinen komento")
                print("Valitse uudelleen")

            elif choice == "0":

                break

            else:
                self._admin_action(choice)


    def _admin_action(self,choice):

        if choice == '1':

            printing_service.print_all_users()

        if choice == '2':

            printing_service.print_all_users_with_practises()

        if choice == '3':

            printing_service.print_all_sessions()

        if choice == '4':

            username = input("Käyttäjä, jonka tiedot annetaan > ")
            printing_service.print_all_sessions_of_user(username)

        if choice == '5':

            practise = input("Harjoitus, jonka tiedot annetaan > ")
            printing_service.print_all_sessions_of_practise(practise)

        if choice == '6':

            practise = input("Harjoitus, jonka tilasto annetaan > ")
            printing_service.print_statistics_of_practise(practise)

        if choice == '7':

            username = input("Poistettava käyttäjätunnus > ")

            print(f"Poistetaan kaikki käyttäjän {username} tiedot.")
            ans = input(" Oletko varma, K = kyllä, K/muu > ")

            if ans != 'K':

                print("Peruutettiin poisto.")

            else:

                user_repository.delete_user(username)
                session_repository.delete_all_sessions_of_user(username)



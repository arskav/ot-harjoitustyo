import os

from entities.definitions import COMMANDS

from ui.mathtrainer import MathTrainer

def main():
    """Sisäänkirjautuminen ja päävalikko
    """

    mathtrainer = MathTrainer()

    if mathtrainer.problems_with_databases():

        print("Ongelmia tietokantojen suhteen.")
        print("Oletko luonut ne komennolla build?")
        print("Ks. käyttöohje.")

        return

    trainee = mathtrainer.login()

    while True:

        mathtrainer.show_main_menu(trainee)

        choice = input("Valinta: ").upper()

        if choice == "X":

            mathtrainer.shutdown(trainee)
            break

        if not choice in COMMANDS:

            os.system('clear')
            print(choice, "on virheellinen komento")
            print("Valitse uudelleen")

        else:

            mathtrainer.action(trainee, choice)

if __name__ == "__main__":
    main()

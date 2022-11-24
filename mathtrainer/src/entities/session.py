import os
from entities.definitions import DESCRIPTION
# Harjoitusten kuvaukset

from services.utilities import return_to_menu
# vakiokysymys vaiheessa, jossa jonkun harjoituksen tietyn tason kysymykset on tehty

import practises.practises1
import practises.practises2
# Näitä lisätään sitä mukaa kun tulee lisää harjoituskokonaisuuksia


class MathTrainerSession:
    def __init__(self, username, practise, maxlevel):
        self._user = username
        self._practise = practise
        self._correct = 0
        self._tries = 0
        self._level = 1
        self._maxlevel = maxlevel
        self._correct_at_level = 0
        self._tries_at_level = 0

    def __str__(self):

        string = self._user
        string += " harjoitus " + str(self._practise)
        string += "\n" + "Yrityksiä tässä harjoituksessa " + \
            str(self._tries) + ", joista "
        string += "oikeita vastauksia " + str(self._correct)
        string += "\nTaso " + str(self._level) + "/" + str(self._maxlevel) + \
            ", tällä tasolla yrityksiä " + \
            str(self._tries_at_level) + ", joista "
        string += "oikeita vastauksia " + str(self._correct_at_level)

        return string

    def level(self):
        return self._level

    def correct(self):
        return self._correct

    def tries(self):
        return self._tries

    def correct_at_level(self):
        return self._correct_at_level

    def tries_at_level(self):
        return self._tries_at_level

    def begin_practise(self, drill, trainee):

        os.system('clear')
        print(DESCRIPTION[drill])
        print("Nyt ei kuitenkaan vielä varsinaisia tehtäviä")
        # Tässä voisi olla myös enemmänkin tehtäväkokonaisuuden esittelyä

        # lisätään tieto, että harjoitus drill aloitettu
        # tässä vaiheessa ohjelmaa tämä aina aloituskerta, koska tietoja ei tallenneta vielä
        # Jatkossa haetaan vanhat tiedot tietokannasta.
        if drill not in trainee.practise_started():
            trainee.practise_started_append(drill)

        self.do_practise(drill, trainee)

    def do_practise(self, drill, trainee):
        # trainee on harjoituksen tekijä, drill harjoituksen nro ja self harjoituksen suoritustiedot

        training = True
        cancelled = False


        while training and self._level <= self._maxlevel:

            if drill == 1:
                practises.practises1.do_practise(self, trainee, cancelled)
                # Tehdään harjoitus 1 tasolla level,
                # session: harjoituskerran tiedot,
                # trainee: käyttäjän harjoittelua koskevat tiedot

            #if drill == 2:
            #    practises.practises2.do_practise(self, trainee, cancelled)
            #vrt. yllä

            # HARJOITUKSEN LISÄÄMINEN
            # jos esim. numero 100
            # if drill == 100:
            #       practises100.do_practise(session, trainee)
            # tiedostossa paractises100 funktio do_practise, joka sisältää harjoituksen.

            if self._level - 1 == self._maxlevel:
                print(f"Olet tehnyt kaikki tehtävät harjoituksissa {drill}.")
                print("Jos haluat tehdä tämän harjoituksen tehtäviä uudelleen,")
                print("valitse uusi käyttäjätunnus.")
                print("TODO tallennetaan tilastointia varten harjoituskerran tiedot tietokantaan.")
                print("taso on nyt max taso + 1 sen merkiksi, että harjoitus tehty loppuun")
                # print(self) tarkistusta varten
                # Tähän voisi lisätä yhteenvedon harjoitusten sujumisesta
                input("Enter paluu päävalikkoon.")

                # päivitetään tieto tästä käyttäjän tietoihin
                trainee.practise_finished_append(drill)
                break

            if cancelled or (return_to_menu() == 'X'):
                print(self)
                training = False
                print("TODO tallennetaan harjoituskerran tiedot tietokantaan")
                input("Jatka ")

    def new_attempt(self):
        # uusi yritys, kasvatetaan yritysten sekä harjoitus- että tasokohtaista lukumäärää yhdellä
        self._tries += 1
        self._tries_at_level += 1

    def level_up(self):
        # siirrytään seuraavalle tasolle
        # Tulostetaan tilanne
        print(self)
        print("Siirrytään seuraavalle tasolle")

        self._level += 1
        # nollataan tason yritysten ja oikeiden vastausten lkm
        self._tries_at_level = 0
        self._correct_at_level = 0

    def correct_up(self):
        # oikea vastaus, kasvatetaan oikeiden vastausten lukumäärää yhdellä
        # tähän voi lisätä muutakin toimintaa
        self._correct += 1
        self._correct_at_level += 1

import os
from entities.definitions import DESCRIPTION
# Harjoitusten kuvaukset

import practises.practises1
# Näitä lisätään sitä mukaa kun tulee lisää harjoituskokonaisuuksia

import practises.practises2
# Näitä lisätään sitä mukaa kun tulee lisää harjoituskokonaisuuksia

from services.utilities import practise_done
# vakiokysymys vaiheessa, jossa jonkun harjoituksen tietyn tason kysymykset on tehty

from services.utilities import return_to_menu


class MathTrainerSession:
    def __init__(self, username, practise, correct, tries, level, maxlevel):
        self._user = username
        self._practise = practise
        self._correct = correct
        self._tries = tries
        self._level = level
        self._maxlevel = maxlevel
        self._correct_at_level = 0
        self._tries_at_level = 0
        self._ongoing = True

    def __str__(self):

        string = self._user
        string += " harjoitus " + str(self._practise)
        string += "\n" + "Yrityksiä tässä harjoituksessa " + \
            str(self._tries) + ", joista "
        string += "oikeita vastauksia " + \
            str(self._correct) + \
            " TODO tämä ei nollaudu aloitettaessa uudelleen päävalikon kautta."
        string += "\nTaso " + str(self._level) + "/" + str(self._maxlevel) + \
            ", tällä tasolla yrityksiä " + \
            str(self._tries_at_level) + ", joista "
        string += "oikeita vastauksia " + str(self._correct_at_level)

        return string

    def practise(self):
        return self._practise

    def level(self):
        return self._level

    def maxlevel(self):
        return self._maxlevel

    def correct(self):
        return self._correct

    def tries(self):
        return self._tries

    def correct_at_level(self):
        return self._correct_at_level

    def tries_at_level(self):
        return self._tries_at_level

    def ongoing(self):
        return self._ongoing

    def set_ongoing(self, truthvalue):
        self._ongoing = truthvalue

    def begin_practise(self, trainee):

        os.system('clear')
        drill = self.practise()
        print(DESCRIPTION[drill])
        # Tässä voisi olla myös enemmänkin tehtäväkokonaisuuden esittelyä

        # lisätään tieto, että harjoitus drill aloitettu
        # tässä vaiheessa ohjelmaa tämä aina aloituskerta, koska tietoja ei tallenneta vielä
        # Jatkossa haetaan vanhat tiedot tietokannasta.
        if drill not in trainee.practise_started():
            trainee.practise_started_append(drill)

        self.do_practise(trainee)

    def do_practise(self, trainee):
        # trainee on harjoituksen tekijä, drill harjoituksen nro ja self harjoituksen suoritustiedot

        correct = 0
        tries = 0
        successive_correct = 0
        is_cancelled = False
        drill = self.practise()

        while self.ongoing():

            print("---------------------------------------")
            print(self)

            if drill == 1:
                is_correct, is_cancelled, is_finish = practises.practises1.question(
                    successive_correct, self.level())

            if drill == 2:
                is_correct, is_cancelled, is_finish = practises.practises2.question(
                    successive_correct, self.level())

            # lisäys
            # if drill == 3:
            #    is_correct, is_cancelled, is_finish = practises.practises3.question(
            #        successive_correct, self.level())

            if is_cancelled:
                self.set_ongoing(False)
                break

            self.new_attempt()
            tries += 1
            # Ainakin yritetty vastata

            if is_correct:
                self.correct_up()
                correct += 1
                successive_correct += 1
            else:
                successive_correct = 0

            if is_finish:
                # Lopetusehdon toteutuessa siirrytään seuraavalle tasolle
                print("Olet tehnyt kaikki tämän tason harjoitukset.")
                self.level_up()
                successive_correct = 0

            if is_finish and self.level() <= self.maxlevel():
                if return_to_menu():
                    self.set_ongoing(False)

                # HARJOITUKSEN LISÄÄMINEN
                # jos esim. numero 100
                # if drill == 100:
                #       practises100.do_practise(session, trainee)
                # tiedostossa paractises100 funktio do_practise, joka sisältää harjoituksen.

            if is_cancelled or (self.level() > self.maxlevel()):
                self.set_ongoing(False)
                print("TODO tallennetaan harjoituskerran tiedot tietokantaan")
                input("Jatka ")

        # Päivitetään käyttäjän kokonaistilanne
        trainee.update_total(correct, tries, drill, self.level())

        if self._level - 1 == self._maxlevel:
            practise_done(drill)
            # päivitetään tieto tästä käyttäjän tietoihin
            trainee.practise_finished_append(drill)

        # Tallennus tietokantaan
        trainee.to_database()
        # TO DO harjoituskerran tiedot tallennetaan tilastointia varten

    def new_attempt(self):
        # uusi yritys, kasvatetaan yritysten sekä harjoitus- että tasokohtaista lukumäärää yhdellä
        self._tries += 1
        self._tries_at_level += 1

    def level_up(self):
        # Siirrytään seuraavalle tasolle ja
        # ja kysytään, jatketaanko harjoittelua sillä,
        # jos edellinen ei ollut jo viimeinen.

        self._level += 1
        # nollataan tason yritysten ja oikeiden vastausten lkm
        self._tries_at_level = 0
        self._correct_at_level = 0

    def correct_up(self):
        # oikea vastaus, kasvatetaan oikeiden vastausten lukumäärää yhdellä
        # tähän voi lisätä muutakin toimintaa
        self._correct += 1
        self._correct_at_level += 1

import os
from entities.definitions import DESCRIPTION, MAXLEVELS
# Harjoitusten kuvaukset

import practises.practises1

import practises.practises2

#import practises.practises3 ei valmis

import practises.practises4
# Näitä lisätään sitä mukaa kun tulee lisää harjoituskokonaisuuksia

from services.utilities import practise_done, return_to_menu

from repositories.session_repository import session_repository
# Harjoituksen tietoihin liittyvät tietokantaoperaatiot

#Kun harjoituksia tulee lisää, päivitä tämä
PRACTISES = {1: practises.practises1.question, 2: practises.practises2.question, \
    3: None, 4: practises.practises4.question
}

class MathTrainerSession:
    def __init__(self, username, practise, correct, tries, level, \
        correct_at_level, tries_at_level):
        self._user = username
        self._practise = practise
        self._correct = correct
        self._tries = tries
        self._level = level
        self._correct_at_level = correct_at_level
        self._tries_at_level = tries_at_level
        self._ongoing = True

    def __str__(self):

        string = self._user
        string += " harjoitus " + str(self._practise)
        string += "\n" + "Yrityksiä tässä harjoituksessa " + \
            str(self._tries) + ", joista "
        string += "oikeita vastauksia " + \
            str(self._correct)
        string += "\nTaso " + str(self._level) + "/" + str(self.maxlevel()) + \
            ", tällä tasolla yrityksiä " + \
            str(self._tries_at_level) + ", joista "
        string += "oikeita vastauksia " + str(self._correct_at_level)

        return string

    def user(self):
        return self._user

    def practise(self):
        return self._practise

    def level(self):
        return self._level

    def maxlevel(self):
        return MAXLEVELS[self.practise()]

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
        # if drill not in trainee.practise_started():
        #    trainee.practise_started_append(drill)
        #    self.to_database_new()

        self.do_practise(trainee)

    def _initialize_doing_practise(self):
        correct = 0
        tries = 0
        successive_correct = 0
        is_cancelled = False
        drill = self.practise()

        return correct, tries, successive_correct, is_cancelled, drill



    def do_practise(self, trainee):
        # trainee on harjoituksen tekijä, drill harjoituksen nro ja self harjoituksen suoritustiedot

        correct, tries, successive_correct, is_cancelled, drill = self._initialize_doing_practise()

        if drill == 3:
            #Harjoitus 3 ei ole valmis
            return

        while self.ongoing():

            print("---------------------------------------")
            print(self)

            is_correct, is_cancelled, is_finish = PRACTISES[drill](
                    successive_correct, self.level())

            if is_cancelled:
                self.cancel()
                break

            self.new_attempt()
            tries += 1
            # Ainakin yritetty vastata

            successive_correct, correct = self.correct_or_not(
                is_correct, successive_correct, correct
                )

            if is_finish:
                successive_correct = 0
                self.finish()



        # Päivitetään käyttäjän kokonaistilanne
        #tämän voisi hoitaa luokan MathTrainerUser metodilla
        trainee.update_total(correct, tries)

        if self.level() - 1 == self.maxlevel():
            practise_done(drill)
            # päivitetään tieto tästä käyttäjän tietoihin
            trainee.practise_finished_append(drill)

        # Tallennus tietokantaan
        trainee.to_database()


    def to_database_new(self):
        session_repository.insert_new_session(self.user(), self.practise(), self.correct(
        ), self.tries(), self.level(), self.correct_at_level(), self.tries_at_level())

    def update_database(self):
        session_repository.update_session(self.user(), self.practise(), self.correct(
        ), self.tries(), self.level(), self.correct_at_level(), self.tries_at_level())

    def new_attempt(self):
        # uusi yritys, kasvatetaan yritysten sekä harjoitus- että tasokohtaista lukumäärää yhdellä
        self._tries += 1
        self._tries_at_level += 1

    def level_up(self):
        # Siirrytään seuraavalle tasolle ja
        # ja kysytään, jatketaanko harjoittelua,
        # jos edellinen ei ollut jo viimeinen.

        self._level += 1
        # nollataan tason yritysten ja oikeiden vastausten lkm
        self._tries_at_level = 0
        self._correct_at_level = 0

    def correct_or_not(self, is_correct, successive_correct, correct):
        if is_correct:
            self.correct_up()
            correct += 1
            successive_correct += 1
        else:
            successive_correct = 0

        return successive_correct, correct

    def finish(self):
        # Lopetusehdon toteutuessa siirrytään seuraavalle tasolle
        #tai jos ollaan viimeisellä tasolla, lopetetaan harjoitus
        self.update_database()
        self.level_up()

        if self.level() <= self.maxlevel():
            self.to_database_new()
            if return_to_menu():
                self.set_ongoing(False)
        else:
            self.set_ongoing(False)
            print("Olet tehnyt kaikki tämän tason harjoitukset.")
            input("Jatka ")





    def correct_up(self):
        # oikea vastaus, kasvatetaan oikeiden vastausten lukumäärää yhdellä
        # tähän voi lisätä muutakin toimintaa
        self._correct += 1
        self._correct_at_level += 1

    def cancel(self):

        self.set_ongoing(False)
        print("Keskeytetty")
        print(self)
        input(" >> ")
        self.update_database()

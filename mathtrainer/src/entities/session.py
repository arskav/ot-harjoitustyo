import os
from entities.definitions import DESCRIPTION
# Harjoitusten kuvaukset

import practises.practises1
# Näitä lisätään sitä mukaa kun tulee lisää harjoituskokonaisuuksia

from services.utilities import practise_done
# vakiokysymys vaiheessa, jossa jonkun harjoituksen tietyn tason kysymykset on tehty


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
        correct = 0
        tries = 0

        while training and self._level <= self._maxlevel:

            if drill == 1:
                correct, tries, cancelled = practises.practises1.do_practise(
                    self, correct, tries, cancelled)
                # Tehdään harjoitus 1 aloittaen tasosta self._level,
                # session: harjoituskerran tiedot,
                # kutsuttavan aliohjelman täytyy kasvattaa oikeiden vastausten
                # ja yritysten lukumäärää ja tehtävätasoa.
                # Kun harjoituskokonaisuuksieen lukumäärä kasvaa, nämä toimenpiteet
                # pitäisi tehdä varsinaisen harjoituksen sisältävän aliohjelman ulkopuolella
                # omassa aliohjelmassa.

            if drill == 2:
                correct, tries, cancelled = practises.practises1.do_practise(
                    self, correct, tries, cancelled)
                # Tämä on testausta varten sama kuin harjoitus 1

            # HARJOITUKSEN LISÄÄMINEN
            # jos esim. numero 100
            # if drill == 100:
            #       practises100.do_practise(session, trainee)
            # tiedostossa paractises100 funktio do_practise, joka sisältää harjoituksen.

            if cancelled:
                training = False
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

        if self._level <= self._maxlevel:
            os.system('clear')
            print(self)
            print("Olet tehnyt kaikki tämän tason harjoitukset.")

        self._level += 1
        # nollataan tason yritysten ja oikeiden vastausten lkm
        self._tries_at_level = 0
        self._correct_at_level = 0

    def correct_up(self):
        # oikea vastaus, kasvatetaan oikeiden vastausten lukumäärää yhdellä
        # tähän voi lisätä muutakin toimintaa
        self._correct += 1
        self._correct_at_level += 1

import os

from entities.definitions import DESCRIPTION, MAXLEVELS
# Harjoitusten kuvaukset

import practises.practises1

import practises.practises2

import practises.practises3

import practises.practises4
# Näitä lisätään sitä mukaa kun tulee lisää harjoituskokonaisuuksia

from services.utilities import return_to_menu

from services.practiseutilities import doing_practise

from repositories.session_repository import session_repository
# Harjoituksen tietoihin liittyvät tietokantaoperaatiot

#Kun harjoituksia tulee lisää, päivitä tämä
PRACTISES = {1: practises.practises1.question, 2: practises.practises2.question, \
    3: practises.practises3.question, 4: practises.practises4.question
}

class MathTrainerSession:
    """Luokka, joka kuvaa harjoitussessiota eli yhden harjoituskokonaisuuden
    yhden tason suorittamista.
    """

    def __init__(self, username, practise, level):
        """Luokan konstruktori, joka luo uuden harjoitussession.

        Args:
            username (string): käyttäjätunnus eli harjoituksen suorittaja.
            practise (int): harjoitus (järjestysnumero).
            level (int): harjoituksen taso.
        """

        self._user = username
        self._practise = practise
        self._correct = 0
        self._tries = 0
        self._level = level
        self._correct_at_level = 0
        self._tries_at_level = 0
        self._ongoing = True

    def __str__(self):
        """Harjoitussession tietojen tulostus.

        Returns:
            sring: harjoitus, yrityksiä ja oikeita vastauksia koko harjoituksessa,
                taso ja tasojen lukumäärä, yrityksiä ja oikeita vastauksia tasolla.
        """
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
        """Palauttaa käyttäjätunnuksen."""
        return self._user

    def practise(self):
        """Palauttaa harjoituksen numeron."""
        return self._practise

    def level(self):
        """Palauttaa harjoituksen tason."""
        return self._level

    def maxlevel(self):
        """Palauttaa harjoituksen tasojen lukumäärän."""
        return MAXLEVELS[self.practise()]

    def correct(self):
        """Palauttaa oikeiden vastauksen lukumäärän koko harjoituksessa."""
        return self._correct

    def tries(self):
        """Palauttaa yritysten lukumäärän koko harjoituksessa."""
        return self._tries

    def correct_at_level(self):
        """Palauttaa oikeiden vastauksen lukumäärän tasolla."""
        return self._correct_at_level

    def tries_at_level(self):
        """Palauttaa yritysten lukumäärän tasolla."""
        return self._tries_at_level

    def ongoing(self):
        """Palauttaa tiedon, jatkuuko harjoitus (True) vai ei (False)."""
        return self._ongoing

    def set_corrects_and_tries(self, correct,tries, correct_at_level, tries_at_level):
        """Päivittää oikeiden vastausten ja yritysten lukumäärän.

        Args:
            correct (int): oikeiden vastausten lkm harjoituksessa.
            tries (int): yritysten lkm harjoituksessa.
            correct_at_level (int): oikeiden vastausten lkm tasolla.
            tries_at_level (int): yritysten lkm tasolla.
        """

        self._correct = correct
        self._tries = tries
        self._correct_at_level = correct_at_level
        self._tries_at_level = tries_at_level

    def set_ongoing(self, truthvalue):
        """Päivittää tiedonharjoituksen jatkumisesta.

        Args:
            truthvalue (Booelan): True jatkuu, False ei jatku.
        """
        self._ongoing = truthvalue

    def begin_practise(self, trainee):
        """Aloittaa harjoituksen (tason) tekemisen.

        Args:
            trainee (MathTrainer): harjoituksen tekijän tiedot.
        """

        os.system('clear')
        drill = self.practise()
        print(DESCRIPTION[drill])
        # Tässä voisi olla myös enemmänkin tehtäväkokonaisuuden esittelyä

        doing_practise(self, trainee, PRACTISES[drill])
        """Kutsuu harjoituksen tekemistä suorittavan aliohjelman.

        Args:
            trainee (MathTrainer): harjoituksen tekijän tiedot.
            PRACTISES[drill] (string) harjoitusta numero drill vastaava ohjelma.
        """

    def new_attempt(self):
        """Kasvattaa yritysten sekä harjoitus- että tasokohtaista lukumäärää yhdellä."""

        self._tries += 1
        self._tries_at_level += 1

    def level_up(self):
        """Siirtyy seuraavalle tasolle ja kysyy, jatketaanko harjoittelua,
        jos ei oltu jo viimeisellä tasolla.
        """

        self._level += 1
        self._tries_at_level = 0
        self._correct_at_level = 0

    def correct_or_not(self, is_correct, successive_correct, correct):
        """Päivittää (tason) oikeiden vastausten ja peräkkäisten oikeiden
        vastausten lukumäärät.

        Args:
            is_correct (bool): onko vastaus oikein (True) vai väärin.
            successive_correct (int): peräkkäisten oikeiden vastausten vanha lkm.
            correct (int): oikeiden vastausten vanha lkm.

        Returns:
            (int, int): päivitetty (peräkkäistenoikeiden lkm, oikeiden lkm).
        """
        if is_correct:
            self.correct_up()
            correct += 1
            successive_correct += 1
        else:
            successive_correct = 0

        return successive_correct, correct

    def finish(self):
        """Lopetusehdon toteutuessa siirtyy joko seuraavalle tasolle ja
        kutsuu harjoitussession tiedot tietokantaan tallentavaa metodia
        tai jos ollaan viimeisellä tasolla, lopetetaan harjoitus.
        """

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
        """Kasvattaa harjoituksen ja tason oikeiden vastausten lukumääriä yhdellä."""

        self._correct += 1
        self._correct_at_level += 1

    def cancel(self):
        """Keskeyttää harjoituksen ja kutsuu harjoitussession tiedot tietokantaan
        tallentavaa metodia."""

        self.set_ongoing(False)
        print("Keskeytetty")
        print(self)
        input(" >> ")
        self.update_database()

    def to_database_new(self):
        """Tallentaa harjoitussession tiedot tietokantaan."""

        session_repository.insert_new_session(self)


    def update_database(self):
        """Päivittää harjoitussession tiedot tietokannassa."""

        session_repository.update_session(self)


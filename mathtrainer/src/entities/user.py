from services.utilities import list_to_string

from repositories.user_repository import user_repository



class MathTrainerUser:
    """Luokka, jonka avulla ylläpidetään käyttäjän tietoja

    Attributes:
        _user: käyttäjätunnus
        _practise_started: lista aloitetuista harjoituksista
        _practise_finished: lista loppuun asti tehdyistä harjoituksista
        _correct_total: kaikissa harjoituksissa oikeita vastauksia
        _tries_total: kaikissa harjoituksissa yrityksiä
    """
    def __init__(self, username, started, finished, correct, tries):
        """Luokan konstruktori

        Args:
            username (string): käyttäjätunnus
            started (list): lista aloitetuista harjoituksista
            finished (list): lista loppuun asti tehdyistä harjoituksista
            correct (integer): oikeiden vastausten lukumäärä
            tries (integer): yritysten lukumäärä
        """

        self._user = username
        self._practise_started = started
        self._practise_finished = finished
        self._correct_total = correct
        self._tries_total = tries

    def username(self):
        """Palauttaa käyttäjätunnukset."""

        return self._user

    def practise_started(self):
        """Palauttaa harjoitukset, jotka aloitettu."""

        return self._practise_started

    def practise_level(self, drill):
        """Palauttaa harjoituksen tason.

        Args:
            drill (integer): harjoituksen numero
        """

        return self._practise_started[drill]

    def practise_finished(self):
        """Palauttaa harjoitukset, jotka tehty loppuun."""

        return self._practise_finished

    def practise_started_append(self, drill):
        """Lisää harjoituksen aloitettuihin harjoituksiin.

        Args:
            drill (integer): harjoituksen numero
        """

        self._practise_started.append(drill)

    def practise_finished_append(self, drill):
        """Lisää harjoituksen lopetettuihin harjoituksiin.


        Args:
            drill (integer): harjoituksen numero
        """

        self._practise_finished.append(drill)

    def correct_total(self):
        """Palauttaa käyttäjän kaikkien oikeiden vastausten lukumäärän."""

        return self._correct_total

    def tries_total(self):
        """Palauttaa käyttäjän kaikkien yritysten lukumäärän"""

        return self._tries_total

    def __str__(self):
        """Käyttäjän tietojen tulostus. Käytetään päävalikon yhteydessä."""

        string = "Käyttäjätunnus: " + self._user
        string += "\n" + "Yrityksiä kaikissa harjoituksissa " + \
            str(self._tries_total) + ", joista "
        string += "oikeita vastauksia " + str(self._correct_total) + "\n"

        if len(self.practise_started()) > 0:
            string += "Aloitettu harjoitukset "
            string += list_to_string(self.practise_started())
            string += "."
        else:
            string += "Ei aloitettuja harjoituksia."

        if self.practise_finished() != []:
            string += " Tehty loppuun harjoitukset "
            string += list_to_string(self.practise_finished())
            string += "."
        else:
            string += " Ei loppuun tehtyjä harjoituksia. "

        return string

    def update_total(self, correct, tries):
        """Päivitetään kokonaistilanne meneillään olevaa
        harjoitussessionia koskevista tiedoista.

        Args:
            correct (integer): harjoitussessionissa oikeita
            tries (integer): harjoitussessionissa yrityksiä
        """

        self._correct_total += correct

        self._tries_total += tries

    def to_database(self):
        """Tallennetaan käyttäjän tiedot tietokantaan.

        Returns:
            Testejä varten palautetaan tallennetut tiedot.
        """

        username = self.username()

        started = list_to_string(self.practise_started())

        finished = list_to_string(self.practise_finished())

        corrects = self.correct_total()

        tries = self.tries_total()

        user_repository.update_user(
            username, started, finished, corrects, tries)

        return (username, started, finished, corrects, tries)

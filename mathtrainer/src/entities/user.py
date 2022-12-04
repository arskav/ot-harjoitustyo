from services.utilities import list_to_string

from repositories.user_repository import user_repository
# Käyttäjätietohin liittyvä tietokantaoperaatiot


class MathTrainerUser:

    def __init__(self, username, started, finished, correct, tries):
        self._user = username
        self._practise_started = started
        self._practise_finished = finished
        self._correct_total = correct
        self._tries_total = tries

    def username(self):
        return self._user

    def practise_started(self):
        # Harjoitukset, jotka aloitettu
        return self._practise_started

    def practise_level(self, drill):
        # Aloitetun harjoituksen taso
        return self._practise_started[drill]

    def practise_finished(self):
        return self._practise_finished

    def practise_started_append(self, drill):
        self._practise_started.append(drill)

    def practise_finished_append(self, drill):

        self._practise_finished.append(drill)

    def correct_total(self):
        return self._correct_total

    def tries_total(self):
        return self._tries_total

    def __str__(self):
        # Tulostus ainakin päävalikon yhteydessä
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
        # Päivitetään kokonaistilanne meneillään olevaa harjoituskertaa
        # koskevista tiedoista session: MathTrainerSessions.
        # Tallennetaan tiedot käyttäjän kokonaistilanteesta tietokantaan.
        self._correct_total += correct

        self._tries_total += tries


    def to_database(self):
        # tallennus tietokantaan

        username = self.username()

        started = list_to_string(self.practise_started())

        finished = list_to_string(self.practise_finished())

        corrects = self.correct_total()

        tries = self.tries_total()

        user_repository.update_user(
            username, started, finished, corrects, tries)

        # Tarkistusta varten
        return (username, started, finished, corrects, tries)

from services.utilities import list_to_string

class MathTrainerUser:

    def __init__(self, username, started, finished, correct, tries):
        self._user = username
        self._practise_started = started
        self._practise_finished = finished
        self._correct_total = correct
        self._tries_total = tries

    def practise_started(self):
        return self._practise_started

    def practise_finished(self):
        return self._practise_finished

    def practise_started_append(self, drill):
        self._practise_started.append(drill)

    def practise_finished_append(self, drill):
        self._practise_finished.append(drill)

    def __str__(self):
        # Tulostus ainakin päävalikon yhteydessä
        string = "Käyttäjätunnus: " + self._user
        string += "\n" + "Yrityksiä kaikissa harjoituksissa " + \
            str(self._tries_total) + ", joista "
        string += "oikeita vastauksia " + str(self._correct_total) + "\n"

        if self.practise_started() != []:
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

    def update_total(self, session):
        # Päivitetään kokonaistilanne meneillään olevaa harjoituskertaa
        # koskevista tiedoista session: MathTrainerSessions
        self._correct_total += session.correct_at_level()
        self._tries_total += session.tries_at_level()

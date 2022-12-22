from services.calculator import calculator
from services.practiseutilities import check_if_input_ok

class Question:
    """Luokka, jonka avulla ylläpidetään eräissä harjoituksissa
    yksittäisen kysymyksen tietoja.
    """

    def __init__(
        self, calculator_in_use, question_part, randomize_func,
        correct_answer_func, feedback_func
        ):
        """Luokan konstruktori

        Args:
            _calculator_in_use (Boolean):
                voiko vastaukseksi antaa '=' ja sitten
                lausekkeen, jonka arvon sovellus laskee.
            _variables (list):
                muuttujien arvot, oletusarvoltaan tyhjä.
            _question (dict):
                _question['text']: funktio, jolla kysymysteksti
                    kirjoitetaan, oletusarvoltaan tyhjä funktio.
                _question['prompt']: kehote vastauksen antamiseen.
                _question['mode']: vastauksen oletettu tyyppi,
                käytössä tällä hetkellä 'integer' (kokonaisluku) ja
                'nonnegative' (positiivinen kokonaisluku). Voisi tulla
                lisää 'real' (desimaaliluku).
            _randomize: funktio, joka antaa kysymyksen muuttujille arvot,
                yleensä satunnaislukuja sopivalta väliltä.
                Oletusarvoltaan tyhjä funktio.
            _correct_answer: funktio, joka laskee kysymyksen muuttujista
                oikean vastauksen kysymykseen. Oletusarvoltaan tyhjä funktio.
            _feedback: funktio, joka tulostaa palautteen annettaessa väärä vastaus.
                Oletusarvoltaan tyhjä funktio.

        """

        self._calculator_in_use = calculator_in_use
        self._variables = []
        self._question = question_part
        self._randomize = randomize_func
        self._correct_answer = correct_answer_func
        self._feedback = feedback_func


    def randomize(self):
        """Asettaa kysymyksen muuttujille (yleensä satunnaiset) arvot.

        Args:
            randomice_func: funktio, joka palauttaa lukuja
        """

        self._variables = self._randomize()

    def give_feedback(self):
        """Tulostaa palautteen."""

        self._feedback(*self.values_of_variables())

    def check_answer(self, ans):
        """Tarkistaa, onko vastaus oikein.

        Args:
            ans (int): käyttäjän antama vastaus lukuna.

        Returns:
            _Boolean: onko vastaus oikein.
        """

        return self._correct_answer(*self.values_of_variables()) == ans

    def ask_question(self):
        """Esittää kysymyksen, ottaa siihen vastauksen ja
        tarkistaa, onko vastaus oikean tyyppinen. Jos on, muutta
        merkkijonona annetun vastauksen luvuksi. Jos 'laskin' käytössä,
        laskee merkin '=' jälkeen annetun lausekkeen arvon.

        Returns:
            int: vastaus lukuna, jos vääränlainen syöte, niin None
        """

        self.randomize()

        print('\nTEHTÄVÄ')

        print((self._question['text'])(*self.values_of_variables()))

        print("ANNA VASTAUS")

        if self._calculator_in_use:

            print("Laskin käytössä, kirjoita vastauksen alkuun = ")

        ans = input(self._question['prompt'])

        if ans == '':

            return None

        if ans[0] == '=' and self._calculator_in_use:

            answer =  calculator(ans[1:])

        else:

            answer = check_if_input_ok(ans, self._question['mode'])

        return answer


    def values_of_variables(self):
        """Palauttaa muuttujien arvot.

        Returns:
            list of int: muuttujien arvot listana.
        """

        return self._variables

    def process(self):
        """Käsittelee kysymykseen annetun vastauksen.

        Returns:
            Boolean, Boolean: onko vastaus oikein, onko vastaaminen keskeytetty
        """

        ans = self.ask_question()

        if ans is None:

            return False, True

        is_correct = self.check_answer(ans)

        if is_correct:

            print("Vastaus on oikein.")

        if not is_correct:

            self.give_feedback()

        return is_correct, False

"""'Vanhan' koodaustavan matematiikan harjoitus. Harjoituksessa
annetaan sanallisesti luku ja tehtävänä on kirjoittaa se numeroin.
Harjoitus on tarkoitettu suomea vieraana kielenä puhuville.
"""
import random
from services.utilities import is_number, ask_question
from services.practiseutilities import cancel, correct_answer
from services.number_to_word import number_to_word


FINISH = 2
"""Peräkkäisten oikeiden vastausten lukumäärä, joka riittää harjoituksen
yhden tason suorittamiseksi. Sovelluksen testaamisen helpottamiseksi
tämä asetettu kahdeksi kaikissa harjoituksissa.
"""


def parameters(level):
    """Arvotaan kysyttävä luku. Harjoituksen tason kasvaessa luvun suuruus kasvaa.

    Args:
        level (int): harjoituksen osan taso.

    Returns:
        int: satunnainen ei-negatiivinen kokonaisluku annetulta väliltä.
    """
    if level == 1:

        number = random.randint(0, 10)

    if level == 2:

        number = random.randint(11, 100)

    if level == 3:

        number = random.randint(101, 999)

    if level == 4:

        number = random.randint(1000, 9999)

    if level == 5:

        number = random.randint(10000, 999999)

    if level == 6:

        number = random.randint(100000, 9999999)

    return number


def give_feedback(answer, number, number_as_word):
    """Palaute, jos vastaa väärin.

    Args:
        answer (int): annettu vastaus.
        number (int): oikea vastaus.
        number_as_word (string): kysytty luku kirjoitettuna.
    """
    feedback = f"Väärin, vastasit {answer}, mutta "
    feedback += number_as_word
    feedback += f" on {number}."
    print("="*len(feedback))
    print(feedback)
    print("=" * len(feedback))


def question(successive_correct, level):
    """Harjoituksen kysymyksen esittäminen.

    Args:
        successive_correct (int): peräkkäisten oikeiden vastausten lkm.
        level (int): osaharjoituksen taso.

    Returns:
        (Boolean, Boolean, Boolean): onko vastaus oikein, keskeytetty = False,
            onko osaharjotuksen taso tehty loppuun.

            Jos osaharjoituksen tekeminen on keskeytetty, palautetaan
            (False, True, False) funktion cancel avulla.
    """

    number = parameters(level)

    is_finish = False

    print("Kirjoita numeroin")
    number_as_word = number_to_word(number)
    ans = ask_question(number_as_word, "tulos = ")

    if is_number(ans):
        answer = int(ans)
    else:
        return cancel()

    if answer == number:
        is_correct = True
    else:
        is_correct = False
        give_feedback(answer, number, number_as_word)

    if is_correct:

        is_finish, successive_correct = correct_answer(
            successive_correct, FINISH)

    return (is_correct, False, is_finish)

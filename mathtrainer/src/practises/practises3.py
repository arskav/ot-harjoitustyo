"""'Uuden' koodaustavan mukainen matemaattisen harjoituksen runko.
Tästä on tarkoitus kehittää yleispätevämpi, nyt koodi riippuu tehdyistä
kysymyksistä question1 ja question2.
"""
from services.practiseutilities import correct_answer
from practises.practises3_questions.question1 import question1
from practises.practises3_questions.question2 import question2

FINISH = 2
    """Peräkkäisten oikeiden vastausten lukumäärä, joka riittää harjoituksen yhden tason suorittamiseksi."""


def question(successive_correct, level):
    """Esittää osaharjoituksen tason mukaisen kysymyksen.

    Args:
        successive_correct (int): peräkkäisten oikeiden lkm.
        level (int): osaharjoituksen taso,

    Returns:
        (Boolean, Boolean, Boolean): onko vastaus oikein, onko keskeytetty,
            onko taso tehty loppuun.
    """

    if level == 1:
        is_correct, is_cancelled = question1()
    elif level == 2:
        is_correct, is_cancelled = question2()
    else:
        pass

    is_finish = False

    if is_cancelled:

        return False, True, is_finish

    if is_correct:
        is_finish, successive_correct = correct_answer(successive_correct, FINISH)

    return is_correct, False, is_finish

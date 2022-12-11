from services.practiseutilities import correct_answer
from practises.practises3_questions.question1 import question1
from practises.practises3_questions.question2 import question2
#Uusien tällaisten kysymysten koodaaminen ei tuo juurikaan mitään uutta
#ohjelmoinnin näkökulmasta, joten tässä tyydytään kahteen esimerkkiin.

#QUESTIONS = {1: question1(), 2: question2()}


FINISH = 1
# Kuinka monen peräkkäisen oikean vastauksen jälkeen lopetetaan.

def question(successive_correct, level):

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

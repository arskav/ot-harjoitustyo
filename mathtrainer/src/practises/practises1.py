import random
from services.utilities import is_number, correct_answer, ask_question
from services.practiseutilities import cancel
from services.number_to_word import number_to_word


FINISH = 1  # testaamisen helpottamiseksi riittää yksi oikea
# Kuinka monen peräkkäisen oikean vastauksen jälkeen lopetetaan.


def parameters(level):
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
    feedback = f"Väärin, vastasit {answer}, mutta "
    feedback += number_as_word
    feedback += f" on {number}."
    print("="*len(feedback))
    print(feedback)
    print("=" * len(feedback))


def question(successive_correct, level):

    number = parameters(level)

    is_finish = False

    print("Ilmoita numeroin")
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

import random
from services.utilities import is_number, cancel, draw_two_integers, correct_answer
from services.number_to_word import number_to_word


FINISH = 1  # testaamisen helpottamiseksi riittää yksi oikea
# Kuinka monen peräkkäisen oikean vastauksen jälkeen lopetetaan.


def left_hand_func(level, a, b):

    if level == 1:
        return f"Jos {number_to_word(a)} lippua maksaa {number_to_word(b)} euroa, mitä maksaa yksi lippu", f"{b}/{a}"

    return None


def left_value_func(level, a, b):

    if level == 1:
        return b / a

    return None


def parameters(level):
    if level == 1:
        a, one_item = draw_two_integers(2, 5, 10, 20)
        b = one_item * a

    return a, b


def give_feedback(x, feedback_left, left_value):
    feedback = f"Väärin, vastasit {x}, mutta "
    feedback += feedback_left
    feedback += " = " + f"{left_value}" + "."
    print("=" * len(feedback))
    print(feedback)
    print("=" * len(feedback))


def question(successive_correct, level):

    a, b = parameters(level)

    is_finish = False

    calculation_words, calculation_numbers = left_hand_func(level, a, b)
    length = len(calculation_words)
    print("-" * length)
    print(calculation_words)
    print("-" * length)
    print("Vastaus on kokonaisluku ...-2, -1, 0, 1, 2,...")
    print("Muu vastaus kuin kokonaisluku keskeyttää tehtävän suorittamisen.")
    ans = input("Vastaus on (euroa) ")

    if is_number(ans):
        x = int(ans)
        left_value = int(left_value_func(level, a, b))
    else:
        return cancel()

    if left_value == x:
        is_correct = True
    else:
        is_correct = False
        give_feedback(x, calculation_numbers, left_value)

    if is_correct:

        is_finish, successive_correct = correct_answer(
            successive_correct, FINISH)

    return (is_correct, False, is_finish)

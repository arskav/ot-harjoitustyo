import random
from services.utilities import is_number, cancel, draw_two_integers, correct_answer
from services.number_to_word import number_to_word


FINISH = 1  # testaamisen helpottamiseksi riittää yksi oikea
# Kuinka monen peräkkäisen oikean vastauksen jälkeen lopetetaan.


def left_hand_func(level, a, b):

    if level == 1:
        return f"lukujen {number_to_word(a)} ja {number_to_word(b)} summa ", f"{a} + {b}"

    if level == 2:
        return f"lukujen {number_to_word(a)} ja {number_to_word(b)} erotus ", f"{a} - {b}"

    if level in [3, 4]:
        return f"lukujen {number_to_word(a)} ja {number_to_word(b)} tulo ", f"{a}*{b}"

    if level in [5, 6]:
        return f"{number_to_word(a)} jaettuna luvulla {number_to_word(b)}", f"{a}/{b}"

    return None


def left_value_func(level, a, b):

    if level == 1:
        return a + b

    if level == 2:
        return a - b

    if level in [3, 4]:
        return a * b

    if level in [5, 6]:
        return a/b

    return None


def parameters(level):
    if level == 1:
        a, b = draw_two_integers(0, 100, 0, 100)

    if level == 2:
        a, b = draw_two_integers(-50, 50, -50, 50)

    if level == 3:
        a, b = draw_two_integers(2, 10, 2, 10)

    if level == 4:
        a, b = draw_two_integers(-10, 10, -10, 10)

    if level == 5:
        k, b = draw_two_integers(1, 10, 1, 10)
        a = k * b

    if level == 6:
        k, b = draw_two_integers(1, 10, -10, 10)
        a = k * b
        if b == 0:
            #olisi nollalla jako
            b = random.randint(1,10)


    multiplier = random.choice([1, 10, 100])

    a = multiplier * a
    b = multiplier * b

    return a, b


def give_feedback(x, feedback_left, left_value):
    feedback = f"Väärin, vastasit {x}, mutta "
    feedback += feedback_left
    feedback += " = " + f"{left_value}" + "."
    print("="*len(feedback))
    print(feedback)
    print("=" * len(feedback))


def question(successive_correct, level):

    a, b = parameters(level)

    is_finish = False

    calculation_words, calculation_numbers = left_hand_func(level, a, b)
    length = len("Mitä on " + calculation_words)
    print("-" * length)
    print("Mitä on " + calculation_words)
    print("-" * length)
    print("Vastaus on kokonaisluku ...-2, -1, 0, 1, 2,...")
    print("Muu vastaus kuin kokonaisluku keskeyttää tehtävän suorittamisen.")
    ans = input("Vastaus on ")

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

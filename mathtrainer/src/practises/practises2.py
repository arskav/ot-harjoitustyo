import random
from services.utilities import is_number, cancel, draw_two_integers, correct_answer, ask_question
from services.number_to_word import number_to_word


FINISH = 1  # testaamisen helpottamiseksi riittää yksi oikea
# Kuinka monen peräkkäisen oikean vastauksen jälkeen lopetetaan.


def left_hand_func(level, first_argument, second_argument):
    # pylint: disable=invalid-name
    a = first_argument
    b = second_argument

    if level == 1:
        return f"lukujen {number_to_word(a)} ja {number_to_word(b)} summa ", f"{a} + {b}"

    if level == 2:
        return f"lukujen {number_to_word(a)} ja {number_to_word(b)} erotus ", f"{a} - {b}"

    if level in [3, 4]:
        return f"lukujen {number_to_word(a)} ja {number_to_word(b)} tulo ", f"{a}*{b}"

    if level in [5, 6]:
        return f"{number_to_word(a)} jaettuna luvulla {number_to_word(b)}", f"{a}/{b}"

    return None
 # pylint: enable=invalid-name

def left_value_func(level, argument1, argument2):

    if level == 1:
        return argument1 + argument2

    if level == 2:
        return argument1 - argument2

    if level in [3, 4]:
        return argument1 * argument2

    if level in [5, 6]:
        return argument1 / argument2

    return None


def parameters(level):
    if level == 1:
        random_integer1, random_integer2 = draw_two_integers(0, 100, 0, 100)

    if level == 2:
        random_integer1, random_integer2 = draw_two_integers(-50, 50, -50, 50)

    if level == 3:
        random_integer1, random_integer2 = draw_two_integers(2, 10, 2, 10)

    if level == 4:
        random_integer1, random_integer2 = draw_two_integers(-10, 10, -10, 10)

    if level == 5:
        random_multiplier, random_integer2 = draw_two_integers(1, 10, 1, 10)
        random_integer1 = random_multiplier * random_integer2

    if level == 6:
        random_multiplier, random_integer2 = draw_two_integers(1, 10, -10, 10)
        random_integer1 = random_multiplier * random_integer2
        if random_integer2 == 0:
            # olisi nollalla jako
            random_integer2 = random.randint(1, 10)

    random_multiplier = random.choice([1, 10, 100])

    random_integer1 = random_multiplier * random_integer1
    random_integer2 = random_multiplier * random_integer2

    return random_integer1, random_integer2


def give_feedback(answer_given, feedback_left, left_value):
    feedback = f"Väärin, vastasit {answer_given}, mutta "
    feedback += feedback_left
    feedback += " = " + f"{left_value}" + "."
    print("="*len(feedback))
    print(feedback)
    print("=" * len(feedback))

def deal_with_answer(ans, successive_correct, calculation_numbers, level, argument1, argument2):

    is_finish = False

    if is_number(ans):
        answer_given = int(ans)
        left_value = int(left_value_func(level, argument1, argument2))
    else:
        return cancel()

    if left_value == answer_given:
        is_correct = True
    else:
        is_correct = False
        give_feedback(answer_given, calculation_numbers, left_value)

    if is_correct:

        is_finish, successive_correct = correct_answer(
            successive_correct, FINISH)

    return (is_correct, False, is_finish)



def question(successive_correct, level):

    random_integer1, random_integer2 = parameters(level)

    calculation_words, calculation_numbers = left_hand_func(level, random_integer1, random_integer2)

    ans = ask_question("Mitä on " + calculation_words, "Vastaus on ")

    return deal_with_answer(ans, successive_correct, calculation_numbers, \
        level, random_integer1, random_integer2)

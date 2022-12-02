from services.utilities import is_number, cancel, draw_two_integers, correct_answer


FINISH = 3
# Kuinka monen peräkkäisen oikean vastauksen jälkeen lopetetaan.


def left_hand_func(level, a, b):

    if level == 1:
        return f"{a} + {b}"

    if level == 2:
        return f"{a} - {b}"

    if level in [3, 4]:
        return f"{a}*{b}"

    if level in [5, 6]:
        return f"{a}/{b}"

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

    calculation = left_hand_func(level, a, b)
    print("Laske " + calculation)
    print("Vastaus on kokonaisluku ...-2, -1, 0, 1, 2,...")
    print("Muu vastaus kuin kokonaisluku keskeyttää tehtävän suorittamisen.")
    ans = input("tulos = ")

    if is_number(ans):
        x = int(ans)
        left_value = left_value_func(level, a, b)
    else:
        return cancel()

    if left_value == x:
        is_correct = True
    else:
        is_correct = False
        give_feedback(x, calculation, left_value)

    if is_correct:

        is_finish, successive_correct = correct_answer(
            successive_correct, FINISH)

    return (is_correct, False, is_finish)

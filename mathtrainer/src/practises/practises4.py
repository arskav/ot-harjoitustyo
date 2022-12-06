from services.utilities import is_number, cancel, draw_two_integers, correct_answer

FINISH = 1  # testaamisen helpottamiseksi riittää yksi oikea
# Kuinka monen peräkkäisen oikean vastauksen jälkeen lopetetaan.


def left_hand_func(level, constant_in_left):

    if level == 1:
        return f"x + {constant_in_left}"

    if level == 2:
        return f"{constant_in_left} - x"

    if level in [3, 4]:
        return f"{constant_in_left}x"

    if level == 5:
        return f"x/{constant_in_left}"

    if level == 6:
        return f"{constant_in_left}/x"

    return None


def left_value_func(level, constant_in_left, answer_given):

    if level == 1:
        return answer_given + constant_in_left

    if level == 2:
        return constant_in_left - answer_given

    if level in [3, 4]:
        return constant_in_left * answer_given

    if level == 5:
        return answer_given / constant_in_left

    if level == 6:
        return constant_in_left / answer_given

    return None


def feedback_left_func(level, constant_in_left, answer_given):

    # pylint: disable=invalid-name
    a = constant_in_left
    x = answer_given

    if level == 1:
        return f"x + {a} = {x} + {a}  = {x + a}"

    if level == 2:
        return f"{a} - x = {a} - {x} = {a - x}"

    if level in [3, 4]:
        return f"{a}x = {a}*{x} = {a * x}"

    if level == 5:
        return f"x/{a} = {x}/{a} = {x/a}"

    if level == 6:
        return f"{a}/x = {a}/{x} = {a/x}"

    return None

# pylint: enable=invalid-name

def parameters(level):
    if level == 1:
        random_integer1, random_temp = draw_two_integers(-10, 10, 1, 10)
        random_integer2 = random_integer1 + random_temp

    if level == 2:
        random_integer1, random_integer2 = draw_two_integers(-20, 20, -10, 10)

    if level == 3:
        random_integer1, random_temp = draw_two_integers(2, 10, 2, 10)
        random_integer2 = random_integer1 * random_temp

    if level == 4:
        random_integer1, random_temp = draw_two_integers(-10, 10, -10, 10)
        random_integer2 = random_integer1 * random_temp

    if level == 5:
        random_integer1, random_integer2 = draw_two_integers(-10, 10, -10, 10)

    if level == 6:
        random_temp, random_integer2 = draw_two_integers(-10, 10, -10, 10)
        random_integer1 = random_temp * random_integer2

    return random_integer1, random_integer2


def give_feedback(solve_task, level, argument_in_left, right_value, answer_given):

    feedback = f"Väärin, kun x = {answer_given}, vasen puoli on "
    feedback += feedback_left_func(level, argument_in_left, answer_given)
    feedback += ", mutta oikea puoli " + f"{right_value}" + "."
    print("="*len(feedback))
    print(solve_task)
    print("Vastauksesi oli x =", answer_given)
    print(feedback)
    print("=" * len(feedback))


def question(successive_correct, level):

    constant_in_left, right_value = parameters(level)

    is_finish = False

    left_hand = left_hand_func(level, constant_in_left)

    solve_task = "Ratkaise x, kun " + left_hand + " = " + f"{right_value}"

    print(solve_task)
    print("Vastaus on kokonaisluku ...-2, -1, 0, 1, 2,..."
          "Muu vastaus kuin kokonaisluku keskeyttää tehtävän suorittamisen.")
    ans = input("x = ")

    if is_number(ans):
        answer_given = int(ans)
        left_value = left_value_func(level, constant_in_left, answer_given)
    else:
        return cancel()

    if left_value == right_value:
        is_correct = True
    else:
        is_correct = False
        give_feedback(solve_task, level, constant_in_left, right_value, answer_given)

    if is_correct:
        is_finish, successive_correct = correct_answer(
            successive_correct, FINISH)

    return (is_correct, False, is_finish)

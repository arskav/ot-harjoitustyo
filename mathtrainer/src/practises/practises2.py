from services.utilities import is_number, cancel, draw_two_integers, correct_answer

FINISH = 3
# Kuinka monen peräkkäisen oikean vastauksen jälkeen lopetetaan.


def left_hand_func(level, a):

    if level == 1:
        return f"x + {a}"

    if level == 2:
        return f"{a} - x"

    if level in [3, 4]:
        return f"{a}x"

    if level == 5:
        return f"x/{a}"

    if level == 6:
        return f"{a}/x"

    return None


def left_value_func(level, a, x):

    if level == 1:
        return x + a

    if level == 2:
        return a - x

    if level in [3, 4]:
        return a * x

    if level == 5:
        return x/a

    if level == 6:
        return a/x

    return None


def feedback_left_func(level, a, x):

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


def parameters(level):
    if level == 1:
        a, k = draw_two_integers(-10, 10, 1, 10)
        b = a + k

    if level == 2:
        a, b = draw_two_integers(-20, 20, -10, 10)

    if level == 3:
        a, k = draw_two_integers(2, 10, 2, 10)
        b = a * k

    if level == 4:
        a, k = draw_two_integers(-10, 10, -10, 10)
        b = a * k

    if level == 5:
        a, b = draw_two_integers(-10, 10, -10, 10)

    if level == 6:
        k, b = draw_two_integers(-10, 10, -10, 10)
        a = k * b

    return a, b


def give_feedback(solve_task, level, a, b, x):

    feedback = f"Väärin, kun x = {x}, vasen puoli on "
    feedback += feedback_left_func(level, a, x)
    feedback += ", mutta oikea puoli " + f"{b}" + "."
    print("="*len(feedback))
    print(solve_task)
    print("Vastauksesi oli x =", x)
    print(feedback)
    print("=" * len(feedback))


def question(successive_correct, level):

    a, b = parameters(level)

    is_finish = False

    left_hand = left_hand_func(level, a)

    solve_task = "Ratkaise x, kun " + left_hand + " = " + f"{b}"

    print(solve_task)
    print("Vastaus on kokonaisluku ...-2, -1, 0, 1, 2,..."
          "Muu vastaus kuin kokonaisluku keskeyttää tehtävän suorittamisen.")
    ans = input("x = ")

    if is_number(ans):
        x = int(ans)
        left_value = left_value_func(level, a, x)
        #right_value = b
        #is_cancelled = False
    else:
        return cancel()

    if left_value == b:
        is_correct = True
    else:
        is_correct = False
        give_feedback(solve_task, level, a, b, x)

    if is_correct:
        is_finish, successive_correct = correct_answer(
            successive_correct, FINISH)

    return (is_correct, False, is_finish)

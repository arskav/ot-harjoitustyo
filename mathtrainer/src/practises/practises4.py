"""Yksinkertaisten muotoa x + a = b, a - x = b, ax = b, a/x = b
olevien yhtälöiden ratkaisemisen harjoittelu."""
import random
from services.utilities import is_number, draw_two_integers
from services.practiseutilities import cancel, correct_answer

FINISH = 2
"""Peräkkäisten oikeiden vastausten lukumäärä, joka riittää harjoituksen
yhden tason suorittamiseksi."""


def left_hand_func(level, constant_in_left):
    """Yhtälön vasemman puolen, jolla tuntematon x, lauseke.

    Args:
        level (int): taso.
        constant_in_left (int): yhtälön vasemmalla puolella oleva vakio.

    Returns:
        string: Yhtälön vasen puoli.
    """

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
    """Yhtälön vasemman puolen lukuarvo, kun muuttujalla annetun vastauksen mukainen arvo.

    Args:
        level (int): taso
        constant_in_left (int): yhtälön vasemmalla puolella oleva vakio.
        answer_given (int): vastaukseksi annettu tuntemattoman x arvo.

    Returns:
        int: vasemman puolen arvo, kun x:llä annetun vastauksen mukainen arvo,
    """

    if level == 1:
        return answer_given + constant_in_left

    if level == 2:
        return constant_in_left - answer_given

    if level in [3, 4]:
        return constant_in_left * answer_given

    if level == 5:
        return answer_given / constant_in_left

    if level == 6:
        try:
            value = constant_in_left / answer_given
        except ZeroDivisionError:
            print("Nollalla ei voi jakaa")
            value = None

        return value

    return None


def feedback_left_func(level, constant_in_left, answer_given):
    """Palaute. Käytetään kun vastattu väärin.

    Args:
        level (int): taso
        constant_in_left (int): yhtälön vasemmalla puolella oleva vakio.
        answer_given (int): vastaukseksi annettu tuntemattoman x arvo.

    Returns:
        string: oikea vastaus perusteluineen.
    """

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
        try:
            feedback_string = f"{a}/x = {a}/{x} = {a/x}"
        except ZeroDivisionError:
            feedback_string = "määrittelemätön, koska nollalla ei voi jakaa"

        return feedback_string

    return None

# pylint: enable=invalid-name

def parameters(level):
    """Tehtävän parametrit.

    Args:
        level (int): taso.

    Returns:
        (int, int): yhtälön vasemmalla ja oikealla puolella olevien vakioiden satunnaiset arvot.
    """

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
        if random_integer1 == 0:
            random_integer1 = random.randint(-10,-1)

    if level == 6:
        random_temp, random_integer2 = draw_two_integers(-10, 10, -10, 10)
        random_integer1 = random_temp * random_integer2

    return random_integer1, random_integer2


def give_feedback(solve_task, level, argument_in_left, right_value, answer_given):
    """Palaute, kun vastattu väärin.

    Args:
        solve_task (string): ratkaistava yhtälö.
        level (int): taso.
        constant_in_left (int): yhtälön vasemmalla puolella oleva vakio.
        right_value (int): yhtälön oikean puolen arvo.
        answer_given (int): vastaukseksi annettu tuntemattoman x arvo.
    """

    feedback = f"Väärin, kun x = {answer_given}, vasen puoli on "
    feedback += feedback_left_func(level, argument_in_left, answer_given)
    feedback += ", mutta oikea puoli " + f"{right_value}" + "."
    print("="*len(feedback))
    print(solve_task)
    print("Vastauksesi oli x =", answer_given)
    print(feedback)
    print("=" * len(feedback))


def question(successive_correct, level):
    """Yhtälön ratkaisutehtävän muodostaminen, esittäminen ja vastauksen käsittely.

    Args:
        successive_correct (int): Peräkkäisten oikeiden vastausten lukumäärä.
        level (int): taso

    Returns:
        (Boolean, Boolean, Boolean): onko vastaus oikein, onko keskeytetty,
            onko taso tehty loppuun.
    """

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

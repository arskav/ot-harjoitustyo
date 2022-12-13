"""Luvun muuttaminen kirjoitettuun asuun."""

UNITS = {2: ('sata', 'sataa'), 3: ('tuhat ', 'tuhatta '), 6: ('miljoona ', 'miljoonaa ') }

def magnitude(number):
    """Annetun luvun suuruusluokka.

    Args:
        number (int): tutkittava luku.

    Returns:
        int: 0 (alle sata), 2 (100-999), 3 (1000-999999), 6 (suurempi kuin miljoona).
    """

    for i in [6,3,2]:

        if number >= 10**i:

            return i

    return 0

def digit_to_word(digit):
    """Muuttaa yksittäisen numeron sanaksi.

    Args:
        digit (int): luku 0,1,..,9.

    Returns:
        string: numero sanallisesti.
    """

    digit_as_words = {0: '', 1: 'yksi', 2: 'kaksi', 3: 'kolme', 4: 'neljä',
                       5: 'viisi', 6: 'kuusi', 7: 'seitsemän', 8: 'kahdeksan', 9: 'yhdeksän'}

    return digit_as_words[digit]


def tens_to_word(number):
    """Muuttaa luvun 1 - 99 sanaksi.

    Args:
        number (int): luku väliltä 1 - 99.

    Returns:
        string: luku kirjoitettuna.
    """

    if number == 0:

        return ''

    if number < 10:

        return digit_to_word(number)

    if number == 10:

        return 'kymmenen'

    if number < 20:

        return digit_to_word(number % 10) + 'toista'

    return digit_to_word(number // 10) + 'kymmentä' + \
        digit_to_word(number % 10)

def positive_number_to_word(number):
    """Muuntaa positiivisen luvun kirjoitettuun muotoon.

    Args:
        number (int): luku 1,2,3,...

    Returns:
        string: luku kirjoitettuna
    """

    if number == 0:

        return ''

    if number < 100:

        return tens_to_word(number)

    order =  magnitude(number)

    if number >= 2*10**order:

        return positive_number_to_word(number // 10**order) + UNITS[order][1] +\
            positive_number_to_word(number % 10**order)

    return UNITS[order][0] + positive_number_to_word(number % 10**order)

def number_to_word(number):
    """Muuttaa luvun ...,-2,-1,0,1,2,... kirjoitettuun muotoon.
    Miljoona suurin yksikkö.

    Args:
        number (int): luku.

    Returns:
        string: luku kirjoitettuna.
    """

    if number == 0:

        return 'nolla'

    sign = ''

    if number < 0:

        sign = 'miinus '

        number = -number

    return sign + positive_number_to_word(number)

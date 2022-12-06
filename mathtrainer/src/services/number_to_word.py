UNITS = {2: ('sata', 'sataa'), 3: ('tuhat ', 'tuhatta '), 6: ('miljoona ', 'miljoonaa ') }

def magnitude(number):

    for i in [6,3,2]:

        if number >= 10**i:

            return i

    return 0

def digit_to_word(digit):

    digit_as_words = {0: '', 1: 'yksi', 2: 'kaksi', 3: 'kolme', 4: 'neljä',
                       5: 'viisi', 6: 'kuusi', 7: 'seitsemän', 8: 'kahdeksan', 9: 'yhdeksän'}

    return digit_as_words[digit]


def tens_to_word(number):

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

    if number == 0:

        return 'nolla'

    sign = ''

    if number < 0:

        sign = 'miinus '

        number = -number

    return sign + positive_number_to_word(number)

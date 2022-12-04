def number_to_list(number):

    number_as_list = []

    while number > 0:

        number_as_list.append(number % 10)

        number = number // 10

    return(number_as_list)


def number_1_99_to_word(number_as_list):

    if len(number_as_list) == 1:

        return digit_to_word(number_as_list[0])

    if len(number_as_list) == 2:

        if number_as_list[0] == 0:
            if number_as_list[1] == 1:
                return 'kymmenen'
            else:
                return digit_to_word(number_as_list[1]) + 'kymmentä'
        else:
            if number_as_list[1] == 1:
                return digit_to_word(number_as_list[0]) + 'toista'
            else:
                return digit_to_word(number_as_list[1]) + 'kymmentä' + digit_to_word(number_as_list[0])


def number_big_to_word(number_as_list):

    while len(number_as_list) > 0 and number_as_list[-1] == 0:

        number_as_list.pop()

    if len(number_as_list) == 0:

        return ''

    if len(number_as_list) <= 2:

        return number_1_99_to_word(number_as_list)

    if len(number_as_list) == 3:

        if number_as_list[-1] == 1:

            return 'sata' + number_big_to_word(number_as_list[:-1])

        else:

            return digit_to_word(number_as_list[-1]) + 'sataa' + number_big_to_word(number_as_list[:-1])

    if len(number_as_list) == 4 and number_as_list[-1] == 1:

            return 'tuhat ' + number_big_to_word(number_as_list[:-1])

    if len(number_as_list) in [4, 5, 6]:

            return number_big_to_word(number_as_list[3:]) + 'tuhatta ' + number_big_to_word(number_as_list[:3])

    if len(number_as_list) == 7:

        if number_as_list[-1] == 1:

            return 'miljoona ' + number_big_to_word(number_as_list[:-1])

        else:

            return digit_to_word(number_as_list[-1]) + 'miljoonaa ' + number_big_to_word(number_as_list[:-1])


def digit_to_word(digit):

    digits_as_words = {0: '', 1: 'yksi', 2: 'kaksi', 3: 'kolme', 4: 'neljä', 5: 'viisi', 6: 'kuusi', 7: 'seitsemän', 8: 'kahdeksan', 9: 'yhdeksän'}    

    return(digits_as_words[digit])


def number_to_word(number):

    if number == 0:

        return 'nolla'

    else:

        return number_big_to_word(number_to_list(number))


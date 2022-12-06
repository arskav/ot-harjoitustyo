import random
# Sekalaisia apualiohjelmia
# Tämä pitäisi jakaa osiin sen mukaisesti, missä apuohjelmaa käytetään


def correct_answer(successive_correct, finish):

    successive_correct += 1
    print(f"Peräkkäisiä oikeita {successive_correct}/{finish}")
    is_finish = successive_correct == finish

    return is_finish, successive_correct


def draw_two_integers(lower1, upper1, lower2, upper2):
    return random.randint(lower1, upper1), random.randint(lower2, upper2)


def return_to_menu():

    # vakiokysymys vaiheessa, jossa jonkun harjoituksen tietyn tason kysymykset on tehty

    print("X: Lopetetaan harjoittelu ja palataan päävalikkoon")

    print("Mikä tahansa muu: jatka harjoittelua.")

    ans = input("X/muu > ")

    return ans.upper() == 'X'


def practise_done(drill):
    # Ilmoitus, kun harjoituksen kaikki tasot on tehty
    print(f"Olet tehnyt kaikki tehtävät harjoituksissa {drill}.")
    print("Jos haluat tehdä tämän harjoituksen tehtäviä uudelleen,")
    print("valitse uusi käyttäjätunnus.")
    input("Enter paluu päävalikkoon.")


def list_to_string(as_list):

    string = " ".join([str(item) + "," for item in as_list])

    return string[:-1]


def string_to_list(as_string):

    if len(as_string) > 0:
        return [int(i) for i in as_string.split(',')]

    return []


def ask_question(assignment_in_words, prompt):
    length = len(assignment_in_words)
    print("-" * length)
    print(assignment_in_words)
    print("-" * length)
    print("Vastaus on kokonaisluku ...-2, -1, 0, 1, 2,...")
    print("Muu vastaus kuin kokonaisluku keskeyttää tehtävän suorittamisen.")
    return input(prompt)


# def dict_to_string(as_dict):

#     as_string = ""

#     for key, value in as_dict.items():

#         as_string += str(key) + ":" + str(value) + ","

#     return as_string[:-1]


# def string_to_dict(as_string):

#     as_dict = {}

#     for triple in as_string.split(','):

#         as_dict[int(triple[0])] = int(triple[2])

#     return as_dict


def is_number(ans):
    """Tarkistetaan, onko annettu vastaus kokonaisluku
    """
    if len(ans) == 0:
        return False
    if ans[0] == '-':
        # negatiivinen luku, ensimmäinen merkki '-'
        return ans[1:].isnumeric()

    return ans.isnumeric()


def cancel():
    """Lopetetaan tehtävien tekeminen.
    """
    print("Lopetus")
    is_correct = False
    is_cancelled = True
    is_finish = False
    return is_correct, is_cancelled, is_finish

# Sekaialisia apualiohjelmia


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


def dict_to_string(as_dict):

    as_string = ""

    for key, value in as_dict.items():

        as_string += str(key) + ":" + str(value) + ","

    return as_string[:-1]


def string_to_dict(as_string):

    as_dict = {}

    for triple in as_string.split(','):

        as_dict[int(triple[0])] = int(triple[2])

    return as_dict

import random
#Sekalaisia apuohjelmia.
#Tämä pitäisi ehkä jakaa osiin sen mukaisesti, missä apuohjelmaa käytetään.
#Osa harjoituksissa käytettävissä apuohjelmista tiedostossa practiseutilities.py

def draw_two_integers(lower1, upper1, lower2, upper2):
    """Arpoo kaksi satunnaista kokonaislukua.

    Args:
        lower1 (int): ensimmäisen luvun alaraja.
        upper1 (int): ensimmäisen luvun yläraja.
        lower2 (int): toisen luvun alaraja.
        upper2 (int): toisen luvun ylaäraja.

    Returns:
        (int, int): arvotut luvut.
    """
    return random.randint(lower1, upper1), random.randint(lower2, upper2)


def return_to_menu():
    """Vakiokysymys vaiheessa, jossa jonkun harjoituksen tietyn tason kysymykset on tehty.
       Harjoittelu lopetetaan vastaamalla 'X' tai 'x', muulloin jatketaan.

    Returns:
        Boolean: lopetettiinko harjoittelu.
    """
    print("X: Lopetetaan harjoittelu ja palataan päävalikkoon")

    print("Mikä tahansa muu: jatka harjoittelua.")

    ans = input("X/muu > ")

    return ans.upper() == 'X'


def list_to_string(as_list):
    """Muuttaa listan merkkijonoksi esimerkiksi tulostusta tai
    tietokantaan tallentamista varten.

    Args:
        as_list (list): lista (esim. harjoitusten numeroita).

    Returns:
        string: lista merkkijonoina.
    """

    string = " ".join([str(item) + "," for item in as_list])

    return string[:-1]


def string_to_list(as_string):
    """Muuttaa merkkijonon listaksi.

    Args:
        as_string (string): merkkijono, joka sisältää luettelon (esim. harjoitusten numeroista).

    Returns:
        list: lista merkkijonon pilkuilla erotetuista jäsenistä.
    """

    if len(as_string) > 0:
        return [int(i) for i in as_string.split(',')]

    return []


def ask_question(assignment_in_words, prompt):
    """Vanhempi versio tulostaa kysymys ja kysyä siihen vastaus.

    Args:
        assignment_in_words (string): kysymys.
        prompt (string): kehote inputissa.

    Returns:
        string: annettu vastaus.
    """
    length = len(assignment_in_words)
    print("-" * length)
    print(assignment_in_words)
    print("-" * length)
    print("Vastaus on kokonaisluku ...-2, -1, 0, 1, 2,...")
    print("Muu vastaus kuin kokonaisluku keskeyttää tehtävän suorittamisen.")
    return input(prompt)

def is_number(ans):
    """Tarkistetaan, onko annettu vastaus kokonaisluku.

    Args:
        ans (string): vastaus merkkijonona.

    Returns:
        Booelan: onko vastaus tulkittavissa luvuksi.
    """

    if len(ans) == 0:
        return False
    if ans[0] == '-':
        # negatiivinen luku, ensimmäinen merkki '-'
        return ans[1:].isnumeric()

    return ans.isnumeric()

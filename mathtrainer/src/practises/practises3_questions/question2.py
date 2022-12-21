"""Harjoituksen 3 toinen kysymys."""
import random
from entities.question import Question
#kysymyksen muuttujat:
#rent, sauna, internet, water_fee, persons


def randomize_func():
    """Annetaan kysymyksen parametreille sopivat satunnaiset arvot.
    Returns:
        Tässä kysymyksessä viiden parametrin arvot.
    """
    rent = random.randint(100,200) * 10
    sauna = random.choice([10, 15, 20, 25, 30])
    internet = random.randint(5,40)
    water_fee = random.randint(15, 25)
    persons = random.randint(2,6)
    return rent, sauna, internet, water_fee, persons

def text_func(rent, sauna, internet, water_fee, persons):
    """Kysymyksen teksti.
    Args:
        rent (int): vuokra.
        sauna (int): saunamaksu.
        internet (int): tietoliikennmaksu.
        water_fee (int): vesimaksu.
        persons (int): perheen koko.
    Returns:
        string: harjoituksen kysymys.
    """
    return f"""
    Perheessä on {persons} jäsentä. Perheen asumismenot ovat kuukaudessa {rent + sauna + internet + persons * water_fee} euroa.
    Menoista vuokran osuus {rent} euroa, saunamaksun osuus on {sauna} ja tietoliikennemaksun {internet} euroa.
    Lisäksi jokaista asukasta kohden peritään vesimaksu.
    Perheeseen syntyy vauva ja vesimaksua aletaan periä {persons + 1} henkilöltä.
    Mitkä ovat perheen uudet asumismenot?
    """

def correct_answer_func(rent, sauna, internet, water_fee, persons):
    """Oikean vastauksen kaava.
    Args:
        Samat kuin kysymyksen tekstissä.
    Returns:
        int: oikea vastaus.
    """
    old_cost = rent + sauna + internet + persons * water_fee
    return old_cost + water_fee

def feedback_func(rent, sauna, internet, water_fee, persons):
    """Palauteteksti.
    Args:
        Samat kuin kysymyksen tekstissä.
    """
    old_cost = rent + sauna + internet + persons * water_fee
    print("Vastaus ei ole oikein.")
    print(f"""
    Vanhat asumiskustannukset olivat siis {old_cost},
    kun tästä vähennetään vuokra {rent} saunamaksu {sauna} ja tietoliikennemaksu {internet},
    vesimaksujen osuudeksi saadaan {old_cost} - -{rent} -{sauna} -{internet} = {old_cost - rent -sauna - internet}.
    Yhdeltä asukkaalta vesimaksu on siis {water_fee * persons} / {persons} = {water_fee}.
    Uudet asumismenot ovat siis {old_cost} + {water_fee} = {old_cost + water_fee} euroa.
    """)

CALCULATOR = True

question_part = {'text': text_func, 'prompt': "Uusi asumiskulu kuukaudessa ", 'mode': 'nonnegative'}

question = Question(CALCULATOR, question_part, randomize_func,
    correct_answer_func, feedback_func)

question.randomize(randomize_func)

question2 = question

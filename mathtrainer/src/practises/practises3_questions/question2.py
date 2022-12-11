import random
from entities.question import Question

#kysymyksen muuttujat:
#rent, sauna, internet, water_fee, persons


def question2():

    question = Question(calculator_in_use = True)


    def randomize_question():

        rent = random.randint(100,200) * 10

        sauna = random.choice([10, 15, 20, 25, 30])

        internet = random.randint(5,40)

        water_fee = random.randint(15, 25)

        persons = random.randint(2,6)

        return rent, sauna, internet, water_fee, persons


    def text_func(rent, sauna, internet, water_fee, persons):

        return f"""
        Perheessä on {persons} jäsentä. Perheen asumismenot ovat kuukaudessa {rent + sauna + internet + persons * water_fee} euroa.
        Menoista vuokran osuus {rent} euroa, saunamaksun osuus on {sauna} ja tietoliikennemaksun {internet} euroa.
        Lisäksi jokaista asukasta kohden peritään vesimaksu.
        Perheeseen syntyy vauva ja vesimaksua aletaan periä {persons + 1} henkilöltä.
        Mitkä ovat perheen uudet asumismenot?
        """


    prompt = "Uusi asumiskulu kuukaudessa "

    mode = 'nonnegative'

    def correct_answer_func(rent, sauna, internet, water_fee, persons):

        old_cost = rent + sauna + internet + persons * water_fee

        return old_cost + water_fee

    def feedback_func(rent, sauna, internet, water_fee, persons):

        old_cost = rent + sauna + internet + persons * water_fee

        print(f"""
        Vanhat asumiskustannukset olivat siis {old_cost},
        kun tästä vähennetään vuokra {rent} saunamaksu {sauna} ja tietoliikennemaksu {internet},
        vesimaksujen osuudeksi saadaan {old_cost} - -{rent} -{sauna} -{internet} = {old_cost - rent -sauna - internet}.
        Yhdeltä asukkaalta vesimaksu on siis {water_fee * persons} / {persons} = {water_fee}.
        Uudet asumismenot ovat siis {old_cost} + {water_fee} = {old_cost + water_fee} euroa.
        """)


    #Tämä aina lopussa
    return question.process(randomize_question, text_func, prompt, mode,\
         correct_answer_func, feedback_func)

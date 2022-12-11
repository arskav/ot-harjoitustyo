import random
from entities.question import Question

#kysymyksen muuttujat:
#salary, benefit, tax, subtraction, fee, prepayment


def question1():

    question = Question(calculator_in_use = True)


    def randomize_question():
        #nettopalkka jää aina positiiviseksi

        temp = random.randint(5, 12)
        salary = temp * 100

        temp = random.randint(1, salary // 10)
        benefit = 10 * temp

        tax_procent = random.choice(range(10, 40, 1)) / 100

        tax = 10 * round(tax_procent * (salary + benefit) // 10)

        fee = round(0.01 * (salary + benefit))

        subtraction = 10 * round(0.05 * (salary + benefit) // 10)

        prepayment = 10 * random.randint(1, (salary + benefit) // 20)

        return salary, benefit, tax, subtraction, fee, prepayment

    def text_func(salary, benefit, tax, subtraction, fee, prepayment):

        return f"""
        Työntekijän peruspalkka kahdelta viikolta on {salary} euroa.
        Työntekijä saa ylityökorvauksia {benefit} euroa.
        Palkasta menee veroa {tax} euroa ja muita lakisääteisiä vähennyksiä {subtraction} euroa.
        Palkasta peritään myös ammattiyhdistyksen jäsenmaksu {fee} euroa.
        Lisäksi palkasta vähennetään palkkaennakkona saatu {prepayment} euroa.
        Kuinka paljon työntekijä saa pankkitilille palkkarahoja?
        """


    prompt = "Pankkitilille tulee euroissa "

    mode = 'nonnegative'

    def correct_answer_func(salary, benefit, tax, subtraction, fee, prepayment):

        return salary + benefit - tax - subtraction - fee - prepayment

    def feedback_func(salary, benefit, tax, subtraction, fee, prepayment):

        print("Vastaus ei ole oikein.")
        print("Palkka plus ylityökorvaus miinus vero miinus "
        "muita lakisääteisiä vähennyksiä miinus ay-maksu miinus palkkaennakko on ")
        print(f"{salary} + {benefit} - {tax} - {subtraction} - {fee} -{prepayment} = "
        f"{salary + benefit - tax - subtraction - fee -prepayment}.")
        input("Jatka > ")

    #Tämä aina lopussa
    return question.process(randomize_question, text_func,\
         prompt, mode, correct_answer_func, feedback_func)

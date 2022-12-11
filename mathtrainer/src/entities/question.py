from services.calculator import calculator
from services.practiseutilities import check_if_input_ok

class Question:

    def __init__(self, calculator_in_use):

        self._calculator_in_use = calculator_in_use
        self._variables = []
        self._question = {'text': (lambda: None), 'prompt':'', 'mode': ''}
        self._randomize = (lambda: None)
        self._correct_answer = (lambda: None)
        self._feedback = (lambda: None)

    def set_randomizing(self, randomice_func):

        self._randomize = randomice_func

    def randomize(self, randomice_func):

        self._variables = randomice_func()

    def set_question(self, text_func, prompt, mode):

        self._question['text'] = text_func

        self._question['prompt'] = prompt

        self._question['mode'] = mode

    def set_feedback(self, feedback_func):

        self._feedback = feedback_func

    def give_feedback(self):

        self._feedback(*self.values_of_variables())

    def set_correct_answer(self, correct_answer_func):

        self._correct_answer = correct_answer_func

    def check_answer(self, ans):

        return self._correct_answer(*self.values_of_variables()) == ans

    def ask_question(self):

        print('\nTEHTÄVÄ')

        print((self._question['text'])(*self.values_of_variables()))

        print("ANNA VASTAUS")

        if self._calculator_in_use:

            print("Laskin käytössä, kirjoita vastauksen alkuun = ")

        ans = input(self._question['prompt'])

        if ans == '':

            return None

        if ans[0] == '=':

            answer =  calculator(ans[1:])

        else:

            answer = check_if_input_ok(ans, self._question['mode'])

        return answer


    def values_of_variables(self):

        return self._variables

    def process(self,randomize_func, text_func, prompt, mode, correct_answer_func, feedback_func):

        self.randomize(randomize_func)

        self.set_question(text_func, prompt, mode)

        self.set_correct_answer(correct_answer_func)

        self.set_feedback(feedback_func)

        ans = self.ask_question()

        if ans is None:
            #keskeytys

            return False, True

        is_correct = self.check_answer(ans)

        if is_correct:

            print("Vastaus on oikein.")

        if not is_correct:

            self.give_feedback()

        return is_correct, False

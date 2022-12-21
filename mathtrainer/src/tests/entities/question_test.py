import unittest
from unittest.mock import patch
from entities.question import Question

def randomice_function_for_testing():

    x = 10; y = 15

    return x, y

def correct_answer_function_for_testing():

    return 10 + 15

def text_function_for_testing():

    print("Kysymysteksti")

question_part_for_testing = {
    'text': text_function_for_testing,
    'prompt': " ",
    'mode': 'integer'
    }

def feedback_function_for_testing():

    print("Palaute")


class TestQuestion(unittest.TestCase):


    def setUp(self):
        self.question = Question(True, question_part_for_testing, randomice_function_for_testing,
        correct_answer_function_for_testing, feedback_function_for_testing)

        self.question_without_calculator= Question(False, question_part_for_testing, randomice_function_for_testing,
        correct_answer_function_for_testing, feedback_function_for_testing)


    @patch('builtins.input', return_value = '25')
    def test_process_correct(self, input):

        is_correct, is_cancelled = self.question.process()

        self.assertEqual((is_correct, is_cancelled), (True, False))


    @patch('builtins.input', return_value = '24')
    def test_process_incorrect(self, input):

        is_correct, is_cancelled = self.question.process()


        self.assertEqual((is_correct, is_cancelled), (False, False))

    @patch('builtins.input', return_value = '=10+15')
    def test_process_correct_by_calculator(self, input):

        is_correct, is_cancelled = self.question.process()

        self.assertEqual((is_correct, is_cancelled), (True, False))

    @patch('builtins.input', return_value = '=10+10')
    def test_process_incorrect_by_calculator(self, input):

        is_correct, is_cancelled = self.question.process()

        self.assertEqual((is_correct, is_cancelled), (False, False))


    @patch('builtins.input', return_value = 'peruutus')
    def test_process_cancelled(self, input):

        is_correct, is_cancelled = self.question.process()

        self.assertEqual((is_correct, is_cancelled), (False, True))

    @patch('builtins.input', return_value = '')
    def test_process_empty(self, input):

        is_correct, is_cancelled = self.question.process()

        self.assertEqual((is_correct, is_cancelled), (False, True))


    @patch('builtins.input', return_value = '=10++')
    def test_process_cancelled_with_calculator(self, input):

        is_correct, is_cancelled = self.question.process()

        self.assertEqual((is_correct, is_cancelled), (False, True))


    @patch('builtins.input', return_value = '=10+15')
    def test_process_without_calculator(self, input):

        is_correct, is_cancelled = self.question_without_calculator.process()

        self.assertEqual((is_correct, is_cancelled), (False, True))






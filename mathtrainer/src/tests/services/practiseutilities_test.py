import unittest
from unittest.mock import patch
from services.practiseutilities import ask_answer_to_question, check_if_input_ok, correct_answer, doing_practise

from entities.user import MathTrainerUser
from entities.session import MathTrainerSession


def get_input(text):
    return input(text)


class TestUtitities(unittest.TestCase):

    def setUp(self):
        self.trainee = MathTrainerUser(
            "Testaaja", [1,2,3], [1], 10, 20)
        self.session = MathTrainerSession(
            "Testaaja", 2, 1)

        self.trainee_4 = MathTrainerUser(
            "Testaaja_harj4", [1,2,3,4], [1,2], 20, 40)
        self.session_4 = MathTrainerSession(
            "Testaaja_harj4", 4, 6)

        self.successive_correct = 0


    def test_check_if_input_ok(self):

        self.assertEqual(check_if_input_ok("123", 'integer'), 123)
        self.assertEqual(check_if_input_ok("-123", 'integer'), -123)
        self.assertEqual(check_if_input_ok("x123", 'integer'), None)
        self.assertEqual(check_if_input_ok("123", 'nonnegative'), 123)
        self.assertEqual(check_if_input_ok("-123", 'nonnegative'), None)

    def test_correct_answer(self):

        self.assertEqual(correct_answer(2,4), (False, 3))
        self.assertEqual(correct_answer(2,3), (True, 3))

    def test_doing_practise_not_finish_correct(self):

        def practise_func(successive_correct, level):
            #testausta varten korvike varsinaiselle
            #practise_func -funktiolle

            #keskeytetään while-silmukka
            self.session._ongoing = False

            correct = True

            return correct, False, False


        doing_practise(self.session, self.trainee, practise_func)

        self.assertEqual(self.session.level(), 1)
        self.assertEqual(self.session.tries(), 1)
        self.assertEqual(self.session.tries_at_level(), 1)
        self.assertEqual(self.session.correct(), 1)
        self.assertEqual(self.session.correct_at_level(), 1)
        self.assertEqual(self.trainee.correct_total(), 11)
        self.assertEqual(self.trainee.tries_total(), 21)

    def test_doing_practise_not_finish_incorrect(self):

        def practise_func(successive_correct, level):
            #testausta varten korvike varsinaiselle
            #practise_func -funktiolle

            #keskeytetään while-silmukka
            self.session._ongoing = False

            correct = False

            return correct, False, False


        doing_practise(self.session, self.trainee, practise_func)

        self.assertEqual(self.session.level(), 1)
        self.assertEqual(self.session.tries(), 1)
        self.assertEqual(self.session.tries_at_level(), 1)
        self.assertEqual(self.session.correct(), 0)
        self.assertEqual(self.session.correct_at_level(), 0)
        self.assertEqual(self.trainee.correct_total(), 10)
        self.assertEqual(self.trainee.tries_total(), 21)

    @patch('builtins.input', return_value = '')
    def test_doing_practise_cancelled(self,input):

        def practise_func(successive_correct, level):
            #testausta varten korvike varsinaiselle
            #practise_func -funktiolle

            #keskeytetään while-silmukka
            self.session._ongoing = False

            correct = False

            cancelled = True

            return correct, cancelled, False



        doing_practise(self.session, self.trainee, practise_func)

        self.assertEqual(self.session.level(), 1)
        self.assertEqual(self.session.tries(), 0)
        self.assertEqual(self.session.tries_at_level(), 0)
        self.assertEqual(self.session.correct(), 0)
        self.assertEqual(self.session.correct_at_level(), 0)
        self.assertEqual(self.trainee.correct_total(), 10)
        self.assertEqual(self.trainee.tries_total(), 20)

    @patch('builtins.input', return_value = 'seuraavalle tasolle')
    def test_doing_practise_level_finished(self,input):

        def practise_func(successive_correct, level):
            #testausta varten korvike varsinaiselle
            #practise_func -funktiolle

            #keskeytetään while-silmukka
            self.session._ongoing = False

            correct = True

            cancelled = False

            finished = True

            return correct, cancelled, finished



        doing_practise(self.session, self.trainee, practise_func)

        self.assertEqual(self.session.tries(), 1)
        self.assertEqual(self.session.correct(), 1)
        self.assertEqual(self.session.level(), 2)
        self.assertEqual(self.session.tries_at_level(), 0)
        self.assertEqual(self.session.correct_at_level(), 0)
        self.assertEqual(self.trainee.correct_total(), 11)
        self.assertEqual(self.trainee.tries_total(), 21)
        self.assertEqual(self.trainee.practise_finished(), [1])

    @patch('builtins.input', return_value = 'harjoitus lopussa')
    def test_doing_practise_at_end(self,input):

        def practise_func(successive_correct, level):
            #testausta varten korvike varsinaiselle
            #practise_func -funktiolle

            #keskeytetään while-silmukka
            self.session._ongoing = False

            correct = True

            cancelled = False

            finished = True

            return correct, cancelled, finished


        #Testataan tilannetta, jossa ylin taso tehty loppuun.
        doing_practise(self.session_4, self.trainee_4, practise_func)

        self.assertEqual(self.session_4.tries(), 1)
        self.assertEqual(self.session_4.correct(), 1)
        self.assertEqual(self.session_4.level(), 7)  #maxtaso 6, 7 lopetusehdossa
        self.assertEqual(self.session_4.tries_at_level(), 0)
        self.assertEqual(self.session_4.correct_at_level(), 0)
        self.assertEqual(self.trainee_4.correct_total(), 21)
        self.assertEqual(self.trainee_4.tries_total(), 41)
        self.assertEqual(self.trainee_4.practise_finished(), [1, 2, 4])



    @patch('builtins.input', return_value = '123')
    def test_ask_answer_to_question(self, input):
        self.assertEqual(ask_answer_to_question('kehote', 'integer'), 123)

    @patch('builtins.input', return_value = 'x123')
    def test_ask_answer_to_question(self, input):
        self.assertEqual(ask_answer_to_question('kehote', 'integer'), None)

    @patch('builtins.input', return_value = '-123')
    def test_ask_answer_to_question(self, input):
        self.assertEqual(ask_answer_to_question('kehote', 'nonnegative'), None)

    @patch('builtins.input', return_value = '0')
    def test_ask_answer_to_question(self, input):
        self.assertEqual(ask_answer_to_question('kehote', 'nonnegative'), 0)

    @patch('builtins.input', return_value = '123')
    def test_ask_answer_to_question(self, input):
        self.assertEqual(ask_answer_to_question('kehote', 'positive'), None)
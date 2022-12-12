import unittest
from services.practiseutilities import check_if_input_ok, correct_answer, doing_practise
from entities.user import MathTrainerUser
from entities.session import MathTrainerSession


class TestUtitities(unittest.TestCase):

    def setUp(self):
        self.trainee = MathTrainerUser(
            "Testaaja", [1,2,3], [1], 10, 20)
        self.session = MathTrainerSession(
            "Testaaja", 2, 1)
        self.successive_correct = 0


    def test_check_if_input_ok(self):

        self.assertEqual(check_if_input_ok("123", 'integer'), 123)
        self.assertEqual(check_if_input_ok("-123", 'integer'), -123)
        self.assertEqual(check_if_input_ok("123", 'nonnegative'), 123)
        self.assertEqual(check_if_input_ok("-123", 'nonnegative'), None)

    def test_correct_answer(self):

        self.assertEqual(correct_answer(2,4), (False, 3))
        self.assertEqual(correct_answer(2,3), (True, 3))

    def test_doing_practise_not_finish(self):

        def practise_func(successive_correct, level):
            #testausta varten korvike varsinaiselle
            #practise_func -funktiolle

            #keskeytetään while-silmukka
            self.session._ongoing = False

            return True, False, False


        doing_practise(self.session, self.trainee, practise_func)

        self.assertEqual(self.session.tries(), 1)
        self.assertEqual(self.trainee.correct_total(), 11)
        self.assertEqual(self.trainee.tries_total(), 21)
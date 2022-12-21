import unittest
from entities.session import MathTrainerSession
from entities.definitions import MAXLEVELS


# self, username, practise = 1, correct = 8, tries = 10, level = 4, maxlevel = 4
#correct_at_levels = 3, tries_at_levels = 5


class TestMathTrainerSession(unittest.TestCase):

    def setUp(self):
            self.session = MathTrainerSession(
            "Testikäyttäjä", 1, 4)

            self.session.set_corrects_and_tries(8, 10, 3, 5)

    def test_tries_given_correctly(self):

        self.assertEqual(self.session.tries(), 10)

    def test_tries_at_level_given_correctly(self):

        self.assertEqual(self.session.tries_at_level(), 5)

    def test_correct_at_level_given_correctly(self):

        self.assertEqual(self.session.correct_at_level(), 3)

    def test_right_given_correctly(self):

        self.assertEqual(self.session.correct(), 8)

    def test_level_given_correctly(self):

        self.assertEqual(self.session.level(), 4)

    def test_maxlevel_given_correctly(self):

        self.assertEqual(self.session.maxlevel(), MAXLEVELS[1])

    # metodin _new_attempt() pitäisi kasvattaa yhdellä harjoitusten kokonaisyritysten _tries ja tason yritysten _tries_level lukumäärää

    def test_new_attempt_increases_tries(self):

        self.session.new_attempt()

        self.assertEqual(self.session._tries, 11)

    def test_new_attempt_increases_tries_level(self):

        self.session.new_attempt()

        self.assertEqual(self.session._tries_at_level, 6)

    # metodin _correct_up pitäisi kasvattaa oikeiden vastausten sekä harjoitus- että tasokohtaista lukumäärää yhdellä

    def test_correct_up_increases_correct_at_level(self):

        self.session.correct_up()

        self.assertEqual(self.session._correct_at_level, 4)

    def test_correct_up_increases_correct(self):

        self.session.correct_up()

        self.assertEqual(self.session._correct, 9)

    # metodin _level_up pitäisi korottaa tasoa yhdella ja nollata tasokohtaisten yritysten ja oikeiden lukumäärä

    def test_level_up_increases_level(self):

        self.session.level_up()

        self.assertEqual(self.session._level, 5)

    def test_level_up_initializes_correct_at_level(self):

        self.session.level_up()

        self.assertEqual(self.session._correct_at_level, 0)

    def test_level_up_initializes_tries_at_level(self):

        self.session.level_up()

        self.assertEqual(self.session._tries_at_level, 0)

    def test_set_ongoing(self):

        self.session.set_ongoing(True)
        self.assertEqual(self.session._ongoing, True)

        self.session.set_ongoing(False)
        self.assertEqual(self.session._ongoing, False)

    def test_correct_or_not_True(self):

        successive_correct, correct = self.session.correct_or_not(True,1,10)
        self.assertEqual(successive_correct, 2)
        self.assertEqual(correct, 11)

    def test_correct_or_not_False(self):

        successive_correct, correct = self.session.correct_or_not(False,1,10)
        self.assertEqual(successive_correct, 0)
        self.assertEqual(correct, 10)




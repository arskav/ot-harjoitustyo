import unittest
from entities.session import MathTrainerSession

#self, username, practise = 1, correct = 2, tries = 4, level = 2, maxlevel = 4

class TestMathTrainerSession(unittest.TestCase):

    def setUp(self):
        self.session = MathTrainerSession(
            "Testikäyttäjä", 1, 2, 4, 2, 4)

   
    def test_tries_given_correctly(self):

        self.assertEqual(self.session.tries(), 4)    

    def test_tries_at_level_given_correctly(self):

        self.assertEqual(self.session.tries_at_level(), 0)
   

    def test_correct_at_level_given_correctly(self):

        self.assertEqual(self.session.correct_at_level(), 0)
    def test_right_given_correctly(self):

         self.assertEqual(self.session.correct(), 2)    


    def test_level_given_correctly(self):

        self.assertEqual(self.session.level(), 2)


    def test_maxlevel_given_correctly(self):

        self.assertEqual(self.session.maxlevel(), 4)
    


    # metodin _new_attempt() pitäisi kasvattaa yhdellä harjoitusten kokonaisyritysten _tries ja tason yritysten _tries_level lukumäärää

    def test_new_attempt_increases_tries(self):

        self.session.new_attempt()

        self.assertEqual(self.session._tries, 5)

    def test_new_attempt_increases_tries_level(self):

        self.session.new_attempt()

        self.assertEqual(self.session._tries_at_level, 1)

    # metodin _correct_up pitäisi kasvattaa oikeiden vastausten sekä harjoitus- että tasokohtaista lukumäärää yhdellä

    def test_correct_up_increases_correct_at_level(self):

        self.session.correct_up()

        self.assertEqual(self.session._correct_at_level, 1)

    def test_correct_up_increases_correct(self):

        self.session.correct_up()

        self.assertEqual(self.session._correct, 3)

    # metodin _level_up pitäisi korottaa tasoa yhdella ja nollata tasokohtaisten yritysten ja oikeiden lukumäärä

    def test_level_up_increases_level(self):

        self.session.level_up()

        self.assertEqual(self.session._level, 3)

    def test_level_up_initializes_correct_at_level(self):

        self.session.level_up()

        self.assertEqual(self.session._correct_at_level, 0)

    def test_level_up_initializes_tries_at_level(self):

        self.session.level_up()

        self.assertEqual(self.session._tries_at_level, 0)

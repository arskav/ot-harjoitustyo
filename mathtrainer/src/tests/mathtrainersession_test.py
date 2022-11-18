import unittest
from entities.session import MathTrainerSession



class TestMathTrainerSession(unittest.TestCase):

    def setUp(self):
        self.session = MathTrainerSession("Testikäyttäjä", 1, 3, level=1, correct=2, tries=4,  correct_level=1, tries_level=2)


    #Pitääkö konstruktorin toiminta testata 
 
    def test_constructor_initialize_tries_correctly(self):
        
        self.assertEqual(self.session._tries, 4)

    def test_constructor_initialize_tries_level_correctly(self):
        
        self.assertEqual(self.session._tries_at_level, 2)


    #metodin _new_attempt() pitäisi kasvattaa yhdellä harjoitusten kokonaisyritysten _tries ja tason yritysten _tries_level lukumäärää    

    def test_new_attempt_increases_tries_correctly(self):

        self.session._new_attempt()

        self.assertEqual(self.session._tries, 5)


    def test_new_attempt_increases_tries_level_correctly(self):

        self.session._new_attempt()

        self.assertEqual(self.session._tries_at_level, 3)

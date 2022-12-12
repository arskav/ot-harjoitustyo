import unittest
from services.number_to_word import number_to_word, positive_number_to_word


class TestUtitities(unittest.TestCase):

    def test_positive_number_to_word(self):

        self.assertEqual(positive_number_to_word(1001011), "miljoona tuhat yksitoista")

    def test_number_to_word(self):

        self.assertEqual(number_to_word(-987654), "miinus yhdeksänsataakahdeksankymmentäseitsemäntuhatta kuusisataaviisikymmentäneljä")


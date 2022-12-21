import unittest
from unittest.mock import patch
from practises.practises3_questions.question1 import question1
from practises.practises3_questions.question2 import question2
from practises.practises3 import question


def fake_randomize1():
        #testausta varten kysymys 1, oikea vastaus näillä arvoilla 500
        return 1000,500,400,70,30,500

def fake_randomize2():
        #testausta varten kysymys 2, oikea vastaus näillä arvoilla 1030
        return 1000, 0, 0, 10, 2


class TestUtitities(unittest.TestCase):

    def setUp(self):

        question1.randomize(fake_randomize1)
        question2.randomize(fake_randomize2)

    @patch('builtins.input', return_value = '500')
    def test_question_correct(self, input):

        (is_correct, is_cancelled, is_finish) = question(0,1)

        #yksi oikea riittää lopetukseen
        self.assertEqual((is_correct, is_cancelled, is_finish), (True, False, True))

    @patch('builtins.input', return_value = '1000')
    def test_question_incorrect(self, input):

        (is_correct, is_cancelled, is_finish) = question(0,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, False, False))

    @patch('builtins.input', return_value = '1000+500-400-70-30-500')
    def test_question_cancelled(self, input):

        (is_correct, is_cancelled, is_finish) = question(0,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, True, False))


    @patch('builtins.input', return_value = '=1000+500-400-70-30-500')
    def test_question_correct_calculator(self, input):

        (is_correct, is_cancelled, is_finish) = question(0,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (True, False, True))

    @patch('builtins.input', return_value = '=1000+500')
    def test_question_incorrect_calculator(self, input):

        (is_correct, is_cancelled, is_finish) = question(0,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, False, False))

    @patch('builtins.input', return_value = '1030')
    def test_question2_correct(self, input):

        (is_correct, is_cancelled, is_finish) = question(0,2)

        #yksi oikea riittää lopetukseen
        self.assertEqual((is_correct, is_cancelled, is_finish), (True, False, True))

    @patch('builtins.input', return_value = '1000')
    def test_question2_incorrect(self, input):

        (is_correct, is_cancelled, is_finish) = question(0,2)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, False, False))

    @patch('builtins.input', return_value = '1000+30')
    def test_question2_cancelled(self, input):

        (is_correct, is_cancelled, is_finish) = question(0,2)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, True, False))


    @patch('builtins.input', return_value = '=1000+30')
    def test_question2_correct_calculator(self, input):

        (is_correct, is_cancelled, is_finish) = question(0,2)

        self.assertEqual((is_correct, is_cancelled, is_finish), (True, False, True))

    @patch('builtins.input', return_value = '=1000+20')
    def test_question2_incorrect_calculator(self, input):

        (is_correct, is_cancelled, is_finish) = question(0,2)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, False, False))

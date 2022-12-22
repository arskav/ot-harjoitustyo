import unittest
from unittest.mock import patch
import practises.practises2 as p


class TestUtitities(unittest.TestCase):


    def setUp(self):

            self.old_func1 = p.parameters
            p.parameters = self.fake_parameters


    def fake_parameters(self,level):
        #testausta varten, oikea vastaus näillä arvoilla 3 tasolla 1
        return 1,2


    @patch('builtins.input', return_value = '3')
    def test_question_correct(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(0,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (True, False, False))

    @patch('builtins.input', return_value = '4')
    def test_question_incorrect(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(0,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, False, False))

    @patch('builtins.input', return_value = '')
    def test_question_cancelled(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(0,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, True, False))


    @patch('builtins.input', return_value = '3')
    def test_question_correct_finished(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(1,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (True, False, True))

    @patch('builtins.input', return_value = '2')
    def test_question_incorrect_not_finished(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(1,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, False, False))
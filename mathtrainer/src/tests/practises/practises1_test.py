"""
idea https://stackoverflow.com/questions/3692159/how-do-i-redefine-functions-in-python
"""
import unittest
from unittest.mock import patch
import practises.practises1 as p


class TestUtitities(unittest.TestCase):

    def setUp(self):

            self.old_func1 = p.parameters
            p.parameters = self.fake_parameters


    def fake_parameters(self,level):
        #testausta varten, oikea vastaus tällä arvolla 123
        return 123


    @patch('builtins.input', return_value = '123')
    def test_question_correct(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(0,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (True, False, False))

    @patch('builtins.input', return_value = '1234')
    def test_question_incorrect(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(0,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, False, False))

    @patch('builtins.input', return_value = '')
    def test_question_cancelled(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(0,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, True, False))


    @patch('builtins.input', return_value = '123')
    def test_question_correct_finished(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(1,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (True, False, True))

    @patch('builtins.input', return_value = '1234')
    def test_question_incorrect_not_finished(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(1,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, False, False))
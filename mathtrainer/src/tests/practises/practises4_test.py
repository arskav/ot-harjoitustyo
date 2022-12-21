"""
idea https://stackoverflow.com/questions/3692159/how-do-i-redefine-functions-in-python
"""

import unittest
from unittest.mock import patch
import practises.practises4 as p


class TestUtitities(unittest.TestCase):

    def setUp(self):

        self.old_func1 = p.parameters
        p.parameters = self.fake_parameters


    def fake_parameters(self,level):
        #testausta varten, oikea vastaus näillä arvoilla -2
        return 3,6


    @patch('builtins.input', return_value = '3')
    def test_question1_correct(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(0,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (True, False, False))

    @patch('builtins.input', return_value = '-3')
    def test_question1_incorrect(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(0,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, False, False))

    @patch('builtins.input', return_value = '')
    def test_question1_cancelled(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(0,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, True, False))


    @patch('builtins.input', return_value = '3')
    def test_question1_correct_finished(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(1,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (True, False, True))

    @patch('builtins.input', return_value = '2')
    def test_question1_incorrect_not_finished(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(1,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, False, False))


    #Taso 2

    @patch('builtins.input', return_value = '-3')
    def test_question2_correct(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(0,2)

        self.assertEqual((is_correct, is_cancelled, is_finish), (True, False, False))

    @patch('builtins.input', return_value = '3')
    def test_question2_incorrect(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(0,2)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, False, False))

    @patch('builtins.input', return_value = '')
    def test_question2_cancelled(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(0,2)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, True, False))

    @patch('builtins.input', return_value = '-3')
    def test_question2_correct_finished(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(1,2)

        self.assertEqual((is_correct, is_cancelled, is_finish), (True, False, True))

    @patch('builtins.input', return_value = '2')
    def test_question1_incorrect_not_finished(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(1,1)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, False, False))

    #Taso 3
    @patch('builtins.input', return_value = '2')
    def test_question3_correct(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(0,3)

        self.assertEqual((is_correct, is_cancelled, is_finish), (True, False, False))

    @patch('builtins.input', return_value = '3')
    def test_question3_incorrect(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(0,3)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, False, False))

    @patch('builtins.input', return_value = '')
    def test_question3_cancelled(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(0,3)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, True, False))

    @patch('builtins.input', return_value = '2')
    def test_question3_correct_finished(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(1,3)

        self.assertEqual((is_correct, is_cancelled, is_finish), (True, False, True))

    @patch('builtins.input', return_value = '-2')
    def test_question3_incorrect_not_finished(self, input):

        (is_correct, is_cancelled, is_finish) = p.question(1,3)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, False, False))

    #Tasot 4,5 vastaavasti, tasoa 6 varten tarvittaisiin uudet parametrit.
    #Tehtävän 4 testaaminen tällä tavoin käytännössä copy-pastea
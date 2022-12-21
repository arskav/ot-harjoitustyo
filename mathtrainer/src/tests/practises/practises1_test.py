"""Testaamisen mahdollistamiseksi alkuperäiseen testattavaan koodiin lisättiin
tasoa 1000 vastaavat toiminnat."""

import unittest
from unittest.mock import patch
from practises.practises1 import question


class TestUtitities(unittest.TestCase):

    @patch('builtins.input', return_value = '123')
    def test_question_correct(self, input):

        (is_correct, is_cancelled, is_finish) = question(0,1000)

        self.assertEqual((is_correct, is_cancelled, is_finish), (True, False, False))

    @patch('builtins.input', return_value = '1234')
    def test_question_incorrect(self, input):

        (is_correct, is_cancelled, is_finish) = question(0,1000)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, False, False))

    @patch('builtins.input', return_value = '')
    def test_question_cancelled(self, input):

        (is_correct, is_cancelled, is_finish) = question(0,1000)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, True, False))


    @patch('builtins.input', return_value = '123')
    def test_question_correct_finished(self, input):

        (is_correct, is_cancelled, is_finish) = question(1,1000)

        self.assertEqual((is_correct, is_cancelled, is_finish), (True, False, True))

    @patch('builtins.input', return_value = '1234')
    def test_question_incorrect_not_finished(self, input):

        (is_correct, is_cancelled, is_finish) = question(1,1000)

        self.assertEqual((is_correct, is_cancelled, is_finish), (False, False, False))
import unittest
from services.utilities import list_to_string, string_to_list, correct_answer, cancel


class TestUtitities(unittest.TestCase):

    def test_list_to_string(self):

        self.assertEqual(list_to_string([1, 2, 3]), "1, 2, 3")

    def test_string_to_list(self):

        self.assertEqual(string_to_list("1, 2, 3"), [1, 2, 3])

    def test_empty_string_to_list(self):

        self.assertEqual(string_to_list(""), [])

    def test_correct_answer_not_finish(self):

        self.assertEqual(correct_answer(3,5), (False, 4))

    def test_correct_answer_finish(self):

        self.assertEqual(correct_answer(4,5), (True, 5))

    def test_cancel(self):

        self.assertEqual(cancel(), (False, True, False))


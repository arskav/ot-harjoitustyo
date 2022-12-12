import unittest
from services.utilities import list_to_string, string_to_list, correct_answer, draw_two_integers, is_number

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

    def test_draw_two_integers(self):

        for i in range(100):
            x, y = draw_two_integers(1,1,3,7)
            self.assertIn(x,[1])
            self.assertIn(y,[3,4,5,6,7])



    def test_is_number(self):

        self.assertEqual(is_number(''), False)
        self.assertEqual(is_number('abc'), False)
        self.assertEqual(is_number('123'), True)
        self.assertEqual(is_number('-999'), True)
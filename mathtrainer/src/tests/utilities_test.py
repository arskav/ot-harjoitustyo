import unittest
from services.utilities import list_to_string, string_to_list, dict_to_string, string_to_dict



class TestUtitities(unittest.TestCase):

    def test_list_to_string(self):

        self.assertEqual(list_to_string([1,2,3]), "1, 2, 3")

    def test_string_to_list(self):

        self.assertEqual(string_to_list("1, 2, 3"), [1,2,3])  

    def test_dict_to_string(self):

        self.assertEqual(dict_to_string({1:2,2:3,3:5}), "1:2,2:3,3:5")

    def test_string_to_dict(self):

        self.assertEqual(string_to_dict("1:2,2:3,3:5"), {1:2,2:3,3:5})


import unittest
from entities.user import MathTrainerUser


class TestMathTrainerUser(unittest.TestCase):

    # def __init__(self, username, started, finished, correct, tries):

    def setUp(self):
        self.trainee = MathTrainerUser(
            "Testaaja", {1: 4, 2: 1}, [1], 10, 20)

    def test_username_given_correctly(self):

        self.assertEqual(self.trainee.username(), "Testaaja")

    def test_practise_started_given_correctly(self):

        self.assertEqual(list(self.trainee.practise_started()), [1, 2])

    def test_practise_started_with_level_given_correctly(self):

        self.assertEqual(
            self.trainee.practise_started_with_level(), {1: 4, 2: 1})

    def test_practise_level(self):

        self.assertEqual(self.trainee.practise_level(1), 4)

    def test_practise_finished_given_correctly(self):

        self.assertEqual(self.trainee.practise_finished(), [1])

    def test_practise_started_append(self):

        self.trainee.practise_started_append(3)

        self.assertEqual(self.trainee.practise_started_with_level(), {
                         1: 4, 2: 1, 3: 1})

    def test_practise_finished_append(self):

        self.trainee.practise_finished_append(2)

        self.assertEqual(self.trainee.practise_finished(), [1, 2])

    def test_correct_total_given_correctly(self):

        self.assertEqual(self.trainee.correct_total(), 10)

    def test_tries_total_given_correctly(self):

        self.assertEqual(self.trainee.tries_total(), 20)

    def test_update_total_correct(self):

        self.trainee.update_total(5, 6, 2, 3)

        self.assertEqual(self.trainee.correct_total(), 15)

    def test_update_total_tries(self):

        self.trainee.update_total(5, 6, 2, 3)

        self.assertEqual(self.trainee.tries_total(), 26)

    def test_update_total_level(self):

        self.trainee.update_total(5, 6, 2, 3)

        self.assertEqual(
            self.trainee.practise_started_with_level(), {1: 4, 2: 3})

    def test_to_database(self):

        (username, started, finished, corrects, tries) = self.trainee.to_database()

        self.assertEqual((username, started, finished, corrects,
                         tries), ("Testaaja", "1:4,2:1", "1", 10, 20))

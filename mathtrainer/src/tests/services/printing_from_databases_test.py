import io
import unittest
from unittest.mock import patch
import sqlite3
from repositories.session_repository import session_repository
from repositories.user_repository import user_repository
from config import DATABASE_SESSIONS
from config import DATABASE_USERS
from initialize_databases import create_sessiontable, create_usertable
from entities.session import MathTrainerSession
from services.printing_from_databases import printing_service


class TestSessionRepository(unittest.TestCase):

    def setUp(self):

        my_connection = sqlite3.connect(DATABASE_SESSIONS)

        create_sessiontable(my_connection)

        cor = 0; tries = 0
        self.session1 = MathTrainerSession('arskaA', 1, 1)
        session_repository.insert_new_session(self.session1)
        cor_l = 10; tries_l = 20; cor += cor_l; tries += tries_l
        self.session1.set_corrects_and_tries(cor,tries, cor_l, tries_l)
        session_repository.update_session(self.session1)

        self.session2 = MathTrainerSession('arskaA', 1, 2)
        session_repository.insert_new_session(self.session2)
        cor_l = 12; tries_l = 21; cor += cor_l; tries += tries_l
        self.session2.set_corrects_and_tries(cor,tries, cor_l, tries_l)
        session_repository.update_session(self.session2)

        self.session3 = MathTrainerSession('arskaA', 1, 3)
        session_repository.insert_new_session(self.session3)
        cor_l = 14; tries_l = 22; cor += cor_l; tries += tries_l
        self.session3.set_corrects_and_tries(cor,tries, cor_l, tries_l)
        session_repository.update_session(self.session3)

        self.session4 = MathTrainerSession('arskaA', 1, 4)
        session_repository.insert_new_session(self.session4)
        cor_l = 16; tries_l = 23; cor += cor_l; tries += tries_l
        self.session4.set_corrects_and_tries(cor,tries, cor_l, tries_l)
        session_repository.update_session(self.session4)

        self.session5 = MathTrainerSession('arskaA', 1, 5)
        session_repository.insert_new_session(self.session5)
        cor_l = 18; tries_l = 24; cor += cor_l; tries += tries_l
        self.session5.set_corrects_and_tries(cor,tries, cor_l, tries_l)
        session_repository.update_session(self.session5)

        self.session6 = MathTrainerSession('arskaA', 1, 6)
        session_repository.insert_new_session(self.session6)
        cor_l = 20; tries_l = 25; cor += cor_l; tries += tries_l
        self.session6.set_corrects_and_tries(cor,tries, cor_l, tries_l)
        session_repository.update_session(self.session6)

        cor = 0; tries = 0
        self.session7 = MathTrainerSession('arskaA', 2, 1)
        session_repository.insert_new_session(self.session7)
        cor_l = 4; tries_l = 5; cor += cor_l; tries += tries_l
        self.session7.set_corrects_and_tries(cor,tries, cor_l, tries_l)
        session_repository.update_session(self.session7)

        self.session8 = MathTrainerSession('arskaA', 2, 2)
        session_repository.insert_new_session(self.session8)
        cor_l = 4; tries_l = 6; cor += cor_l; tries += tries_l
        self.session8.set_corrects_and_tries(cor,tries, cor_l, tries_l)
        session_repository.update_session(self.session8)

        cor = 0; tries = 0
        self.session9 = MathTrainerSession('arskaB', 1, 1)
        session_repository.insert_new_session(self.session9)
        cor_l = 5; tries_l = 10; cor += cor_l; tries += tries_l
        self.session9.set_corrects_and_tries(cor,tries, cor_l, tries_l)
        session_repository.update_session(self.session9)

        self.session10 = MathTrainerSession('arskaB', 1, 2)
        session_repository.insert_new_session(self.session10)
        cor_l = 4; tries_l = 10; cor += cor_l; tries += tries_l
        self.session10.set_corrects_and_tries(cor,tries, cor_l, tries_l)
        session_repository.update_session(self.session10)

        self.session11 = MathTrainerSession('arskaB', 1, 3)
        session_repository.insert_new_session(self.session11)
        cor_l = 5; tries_l = 20; cor += cor_l; tries += tries_l
        self.session11.set_corrects_and_tries(cor,tries, cor_l, tries_l)
        session_repository.update_session(self.session11)

        self.session12 =  MathTrainerSession('arskaC', 1, 1)
        session_repository.insert_new_session(self.session12)
        self.session12.set_corrects_and_tries(11,12, 11, 12)
        session_repository.update_session(self.session12)

        my_connection = sqlite3.connect(DATABASE_USERS)

        create_usertable(my_connection)

        user_repository.insert_new_user('arskaA')
        user_repository.update_user('arskaA', '1,2', '1', 102, 151)

        user_repository.insert_new_user('arskaB')
        user_repository.update_user('arskaB', '1', '', 14, 40)

        user_repository.insert_new_user('arskaC')
        user_repository.update_user('arskaC', '1', '', 11, 12)


    #idea https://realpython.com/lessons/mocking-print-unit-tests/
    @patch('builtins.print')
    def test_print_all_sessions_of_user_empty(self,mock_print):

        printing_service.print_all_sessions_of_user('outo')
        mock_print.assert_called_with("Ei suorituksia.")

    @patch('builtins.print')
    def test_print_all_sessions_of_practise_empty(self,mock_print):

        printing_service.print_all_sessions_of_practise(4)
        mock_print.assert_called_with("Ei suorituksia.")


    def test_print_statistics_of_practise(self):

        calculated_by_hand = {1: {'corrects': 26, 'tries': 42 }, 2: {'corrects': 16, 'tries': 31 },
        3: {'corrects': 19 , 'tries': 42},4: {'corrects': 16 , 'tries': 23},5: {'corrects': 18, 'tries': 24},
        6: {'corrects': 20, 'tries': 25 }}

        calculated_by_app =  printing_service.print_statistics_of_practise(1)

        self.assertDictEqual(calculated_by_app, calculated_by_hand)

    def test_print_statistics_of_practise_empty(self):

        calculated_by_hand = {}

        calculated_by_app =  printing_service.print_statistics_of_practise(4)

        self.assertDictEqual(calculated_by_app, calculated_by_hand)


    @patch('builtins.print')
    def test_print_all_users(self, mock_print):
        """Aakkosjärjestyksessä viimeinen käyttäjätunnus arskaC"""

        printing_service.print_all_users()

        mock_print.assert_called_with("arskaC")

    @patch('builtins.print')
    def test_print_all_users_with_practises(self, mock_print):
        """Aakkosjärjestyksessä viimeinen käyttäjätunnus arskaC"""

        printing_service.print_all_users_with_practises()

        mock_print.assert_called_with("arskaC aloitetut harjoitukset: 1, ei loppuun tehtyjä harjoituksia. oikein/yritykset: 11/12")

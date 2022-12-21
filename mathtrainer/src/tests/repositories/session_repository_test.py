import io
import unittest
from unittest.mock import patch
import sqlite3
from repositories.session_repository import session_repository
from config import DATABASE_SESSIONS
from initialize_databases import create_sessiontable
from entities.session import MathTrainerSession

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


    def test_insert_new_session(self):

        self.session13 = MathTrainerSession('arskaD', 4, 2)
        session_repository.insert_new_session(self.session13)

        sessions = session_repository.find_all_sessions()

        self.assertEqual(len(sessions), 13)
        self.assertEqual(sessions[12], (13, 'arskaD', 4, 0, 0, 2, 0, 0))


    def test_update_session(self):

        self.session13 = MathTrainerSession('arskaD', 4, 2)
        session_repository.insert_new_session(self.session13)
        self.session13.set_corrects_and_tries(100,200, 10, 20)
        session_repository.update_session(self.session13)
        sessions = session_repository.find_all_sessions()
        self.assertEqual(len(sessions), 13)
        self.assertEqual(sessions[12], (13, 'arskaD', 4, 100, 200, 2, 10, 20))


    def test_find_all_sessions(self):

        sessions = session_repository.find_all_sessions()
        self.assertEqual(len(sessions), 12)
        self.assertEqual(sessions[0][1:], ('arskaA', 1, 10, 20, 1, 10, 20))
        self.assertEqual(sessions[2][1:], ('arskaA', 1, 36, 63, 3, 14, 22))
        self.assertEqual(sessions[-1][1:], ('arskaC', 1, 11, 12, 1, 11, 12))

    def test_find_all_sessions_of_user(self):

        sessions = session_repository.find_all_sessions_of_user('arskaA')
        self.assertEqual(len(sessions), 8)
        self.assertEqual(sessions[0][1:], ('arskaA', 1, 10, 20, 1, 10, 20))
        self.assertEqual(sessions[-1][1:], ('arskaA', 2, 8, 11, 2, 4, 6))

        sessions = session_repository.find_all_sessions_of_user('arskaB')
        self.assertEqual(len(sessions), 3)
        self.assertEqual(sessions[-1][1:], ('arskaB', 1, 14, 40, 3, 5, 20))

        sessions = session_repository.find_all_sessions_of_user('arskaC')
        self.assertEqual(len(sessions), 1)
        self.assertEqual(sessions[0][1:], ('arskaC', 1, 11, 12, 1, 11, 12))

        sessions = session_repository.find_all_sessions_of_user('arska')
        self.assertEqual(len(sessions), 0)

    def test_find_all_sessions_of_practise(self):

        sessions = session_repository.find_all_sessions_of_practise(1)
        self.assertEqual(len(sessions), 10)
        self.assertEqual(sessions[0][1:], ('arskaA', 1, 10, 20, 1, 10, 20))
        self.assertEqual(sessions[7][1], 'arskaB')
        self.assertEqual(sessions[-1][1], 'arskaC')

        sessions = session_repository.find_all_sessions_of_practise(2)
        self.assertEqual(len(sessions), 2)
        self.assertEqual(sessions[0][1], 'arskaA')
        self.assertEqual(sessions[1][1], 'arskaA')

    def test_delete_all_sessions_of_user(self):

        sessions = session_repository.find_all_sessions_of_user('arskaB')
        self.assertEqual(len(sessions), 3)

        session_repository.delete_all_sessions_of_user('arskaB')

        sessions_after_deleting = session_repository.find_all_sessions_of_user('arskaB')

        self.assertEqual(len(sessions_after_deleting), 0)





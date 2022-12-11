import unittest
import sqlite3
from repositories.session_repository import session_repository
from initialize_databases import DATABASE_SESSIONS, create_sessiontable
from entities.session import MathTrainerSession

class TestSessionRepository(unittest.TestCase):

    def setUp(self):

        my_connection = sqlite3.connect(DATABASE_SESSIONS)

        create_sessiontable(my_connection)

        self.session1 = MathTrainerSession('arskaA', 1, 3)

        self.session2 = MathTrainerSession('arskaA', 1, 3)

        self.session2.set_corrects_and_tries(90,100,9,10)

        self.session3 =  MathTrainerSession('arskaB', 2, 1)

        self.session4 =  MathTrainerSession('arskaC', 1, 1)

    def test_insert_new_session(self):

        session_repository.insert_new_session(self.session1)

        session = session_repository.find_all_sessions()

        self.assertEqual(len(session), 1)
        self.assertEqual(session[0][1], 'arskaA')
        self.assertEqual(session[0][2], 1)
        self.assertEqual(session[0][3], 0)
        self.assertEqual(session[0][4], 0)
        self.assertEqual(session[0][5], 3)
        self.assertEqual(session[0][6], 0)
        self.assertEqual(session[0][7], 0)

    def test_update_session(self):

        session_repository.insert_new_session(self.session1)
        session_repository.update_session(self.session2)
        session = session_repository.find_all_sessions()
        self.assertEqual(len(session), 1)
        self.assertEqual(session[0][1], 'arskaA')
        self.assertEqual(session[0][2], 1)
        self.assertEqual(session[0][3], 90)
        self.assertEqual(session[0][4], 100)
        self.assertEqual(session[0][5], 3)
        self.assertEqual(session[0][6], 9)
        self.assertEqual(session[0][7], 10)

    def test_find_all_sessions(self):
        session_repository.insert_new_session(self.session1)
        session_repository.update_session(self.session2)
        session_repository.insert_new_session(self.session3)
        session_repository.insert_new_session(self.session4)
        session = session_repository.find_all_sessions()
        self.assertEqual(len(session), 3)
        self.assertEqual(session[0][1], 'arskaA')
        self.assertEqual(session[0][2], 1)
        self.assertEqual(session[0][3], 90)
        self.assertEqual(session[0][4], 100)
        self.assertEqual(session[0][5], 3)
        self.assertEqual(session[0][6], 9)
        self.assertEqual(session[0][7], 10)
        self.assertEqual(session[1][1], 'arskaB')
        self.assertEqual(session[1][2], 2)
        self.assertEqual(session[1][3], 0)
        self.assertEqual(session[1][4], 0)
        self.assertEqual(session[1][5], 1)
        self.assertEqual(session[1][6], 0)
        self.assertEqual(session[1][7], 0)
        self.assertEqual(session[2][1], 'arskaC')
        self.assertEqual(session[2][2], 1)
        self.assertEqual(session[2][3], 0)
        self.assertEqual(session[2][4], 0)
        self.assertEqual(session[2][5], 1)
        self.assertEqual(session[2][6], 0)
        self.assertEqual(session[2][7], 0)

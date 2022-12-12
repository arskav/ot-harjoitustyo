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
        sessions = session_repository.find_all_sessions()
        self.assertEqual(len(sessions), 3)
        self.assertEqual(sessions[0][1], 'arskaA')
        self.assertEqual(sessions[0][2], 1)
        self.assertEqual(sessions[0][3], 90)
        self.assertEqual(sessions[0][4], 100)
        self.assertEqual(sessions[0][5], 3)
        self.assertEqual(sessions[0][6], 9)
        self.assertEqual(sessions[0][7], 10)
        self.assertEqual(sessions[1][1], 'arskaB')
        self.assertEqual(sessions[1][2], 2)
        self.assertEqual(sessions[1][3], 0)
        self.assertEqual(sessions[1][4], 0)
        self.assertEqual(sessions[1][5], 1)
        self.assertEqual(sessions[1][6], 0)
        self.assertEqual(sessions[1][7], 0)
        self.assertEqual(sessions[2][1], 'arskaC')
        self.assertEqual(sessions[2][2], 1)
        self.assertEqual(sessions[2][3], 0)
        self.assertEqual(sessions[2][4], 0)
        self.assertEqual(sessions[2][5], 1)
        self.assertEqual(sessions[2][6], 0)
        self.assertEqual(sessions[2][7], 0)

    def test_find_all_sessions_of_user(self):
        session_repository.insert_new_session(self.session1)
        session_repository.update_session(self.session2)
        session_repository.insert_new_session(self.session3)
        session_repository.insert_new_session(self.session4)
        self.session5 =  MathTrainerSession('arskaC', 2, 1)
        session_repository.insert_new_session(self.session5)

        sessions = session_repository.find_all_sessions_of_user('arskaA')
        self.assertEqual(len(sessions), 1)
        self.assertEqual(sessions[0][1], 'arskaA')
        self.assertEqual(sessions[0][2], 1)
        self.assertEqual(sessions[0][3], 90)
        self.assertEqual(sessions[0][4], 100)
        self.assertEqual(sessions[0][5], 3)
        self.assertEqual(sessions[0][6], 9)
        self.assertEqual(sessions[0][7], 10)

        sessions = session_repository.find_all_sessions_of_user('arskaC')
        self.assertEqual(len(sessions), 2)
        self.assertEqual(sessions[0][1], 'arskaC')
        self.assertEqual(sessions[0][2], 1)
        self.assertEqual(sessions[0][3], 0)
        self.assertEqual(sessions[0][4], 0)
        self.assertEqual(sessions[0][5], 1)
        self.assertEqual(sessions[0][6], 0)
        self.assertEqual(sessions[0][7], 0)
        self.assertEqual(sessions[1][1], 'arskaC')
        self.assertEqual(sessions[1][2], 2)
        self.assertEqual(sessions[1][3], 0)
        self.assertEqual(sessions[1][4], 0)
        self.assertEqual(sessions[1][5], 1)
        self.assertEqual(sessions[1][6], 0)
        self.assertEqual(sessions[1][7], 0)



    def test_find_all_sessions_of_practise(self):
        session_repository.insert_new_session(self.session1)
        session_repository.update_session(self.session2)
        session_repository.insert_new_session(self.session3)
        session_repository.insert_new_session(self.session4)
        sessions = session_repository.find_all_sessions_of_practise(1)
        self.assertEqual(len(sessions), 2)
        self.assertEqual(sessions[0][1], 'arskaA')
        self.assertEqual(sessions[0][2], 1)
        self.assertEqual(sessions[0][3], 90)
        self.assertEqual(sessions[0][4], 100)
        self.assertEqual(sessions[0][5], 3)
        self.assertEqual(sessions[0][6], 9)
        self.assertEqual(sessions[0][7], 10)
        self.assertEqual(sessions[1][1], 'arskaC')
        self.assertEqual(sessions[1][2], 1)
        self.assertEqual(sessions[1][3], 0)
        self.assertEqual(sessions[1][4], 0)
        self.assertEqual(sessions[1][5], 1)
        self.assertEqual(sessions[1][6], 0)
        self.assertEqual(sessions[1][7], 0)


        session = session_repository.find_all_sessions_of_practise(2)
        self.assertEqual(len(session), 1)
        self.assertEqual(session[0][1], 'arskaB')
        self.assertEqual(session[0][2], 2)
        self.assertEqual(session[0][3], 0)
        self.assertEqual(session[0][4], 0)
        self.assertEqual(session[0][5], 1)
        self.assertEqual(session[0][6], 0)
        self.assertEqual(session[0][7], 0)


    def test_find_all_sessions(self):
        session_repository.insert_new_session(self.session1)
        session_repository.update_session(self.session2)
        session_repository.insert_new_session(self.session3)
        session_repository.insert_new_session(self.session4)
        data = session_repository.find_session_of_user('arskaA',1)
        self.assertEqual(data[0], 90)
        self.assertEqual(data[1], 100)
        self.assertEqual(data[2], 3)
        self.assertEqual(data[3], 9)
        self.assertEqual(data[4], 10)

        data = session_repository.find_session_of_user('arskaA',2)
        self.assertEqual(data[0], None)
        self.assertEqual(data[1], None)
        self.assertEqual(data[2], None)
        self.assertEqual(data[3], None)
        self.assertEqual(data[4], None)


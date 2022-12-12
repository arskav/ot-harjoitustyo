import unittest
import sqlite3
from repositories.user_repository import user_repository
from initialize_databases import DATABASE_USERS, create_usertable


class TestUserRepository(unittest.TestCase):

    def setUp(self):

        my_connection = sqlite3.connect(DATABASE_USERS)

        create_usertable(my_connection)

        #self.user_arska = User('arska', [1,2], [1], 5, 10)

    def test_insert_new_user(self):

        user_repository.insert_new_user('arska')

        users = user_repository.find_all_users_with_practises()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][1], 'arska')
        self.assertEqual(users[0][2], '')
        self.assertEqual(users[0][3], '')
        self.assertEqual(users[0][4], 0)
        self.assertEqual(users[0][5], 0)

    def test_update_user(self):

        user_repository.insert_new_user('arska')
        user_repository.update_user('arska','1,2','1', 10, 20)
        users = user_repository.find_all_users_with_practises()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][1], 'arska')
        self.assertEqual(users[0][2], '1,2')
        self.assertEqual(users[0][3], '1')
        self.assertEqual(users[0][4], 10)
        self.assertEqual(users[0][5], 20)

    def test_find_all_users(self):

        user_repository.insert_new_user('ArskaB')
        user_repository.insert_new_user('arskaA')
        user_repository.insert_new_user('arskaC')
        #aakkosjärjestys, isoja kirjainkokoa ei huomioida:
        #arskaA, ArskaB, arskaC
        users = user_repository.find_all_users()
        self.assertEqual(len(users), 3)
        self.assertEqual(users[0][0], 'arskaA')
        self.assertEqual(users[1][0], 'ArskaB')
        self.assertEqual(users[2][0], 'arskaC')

    def test_find_all_users_with_practises(self):

        user_repository.insert_new_user('arskaB')
        user_repository.insert_new_user('arskaA')
        user_repository.update_user('arskaA','1,2','1', 10, 20)
        user_repository.update_user('arskaB','1,2,3,4','1,2', 30, 100)
        usersdata = user_repository.find_all_users_with_practises()
        self.assertEqual(usersdata[0][1], 'arskaA')
        self.assertEqual(usersdata[0][2], '1,2')
        self.assertEqual(usersdata[0][3], '1')
        self.assertEqual(usersdata[0][4], 10)
        self.assertEqual(usersdata[0][5], 20)
        self.assertEqual(usersdata[1][1], 'arskaB')
        self.assertEqual(usersdata[1][2], '1,2,3,4')
        self.assertEqual(usersdata[1][3], '1,2')
        self.assertEqual(usersdata[1][4], 30)
        self.assertEqual(usersdata[1][5], 100)

    def test_find_user(self):

        user_repository.insert_new_user('arskaB')
        user_repository.insert_new_user('arskaA')
        user_repository.insert_new_user('arskaC')
        user_repository.update_user('arskaB','1,2,3,4','1,2', 30, 100)
        userdata = user_repository.find_user('arskaB')
        self.assertEqual(userdata[1], 'arskaB')
        self.assertEqual(userdata[2], '1,2,3,4')
        self.assertEqual(userdata[3], '1,2')
        self.assertEqual(userdata[4], 30)
        self.assertEqual(userdata[5], 100)
        userdata = user_repository.find_user('outo_tyyppi')
        self.assertEqual(userdata, None)

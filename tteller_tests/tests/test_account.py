import unittest
from app import account
import os

account.DBPATH = "_test.json"  # make sure your tests aren't messing up your real data

class TestAccount(unittest.TestCase):

    def setUp(self):
        # this code runs prior to every test case
        # it is important to know that test cases do not run in a predictable order
        # the purpose of setUp is to make sure assumptions are correct (data is in
        # the state you want it to be etc.)

        try:
            os.remove("_test.json")
        except FileNotFoundError:
            pass
    
    def test_creation(self):

        nobody = account.Account()
        self.assertIsNone(nobody.first_name, "default for first_name should be None")

        mike = account.Account(first_name="Mike", last_name="Bloom")
    
    def test_save(self):
        mike = account.Account(first_name="Mike", last_name="Bloom", account_number="123456")
        mike.save()

        testmike = account.Account.from_account_number("123456")
        self.assertEqual(testmike.first_name, "Mike", "Saved account is loaded from file")
    
    def test_login(self):
        pass

    
    def test_deposit(self):
        pass

    def test_withdraw(self):
        mike = account.Account(account_number="123456", balance=100.0)

        mike.withdraw(50.0)
        self.assertAlmostEqual(mike.balance, 50.0, "balance removes money")

        with self.assertRaises(account.InsufficientFundsError, msg="Overdraft should raise insufficient funds error"):  # note you don't need an 'as'
            mike.withdraw(10.0)

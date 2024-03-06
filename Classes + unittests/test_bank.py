import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):
    account1 = BankAccount(8604, "Lea", 10000.00)

    def setUp(self):
        self.account3 = BankAccount(8604, "Lea", 10000.00)

    def testConstructor(self):
        self.assertEqual(8604, self.account1.account_number)

    def test_deposit(self):
        print('test_deposit')
        account2 = BankAccount(8604, "Lea", 10000.00)
        account2.deposit(2500.00)
        self.assertEqual(account2.balance, 12500.00)
        self.account1.deposit(2500.00)
        self.assertEqual(self.account1.balance, 12500.00)
        self.account3
        #self.assertEqual(account2.deposit(-1000.0), 12500.0, 'Failed to deposit a valid amount')

    def test_withdraw(self):
        print('test_withdraw')
        self.account3.withdraw(2500.0)
        self.assertEqual(self.account3.balance, 7500.0)
        self.account3.withdraw(0.0)
        self.assertEqual(self.account3.balance, 7500.0, 'Failed to withdraw a valid amount')
        self.account3.withdraw(-500.0)
        self.assertEqual(self.account3.balance, 7500.0, 'Failed to withdraw a valid amount')

if __name__ == '__main__':
    unittest.main()
    

'''#Instance of bankaccount class
account1 = BankAccount(8604, "Lea Albano", 10000.0)
account1.deposit(2500.0)
account1.withdraw(-200.0)
account1.print_details()'''
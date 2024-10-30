import unittest
from transaction import Transaction
from user import User

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.user = User.register("testuser3", "password789")

    def test_add_transaction(self):
        Transaction.add_transaction(self.user.id, 100, "Food", "Groceries", "expense")
        transactions = Transaction.get_transactions(self.user.id)
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0][2], 100)
        self.assertEqual(transactions[0][3], "Food")
        self.assertEqual(transactions[0][4], "Groceries")
        self.assertEqual(transactions[0][5], "expense")

if __name__ == '__main__':
    unittest.main()
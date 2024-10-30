import unittest
from report import Report
from user import User
from transaction import Transaction

class TestReport(unittest.TestCase):
    def setUp(self):
        self.user = User.register("testuser5", "password131415")
        Transaction.add_transaction(self.user.id, 1000, "Salary", "Monthly salary", "income")
        Transaction.add_transaction(self.user.id, 200, "Food", "Groceries", "expense")
        Transaction.add_transaction(self.
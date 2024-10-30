import unittest
from budget import Budget
from user import User

class TestBudget(unittest.TestCase):
    def setUp(self):
        self.user = User.register("testuser4", "password101112")

    def test_set_and_get_budget(self):
        Budget.set_budget(self.user.id, "Food", 500)
        budgets = Budget.get_budgets(self.user.id)
        self.assertEqual(len(budgets), 1)
        self.assertEqual(budgets[0][2], "Food")
        self.assertEqual(budgets[0][3], 500)

if __name__ == '__main__':
    unittest.main()
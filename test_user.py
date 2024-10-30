import unittest
from user import User

class TestUser(unittest.TestCase):
    def test_register(self):
        user = User.register("testuser", "password123")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "testuser")

    def test_login(self):
        User.register("testuser2", "password456")
        user = User.login("testuser2", "password456")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "testuser2")

    def test_login_fail(self):
        user = User.login("nonexistent", "wrongpassword")
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()
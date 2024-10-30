from database import db
from datetime import datetime

class Transaction:
    @staticmethod
    def add_transaction(user_id, amount, category, description, transaction_type):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.execute(
            "INSERT INTO transactions (user_id, amount, category, description, type, date) VALUES (?, ?, ?, ?, ?, ?)",
            (user_id, amount, category, description, transaction_type, date)
        )

    @staticmethod
    def get_transactions(user_id):
        db.execute("SELECT * FROM transactions WHERE user_id = ? ORDER BY date DESC", (user_id,))
        return db.fetchall()
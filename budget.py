from database import db

class Budget:
    @staticmethod
    def set_budget(user_id, category, amount):
        db.execute(
            "INSERT OR REPLACE INTO budgets (user_id, category, amount) VALUES (?, ?, ?)",
            (user_id, category, amount)
        )

    @staticmethod
    def get_budgets(user_id):
        db.execute("SELECT * FROM budgets WHERE user_id = ?", (user_id,))
        return db.fetchall()

    @staticmethod
    def check_budget(user_id, category):
        db.execute(
            "SELECT b.amount, COALESCE(SUM(t.amount), 0) as spent FROM budgets b "
            "LEFT JOIN transactions t ON b.user_id = t.user_id AND b.category = t.category "
            "WHERE b.user_id = ? AND b.category = ? AND t.type = 'expense' "
            "GROUP BY b.category",
            (user_id, category)
        )
        result = db.fetchone()
        if result:
            budget, spent = result
            return budget - spent
        return None
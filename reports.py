from database import db

class Report:
    @staticmethod
    def generate_monthly_report(user_id, year, month):
        start_date = f"{year}-{month:02d}-01"
        end_date = f"{year}-{month:02d}-31"
        return Report._generate_report(user_id, start_date, end_date)

    @staticmethod
    def generate_yearly_report(user_id, year):
        start_date = f"{year}-01-01"
        end_date = f"{year}-12-31"
        return Report._generate_report(user_id, start_date, end_date)

    @staticmethod
    def _generate_report(user_id, start_date, end_date):
        db.execute(
            "SELECT type, SUM(amount) FROM transactions "
            "WHERE user_id = ? AND date BETWEEN ? AND ? "
            "GROUP BY type",
            (user_id, start_date, end_date)
        )
        results = db.fetchall()

        total_income = next((r[1] for r in results if r[0] == 'income'), 0)
        total_expenses = next((r[1] for r in results if r[0] == 'expense'), 0)

        db.execute(
            "SELECT category, SUM(amount) FROM transactions "
            "WHERE user_id = ? AND date BETWEEN ? AND ? AND type = 'expense' "
            "GROUP BY category",
            (user_id, start_date, end_date)
        )
        category_expenses = dict(db.fetchall())

        return {
            'total_income': total_income,
            'total_expenses': total_expenses,
            'savings': total_income - total_expenses,
            'category_expenses': category_expenses
        }
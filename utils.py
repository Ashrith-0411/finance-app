import json

def backup_data(filename='backup.json'):
    from database import db
    
    db.execute("SELECT * FROM users")
    users = db.fetchall()
    
    db.execute("SELECT * FROM transactions")
    transactions = db.fetchall()
    
    db.execute("SELECT * FROM budgets")
    budgets = db.fetchall()
    
    data = {
        'users': users,
        'transactions': transactions,
        'budgets': budgets
    }
    
    with open(filename, 'w') as f:
        json.dump(data, f)
    
    print(f"Data backed up to {filename}")

def restore_data(filename='backup.json'):
    from database import db
    
    with open(filename, 'r') as f:
        data = json.load(f)
    
    db.execute("DELETE FROM users")
    db.execute("DELETE FROM transactions")
    db.execute("DELETE FROM budgets")
    
    for user in data['users']:
        db.execute("INSERT INTO users VALUES (?, ?, ?)", user)
    
    for transaction in data['transactions']:
        db.execute("INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?, ?)", transaction)
    
    for budget in data['budgets']:
        db.execute("INSERT INTO budgets VALUES (?, ?, ?, ?)", budget)
    
    print(f"Data restored from {filename}")
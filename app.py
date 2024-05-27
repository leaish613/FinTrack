from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to create the transactions table
def create_table():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    amount REAL,
                    category TEXT,
                    type TEXT
                 )''')
    conn.commit()
    conn.close()

# Function to create the users table
def create_users_table():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT
                 )''')
    conn.commit()
    conn.close()

# Call the function to create the tables
create_table()
create_users_table()

# Function to fetch all transactions from the database
def get_transactions():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM transactions''')
    transactions = c.fetchall()
    conn.close()
    return transactions

# Route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get name from the form
        name = request.form['name']
        # Insert or update user into the database
        conn = sqlite3.connect('finance.db')
        c = conn.cursor()
        c.execute('''INSERT OR REPLACE INTO users (id, name) VALUES (1, ?)''', (name,))
        conn.commit()
        conn.close()
        return redirect(url_for('tracker'))
    return render_template('login.html')

# Function to fetch user's name
def get_user_name():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('''SELECT name FROM users WHERE id = 1''')
    user = c.fetchone()
    conn.close()
    return user[0] if user else None

# Route for the finance tracker page
@app.route('/tracker', methods=['POST', 'GET'])
def tracker():
    name = get_user_name()
    if not name:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Get transaction details from the form
        title = request.form['title']
        amount = float(request.form['amount'])
        category = request.form['category']
        transaction_type = request.form['type']

        # Insert transaction into the database
        conn = sqlite3.connect('finance.db')
        c = conn.cursor()
        c.execute('''INSERT INTO transactions (title, amount, category, type) 
                     VALUES (?, ?, ?, ?)''', (title, amount, category, transaction_type))
        conn.commit()
        conn.close()
        return redirect(url_for('tracker'))

    # Fetch all transactions from the database
    transactions = get_transactions()

    # Calculate total income and expenses
    income = sum(transaction[2] for transaction in transactions if transaction[4] == 'income')
    expenses = sum(transaction[2] for transaction in transactions if transaction[4] == 'expense')

    return render_template('tracker.html', name=name, transactions=transactions, income=income, expenses=expenses)

# Route to delete a transaction
@app.route('/delete/<int:id>')
def delete_transaction(id):
    # Delete transaction from the database
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('''DELETE FROM transactions WHERE id=?''', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('tracker'))

if __name__ == '__main__':
    app.run(debug=True)

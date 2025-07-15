from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3, os

app = Flask(__name__)
app.secret_key = 'secret'

# Create DB if not exists
def init_db():
    if not os.path.exists('users.db'):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )''')
        conn.commit()
        conn.close()

init_db()

# ---- ROUTES ----
@app.route('/')
def login_page():
    return render_template('teacher_login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        session['username'] = username
        return redirect('/dashboard')
    else:
        flash("Login failed: Invalid username or password.")
        return redirect('/')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    try:
        conn = sqlite3.connect('users.d

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import re
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
app.secret_key = os.environ.get('SECRET_KEY')


#signup 
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email'].lower().strip()
        username = request.form['username'].lower().strip()
        password = request.form['password'].strip()
        repeat_password = request.form['repeat-password'].strip()

        if not email or not username or not password or not repeat_password:
            return render_template('signup.html', error="All fields are required. Please go back and complete all fields.")

        if not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
            return render_template('signup.html', error="Please enter a valid email address.")

        if len(password) < 8 or len(password) > 14:
            return render_template('signup.html', error="Password must be between 8 and 14 characters.")

        if not re.search(r'\d', password) or not re.search(r'[A-Za-z]', password):
            return render_template('signup.html', error="Password must contain at least one letter and one number.")

        if password != repeat_password:
            return render_template('signup.html', error="Passwords do not match. Please go back and try again.")

        if not re.match(r'^[\w-]+$', username, re.UNICODE):
            return render_template('signup.html', error="Username can only contain letters, numbers, hyphens, and underscores.")

        password_hash = generate_password_hash(password, method='pbkdf2:sha256')

        conn = sqlite3.connect('hashitracker.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
        if cursor.fetchone():
            conn.close()
            return render_template('signup.html', error="That email is already registered. Please go back and try again.")

        cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
        if cursor.fetchone():
            conn.close()
            return render_template('signup.html', error="That username is already taken. Please go back and try again.")

        cursor.execute(
            'INSERT INTO users (email, username, password_hash) VALUES (?, ?, ?)',
            (email, username, password_hash)
        )
        conn.commit()
        conn.close()

        return render_template('signup_success.html', username=username, email=email)

    return render_template('signup.html')

#login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].lower().strip()
        password = request.form['password'].strip()

        if not username or not password:
            return render_template('login.html', error="Please enter both username and password.")

        conn = sqlite3.connect('hashitracker.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, password_hash FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        conn.close()

        if result is None:
            return render_template('login.html', error="Incorrect username or password")

        user_id, stored_hash = result
        if not check_password_hash(stored_hash, password):
            return render_template('login.html', error="Incorrect username or password")

        session['user_id'] = user_id
        return redirect(url_for('home'))


    return render_template('login.html')

@app.route('/recovery')
def recovery():
    return render_template('recovery.html')

@app.route('/home')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True, port=5001)
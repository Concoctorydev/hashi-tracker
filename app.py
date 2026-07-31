from flask import Flask, render_template, request
import sqlite3
from werkzeug.security import generate_password_hash
import re

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True, port=5001)
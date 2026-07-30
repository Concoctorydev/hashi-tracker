from flask import Flask, render_template, request
import sqlite3
from werkzeug.security import generate_password_hash

app = Flask(__name__)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        repeat_password = request.form['repeat-password']

        if not email or not username or not password or not repeat_password:
            return render_template('signup.html', error="All fields are required. Please go back and complete all fields.")

        if password != repeat_password:
            return render_template('signup.html', error="Passwords do not match. Please go back and try again.")

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

        return f"Signed up: {username} ({email})"

    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
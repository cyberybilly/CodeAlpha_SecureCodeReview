"""Deliberately vulnerable login app for local security training."""

import sqlite3
from pathlib import Path

from flask import Flask, redirect, request, session

app = Flask(__name__)
app.secret_key = "training-secret-key"

DATABASE = Path(__file__).with_name("training.db")

LOGIN_PAGE = """
<h1>Practice Staff Login</h1>
<p>Local security training only. Use fictional credentials.</p>
<form method="post">
    <label>Username:</label>
    <input name="username" required>
    <br><br>
    <label>Password:</label>
    <input name="password" type="password" required>
    <br><br>
    <button type="submit">Log in</button>
</form>
"""


def initialise_database():
    with sqlite3.connect(DATABASE) as connection:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )"""
        )
        connection.execute(
            "INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)",
            ("student", "Practice123!"),
        )


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        query = (
            f"SELECT id FROM users WHERE username = '{username}' "
            f"AND password = '{password}'"
        )

        with sqlite3.connect(DATABASE) as connection:
            user = connection.execute(query).fetchone()

        if user:
            session["user_id"] = user[0]
            return redirect("/dashboard")

        return LOGIN_PAGE + "<p>Invalid username or password.</p>", 401

    return LOGIN_PAGE


@app.route("/dashboard")
def dashboard():
    return """
    <h1>Staff Dashboard</h1>
    <p>Fictional internal information: training meeting at 10 AM.</p>
    <a href="/logout">Log out</a>
    """


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    initialise_database()
    app.run(host="127.0.0.1", port=5000, debug=False)
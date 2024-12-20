from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["SECRET_KEY"] = "hardcoded_secret_key"

# Database setup
def init_db():
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("home.html")

# SQL Injection Vulnerability
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute(query)  # Vulnerable to SQL injection
    user = cursor.fetchone()
    conn.close()
    if user:
        return "Logged in!"
    return "Invalid credentials!"

# Insecure File Upload
@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))  # No validation
        return "File uploaded!"
    return render_template("upload.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

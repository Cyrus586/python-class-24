from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import secrets
import re 

secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.secret_key = secret_key




users = []

def is_valid_password(password):
    return len(password) >= 8

def is_valid_name(username):
    return re.match('^[a-zA-Z0-9_-]+$', username) is not None

def is_valid_email(email):
    return re.match("@", email) is not None



# end def
@app.route("/")
def index():
    return render_template("signup.html")

@app.route("/signup", methods=["post"])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")
    email    = request.form.get("email")
    con_pass = request.form.get("c_password")
    
    
    
    if not is_valid_name(username):
        flash('Invalid username. Use only letters, numbers, underscore, and hyphens', 'error')
        return redirect(url_for('index'))

    if not is_valid_password(password):
        flash('Invalid password. Password must be at least 8 characters long. ', 'error')
        return redirect(url_for('index'))

    if not password != con_pass:
        flash("Passwords donot match.", "error")
        return redirect(url_for("index"))
    
    if not username or not password or not email or not con_pass:
        flash("All Fields are required.", "error")
        return redirect(url_for("index"))
    
    users.append({"username": username, "password": password, "email": email })
    flash("Sign-up Successful!", "success")
    return redirect(url_for("index"))
    
# end def

if __name__ == "__main__":
    app.run(debug=True)
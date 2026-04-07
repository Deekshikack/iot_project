=from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def do_login():
    email = request.form['email']
    password = request.form['password']

    # simple login
    if email == "admin@gmail.com" and password == "1234":
        return redirect('/dashboard')
    else:
        return "Invalid Login"

@app.route('/dashboard')
def dashboard():
    temp = random.randint(20, 60)
    hum = random.randint(30, 90)
    energy = random.randint(100, 500)

    alert = ""
    if temp > 50:
        alert = "⚠️ High Temperature!"

    return render_template("dashboard.html",
                           temp=temp,
                           hum=hum,
                           energy=energy,
                           alert=alert,
                           data=[])

if __name__ == "__main__":
    app.run(debug=True)
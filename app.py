from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ganti dengan username dan password yang kamu inginkan
USERNAME = "cintaku"
PASSWORD = "071198"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/check_login', methods=['POST'])
def check_login():
    username = request.form['username']
    password = request.form['password']
    if username == USERNAME and password == PASSWORD:
        return redirect(url_for('birthday'))
    else:
        return "<h3 style='color:red'>Username atau Password salah!</h3>"

@app.route('/birthday')
def birthday():
    return render_template('birthday.html')

if __name__ == '__main__':
    app.run(debug=True)

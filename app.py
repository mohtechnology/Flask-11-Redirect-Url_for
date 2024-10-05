from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the home page"

@app.route('/user/<name>')
def user(name):
    return redirect('/')

@app.route('/go-home')
def go_home():
    return redirect(url_for('user', name = "moh"))

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello Sundaytoz"

@app.route("login")
def login():
    value = 1+2
    return "login ok"

@app.route("logout")
def logout():
    return "logout ok"


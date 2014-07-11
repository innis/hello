from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello Sundaytoz"

@app.route("logout")
def logout():
    return "logout ok"
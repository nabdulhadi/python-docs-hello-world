from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Sakher this is my first Webapp!"

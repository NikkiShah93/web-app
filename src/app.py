from flask import Flask

## creating an app
app = Flask(__name__)

## adding the first route
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
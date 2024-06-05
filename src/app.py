from flask import Flask, jsonify, render_template

## creating an app
app = Flask(__name__)

## adding the first route
@app.route("/")
def hello_world():
    return render_template("index.html")

## adding the health end point
## to check if the service is up and running
@app.route("/health")
def health():
    return jsonify(status="UP")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
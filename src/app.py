from flask import Flask, jsonify, render_template
import socket

## creating an app
app = Flask(__name__)

def fetch():
    host = str(socket.gethostname())
    ip = str(socket.gethostbyname(host))
    return host, ip

## adding the first route
@app.route("/")
def hello_world():
    return render_template("index.html")

## adding the health end point
## to check if the service is up and running
@app.route("/health")
def health():
    return jsonify(status="UP")

## adding the details path
## for checking the host
## and IP of the contianer
@app.route("/details")
def details():
    host, ip = fetch()
    return render_template("details.html", HOST=host, IP=ip)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
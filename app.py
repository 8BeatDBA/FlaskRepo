

from flask import Flask, request
from pytest import Item

app = Flask(__name__)



def check_server_status():
    return "Up and Running !!! "

@app.route("/main")
def home():
    check_server_status()
    return "Server is up and running! Listening for requests.. "



# New POST route
@app.route("/data", methods=["POST"])
def data():
    content = request.json
    return f"Received: {content}", 200


if __name__ == "__main__":
    app.run(debug=True)
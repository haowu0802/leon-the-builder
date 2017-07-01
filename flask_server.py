import os  # for getting env vars

from flask import Flask  # flask micro framework

app = Flask(__name__)  # init flask application


# index
@app.route("/")
def hello():
    return "Leon the builder"


# log form
@app.route("/log")
def log():
    return "log form"


# main
if __name__ == '__main__':
    app.debug = True  # restart on file change
    port = int(os.environ.get("PORT", 5001))  # for heroku, port is in env var
    app.run(host='0.0.0.0', port=port)  # server start with env var port

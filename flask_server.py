import os  # for getting env vars

from flask import Flask  # flask microframework

app = Flask(__name__)  # init flask application


# index
@app.route("/")
def hello():
    return "Hello Flask!"

# main
if __name__ == '__main__':
    app.debug = True  # restart on file change
    port = int(os.environ.get("PORT", 5001))  # for heroku, port is in env var
    app.run(host='0.0.0.0', port=port)  # server start with env var port

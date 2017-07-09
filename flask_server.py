import os  # for getting env vars

from flask import Flask  # flask micro framework
from flask import render_template  # template render
from flask import request  # for rest apis
from flask import flash  # flash messages
from flask import url_for  # url maker
from flask import redirect  # redirects

# import pymongo  # mongodb support

app = Flask(__name__)  # init flask application


# index
@app.route("/")
def index():
    return render_template('index.html')  # index page


# log form
@app.route("/log", methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        pass
        # flash("log added" % item.name)  # add flash message to message queue
        return redirect(url_for('log'))  # redirect to logs
    else:
        return render_template('log.html')  # log form page


# main
if __name__ == '__main__':
    app.debug = True  # restart on file change
    port = int(os.environ.get("PORT", 5001))  # for heroku, port is in env var
    app.run(host='0.0.0.0', port=port)  # server start with env var port

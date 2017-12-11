import sqlite3
from datetime import datetime
from flask import Flask, redirect
import constants


tenhash = Flask(constants.TENHASH)
tenhash.config.from_object('config.DevelopmentConfig')
tenhash.config.from_pyfile(constants.TENHASH_SETTINGS, silent=False)


@tenhash.route('/')
def homepage():
    """This is to render the homepage"""
    return redirect("http://posts.tenhash.com", code=302)


@tenhash.route('/spa')
def single_page_application():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    return """
    <h1>Hello Tenhash users</h1></br>
    <h2>Welcome to First Single Page Application</h2>
    <p>It is currently {time}.</p>  
    """.format(time=the_time)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(tenhash.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


if constants.TENHASH == '__main__':
    tenhash.run(debug=True, use_reloader=True)

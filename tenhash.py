import sqlite3
from datetime import datetime
from flask import Flask
import constants


tenhash = Flask(constants.TENHASH)
tenhash.config.from_object('config.DevelopmentConfig')
tenhash.config.from_pyfile(constants.TENHASH_SETTINGS, silent=False)


@tenhash.route('/')
def homepage():
    """This is to render the homepage"""
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>  
    """.format(time=the_time)


@tenhash.route('/testing')
def testing():
    """ testing bed """
    return "testing time this"


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(tenhash.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


if constants.TENHASH == '__main__':
    tenhash.run(debug=True, use_reloader=True)

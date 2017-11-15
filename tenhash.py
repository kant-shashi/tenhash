from flask import Flask
from datetime import datetime
import constants

tenhash = Flask(constants.TENHASH)

@tenhash.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="https://graph.facebook.com/shashikant.0?fields=picture.width(720).height(720) ">
    """.format(time=the_time)


@tenhash.route('/testing')
def testing():
    return "testing time this"



if __name__ == '__main__':
    tenhash.run(debug=True, use_reloader=True)
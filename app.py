from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="https://graph.facebook.com/shashikant.0?fields=picture.width(720).height(720) ">
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
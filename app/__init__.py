from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_will_never_guess'

from app import routes


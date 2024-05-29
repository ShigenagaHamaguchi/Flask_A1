from flask import Flask


app = Flask(__name__)
app.config.from_object("calc_app.config")
from calc_app import views
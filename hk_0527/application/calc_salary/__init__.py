from flask import Flask

app = Flask(__name__)
app.config.from_object('calc_salary.config')
app.secret_key = 'super secret key'

import calc_salary.views
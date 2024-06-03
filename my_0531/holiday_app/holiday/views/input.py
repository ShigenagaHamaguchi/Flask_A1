from flask import request, redirect, url_for, render_template, flash, session
from holiday import app


@app.route('/', methods=['POST','GET'])
def input():
    return render_template('input.html')

from holiday import app,db
from holiday.models.holiday import Holiday
from flask import request,url_for,redirect,flash,render_template


@app.route("/list")
def show_list():
    holidays = Holiday.query.order_by(Holiday.date.desc()).all()
    return render_template("list.html",holidays=holidays)
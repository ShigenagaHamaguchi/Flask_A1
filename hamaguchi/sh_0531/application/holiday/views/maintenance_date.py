from holiday import app,db
from holiday.models.holiday import Holiday
from flask import request,url_for,redirect,flash,render_template

@app.route("/maintenance",methods=["GET"])
def show_maintenace(text):
    return render_template("maintenance_date.html",maintenance=text)
    
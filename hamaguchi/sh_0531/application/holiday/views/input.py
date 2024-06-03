from holiday import app,db
from holiday.models.holiday import Holiday
from datetime import datetime
from flask import request,url_for,redirect,flash,render_template
import re
from holiday.domain.year import Year
from holiday.domain.holitext import HoliText,HoliTextVaildation
@app.route("/",methods=["GET"])
def show_holiday():
    return render_template("input.html")

@app.route("/holiday",methods=["POST"])
def router_holiday():
    if not request.form["option"]:
        flash("正しいボタンを押してください")
        return redirect(url_for("show_holiday"))
    
    if request.form["option"] == "insert":
        if not request.form["date"] or not request.form["text"]:
            flash("正しい値を入力してください")
            return redirect(url_for("show_holiday"))
        
        date = request.form["date"]
        text = request.form["text"]
        print(date)
        
        
        if not Year(date.split("-")[0]).validation:
            flash("2000~3000年の範囲で入力できます")
            return redirect(url_for("show_holiday"))
        if not HoliText(text).validation():
            flash("祝日テキストにはひらがな、漢字、カタカナのみ入力できます")
            return redirect(url_for("show_holiday"))

        holiday = Holiday.query.get(date) 
        print(holiday)
        try:
            if holiday!=None:
                holiday =Holiday(date,text)
                db.session.merge(holiday)
                flash("編集完了しました")
            else:
                holiday =Holiday(date,text)
                db.session.add(holiday)
                flash("新規登録完了しました")
        except Exception as e:
            print(e)
            return redirect(url_for("show_holiday"))
        else:
            db.session.commit()
        text = "{}：（{}）を新規登録・編集しました".format(holiday.date,holiday.text)
        return render_template("maintenance_date.html",maintenance=text)
    else:
        if not request.form["date"]:
            flash("正しい値を入力してください")
            return redirect(url_for("show_holiday"))
        
        holiday = Holiday.query.get(request.form["date"])
        print(holiday)
        if holiday == None:
            flash("正しい値を入力してください")
            return redirect(url_for("show_holiday"))
        db.session.delete(holiday)
        db.session.commit()
        flash("削除できました")

        text = "{}：（{}）を消しました".format(holiday.date,holiday.text)
        return render_template("maintenance_date.html",maintenance=text)
@app.route("/holiday/new",methods=["GET"])
def insert(date,text):
    
    if not date or not text:
        flash("正しい値を入力してください")
        return redirect(url_for("show_holiday"))
    
    date = request.form["date"]
    text = request.form["text"]

    holiday = Holiday.query.get(date) 
    print(holiday)
    try:
        if holiday!=None:
            holiday =Holiday(date,text)
            db.session.merge(holiday)
            flash("編集完了しました")
        else:
            db.session.add(holiday)
            flash("新規登録完了しました")
    except Exception as e:
        print(e)
        return redirect(url_for("show_holiday"))
    else:
        db.session.commit()
    return redirect(url_for("show_maintenace",text=text))


@app.route("/holiday/delete",methods=["GET","POST"])
def delete(date):
    if not date:
        flash("正しい値を入力してください")
        return redirect(url_for("show_holiday"))
    
    holiday = Holiday.query.get(date)
    print(holiday)
    if holiday == None:
        flash("正しい値を入力してください")
        return redirect(url_for("show_holiday"))
    
    db.session.delete(holiday)
    db.session.commit()
    text = "{}：（{}）を消しました".format(holiday.date,holiday.text)
    
    return render_template("maintenance_date.html",maintenance=text)
    
    

    
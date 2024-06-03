from flask_blog import app,db
from flask import render_template,request,redirect,session,flash,url_for

from functools import wraps
from flask_blog.models.entries import Entry

def login_required(view):
    @wraps(view)
    def inner(*args,**keyword):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return view(*args,**keyword)
    return inner

@app.route("/")
@login_required
def show_entries():
    """
    試しのレンダリング
    """
    if not session.get("logged_in"):
        return redirect(url_for("show_login"))
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template("entries/index.html",entries=entries)
 
@app.route("/login",methods=["POST"])
def login():
    """
    ユーザネームとパスワードの比較
    """
    error = None
    if request.form["username"] != app.config["USERNAME"]:
        print("ユーザ名が異なります")
        flash("ユーザ名が異なります")
    elif request.form["password"] != app.config["PASSWORD"]:
        print("パスワードが異なります")
        flash("パスワードが異なります")
    else:
        session["logged_in"] = True
        flash("ログインしました")
        return redirect(url_for("show_entries"))
    return render_template("entries/login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in",None)    
    flash("ログアウトしました")
    return redirect(url_for("show_entries"))

@app.route("/login",methods=["GET"])
def show_login():
    """
    ログインフォームの作成
    """
    return render_template("entries/login.html")


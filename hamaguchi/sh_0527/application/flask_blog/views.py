from flask_blog import app
from flask import render_template,request,redirect,session,flash


@app.route("/")
def show_entries():
    """
    試しのレンダリング
    """
    if not session.get("logged_in"):
        redirect("login")
    return render_template("entries/index.html")

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
        return redirect("/")
    return render_template("entries/login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in",None)    
    flash("ログアウトしました")
    return redirect("/")

@app.route("/login",methods=["GET"])
def show_login():
    """
    ログインフォームの作成
    """
    return render_template("entries/login.html")
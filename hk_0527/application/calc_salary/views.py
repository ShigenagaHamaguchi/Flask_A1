from flask import request, redirect, url_for, render_template, flash, session, send_from_directory
from calc_salary import app

def calc_tax(salary):
    if salary > 1000000:
        tax_rate = 0.2
        tax = (salary - 1000000)*tax_rate + (1000000 * 0.1)
    else:
        tax_rate = 0.1
        tax = salary * tax_rate

    if tax - int(tax) >= 0.5:
        tax = int(tax) + 1
    else:
        tax = int(tax)

    return tax


@app.route('/')
def show_entries():
    salary = session.get("salary", None)
    return render_template('input.html', salary=salary)


@app.route('/output', methods=['GET','POST'])
def output():

    if request.form['salary'] == "":
        session['salary'] = request.form['salary']
        flash('給与が未入力です。入力してください。')
        return redirect(url_for('show_entries'))
    elif len(request.form['salary']) > 10:
        session['salary'] = request.form['salary']
        flash('給与には最大9,999,999,999まで入力可能です。')
        return redirect(url_for('show_entries'))
    
    salary = int(request.form['salary'])

    if salary < 0:
        session['salary'] = request.form['salary']
        flash('0円以上の数値を入力してください')
        return redirect(url_for('show_entries'))
    
    tax = calc_tax(salary)

    tedori = salary - tax

    return render_template('output.html', salary=salary, tedori=tedori, tax=tax)


@app.route("/music/money.mp3")
def play_music():
    return send_from_directory("music", "money.mp3")
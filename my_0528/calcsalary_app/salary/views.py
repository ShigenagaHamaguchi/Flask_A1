from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/', methods=['GET','POST'])
def input():
    init_val = session.get("input_data", None)
    return render_template('input.html', init_val=init_val)
        

@app.route('/output', methods=['GET','POST'])
def output():
    # バリデーションチェック
    if request.form['salary'] == '':
        flash('給与が未入力です。入力してください')
        session["input_data"] = request.form['salary']
        return redirect(url_for('input'))
    
    if int(request.form['salary']) >= 10000000000:
        flash('給与には最大9,999,999,999まで入力可能です。')
        session["input_data"] = request.form['salary']
        return redirect(url_for('input'))

    if int(request.form['salary']) < 0:
        flash('給与にはマイナスの値は入力できません。')
        session["input_data"] = request.form['salary']
        return redirect(url_for('input'))

    # 計算処理
    if request.method == 'POST':
        salary = int(request.form['salary'])
        # ベースとなる給料を定義
        base = 1000000

        # 給料から税額と支給額を算出
        if(salary <= base):
            tax = salary * 0.1
        else:
            tax = (salary - base)*0.2 + base*0.1
        tax = Decimal(str(tax)).quantize(Decimal("0"),rounding = ROUND_HALF_UP)
        payamount = salary - tax
        session.pop('input_data', None)
        return render_template('output.html', salary=salary, tax=tax, payamount=payamount)
    

    return render_template('output.html')
    
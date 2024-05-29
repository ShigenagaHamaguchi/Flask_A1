from calc_app import app
from flask import render_template,request,redirect,session,flash,url_for,jsonify
from calc_app.calc import calc_salary,calc_tax,BOUDER,TAX_RATE2,TAX_RATE1

@app.route("/",methods=["GET"])
def calc_app():
    """
    入力フォームを返す
    """
    return render_template("input.html")

@app.route("/tax_rate",methods=["GET"])
def tax_rate():
    """
    税金の内訳算出しテキストを返す
    """
    salary = request.args.get("salary")
    tax1,tax2 = calc_tax(salary=int(salary))
    text = """"""
    if tax2 != None:
        text = """<h3>あなたの給料は{0}円であり、</h3><h1>{1}円を超えています。</h1>
        <p>{1}円以下は所得税{2}%が適用され{3}円,</p><p>{1}円を超えたものは所得税{4}%が適用され{5}円引かれます。</p>""".format(salary,BOUDER,round(TAX_RATE1*100),round(tax1),round(TAX_RATE2*100),round(tax2))
    else:
        text="<p>あなたの給料は{0}円以下なので、所得税{1}%が適用され{2}円引かれます。</p>".format(BOUDER,round(TAX_RATE1*100),salary)
    return jsonify({"tax_rate":text}),200

@app.route("/output",methods=["GET","POST"])
def output():
    """
    入力された給料から税金を考慮し手取りを出力
    """
    if request.method == "POST":
        if not request.form["salary"] :
            flash("給与がありません")
            return redirect(url_for("calc_app"))
        try:
            salary = int(request.form["salary"])
        except Exception as e:
            flash("数字を入力してください")
            return redirect(url_for("calc_app"))
        if salary < 0:
            flash("0以上を入力してください")
        elif salary > 999999999999999999999:
            flash("数値は20桁未満で入力してください")
        else:
            return render_template("output.html",salary=salary,payamount=calc_salary(salary))
    return redirect(url_for("calc_app"))
from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday.models.mst_holiday import Holiday
from holiday import db
from datetime import date

@app.route('/maintenance_date', methods=['POST'])
def maintenance_date():
    dt = date(int(request.form["holiday"][0:4]), int(request.form["holiday"][5:7]), int(request.form["holiday"][8:10]))
    if request.form["button"] == "new_entry":    
        #DBデータの取得
        holiday = Holiday.query.filter_by(holi_date=dt).first()

        #新規登録        
        if holiday is None:      
            holiday_insup = Holiday(holi_date = dt, holi_text = request.form["holi_text"])  
            db.session.add(holiday_insup)            
            db.session.commit()
            msg = request.form["holiday"] + "（" + request.form["holi_text"] + "）が登録されました"
        #更新
        else:         
            holiday_insup = Holiday(holi_date = holiday.holi_date, holi_text = request.form["holi_text"])  
            db.session.merge(holiday_insup)
            db.session.commit()   
            msg = request.form["holiday"] + "は「" + request.form["holi_text"] + "」に更新されました"                     

        return render_template("result.html", msg = msg)

    elif request.form["button"] == "delete":
        holiday = Holiday.query.filter_by(holi_date=dt).first()
        #存在した場合のみ削除
        if holiday is None: 
            flash(request.form["holiday"] + "は、祝日マスタに登録されていません")
            return redirect(url_for("input")) 
        else:
            Holiday.query.filter_by(holi_date = dt).delete()
            db.session.commit()
            msg = str(holiday.holi_date) + "（" + holiday.holi_text + "）は、削除されました"              
            return render_template("result.html", msg = msg)                            

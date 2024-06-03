
from holiday import db
from datetime import datetime

class Holiday(db.Model):
    __tablename__ = 'holiday'
    date = db.Column(db.Date,primary_key=True)
    text = db.Column(db.Text)

    def __init__(self,date=None,text=None):
        self.date = date
        self.text = text
    
    def __repr__(self):
        return '<Holiday date:{} text:{}'.format(self.date,self.text)
from flask_script import Command
from holiday import db
from holiday.models.holiday import Holiday 


class InitDB(Command):
    """
    create database
    """

    def run(self):
        db.create_all()
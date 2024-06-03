DEBUG = True
USERNAME = "mem36"
PASSWORD = "pass"
SECRET_KEY = "secret key"

# URI = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(
#     **{
#         "user":"root",
#         "password":"mysql",
#         "host":"localhost",
#         "database":"ENSHU"
#     }
# )
import os
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}/{database}?charset={utf8}".format(**{
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "mysql"),
    "host": os.getenv("DB_HOST", "localhost"),
    "database":os.getenv("DB_DATABASE", "ENSHU"),
    "utf8":os.getenv("DB_CODE", "utf8")
})

SQLALCHEMY_TRACK_MODIFICATIONS = False

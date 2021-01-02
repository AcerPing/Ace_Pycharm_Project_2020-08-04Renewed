from flask import Flask
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import Config
# from app.forms import RegisterForm

app = Flask(__name__) #建立Application物件，__name__代表目前執行的模組，可以設定靜態檔案的路徑處理
app.config.from_object(Config)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'You must login to access this page'
login.login_message_category = 'info'

from app.routes import *


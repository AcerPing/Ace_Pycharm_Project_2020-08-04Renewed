from flask import Flask,render_template,flash
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.forms import RegisterForm
from app.models import User

app = Flask(__name__) #建立Application物件，__name__代表目前執行的模組，可以設定靜態檔案的路徑處理
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.config.from_object(Config)

@app.route('/') #函式的裝飾(Decorator):以函式為基礎，提供附加的功能
def index(): #用來回應網站首頁連線的函式；用來回應路徑 / 的處理函式
    return render_template("bootstrap.html")  # 回傳網站首頁內容

@app.route('/register',methods=["Get","Post"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)
        print(username,email,password)
        user = User(username=username,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, Registration Success',category='Success')
    return render_template("register.html", form=form)

@app.route('/html') #函式的裝飾(Decorator):以函式為基礎，提供附加的功能
def html():
    title = "Python Website Tutorial"
    data =  ["person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch", "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]
    return render_template("bootstrap.html",title = title,data = data)

#啟動網站伺服器，可透過port參數指定埠號
if __name__=="__main__": #如果以主程式執行
    app.run(debug=True) #立刻啟動伺服器
from flask import render_template,flash,redirect,url_for,request
from flask_login import login_user, login_required, current_user, logout_user
from app import app,bcrypt,db
from app.forms import RegisterForm,LoginForm
from app.models import User

@app.route('/') #函式的裝飾(Decorator):以函式為基礎，提供附加的功能
@login_required
def index(): #用來回應網站首頁連線的函式；用來回應路徑 / 的處理函式
    return render_template("bootstrap.html")  # 回傳網站首頁內容

@app.route('/register',methods=["Get","Post"])
def register():
    if current_user.is_authenticated:
        return  redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)
        print(username,email,password)
        user = User(username=username,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, Registration Success',category='success')
        return redirect(url_for('index'))
    return render_template("register.html", form=form)


@app.route('/html') #函式的裝飾(Decorator):以函式為基礎，提供附加的功能
def html():
    title = "Python Website Tutorial"
    data =  ["person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch", "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]
    return render_template("index.html",title = title,data = data)

@app.route('/login',methods=["Get","Post"])
def login():
    if current_user.is_authenticated:
        return  redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        #Check if password is matched
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            #User exists and password matched
            login_user(user,remember=remember)
            flash("Login Success",category='info')
            if request.args.get('next'):
                next_page=request.args.get('next')
                # print("next_page",next_page)
                return redirect(next_page)
            return redirect(url_for('index'))
        flash("User not exists or Password not matched",category="danger")
    return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
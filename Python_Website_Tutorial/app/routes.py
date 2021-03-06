from flask import render_template,flash,redirect,url_for,request
from flask_login import login_user, login_required, current_user, logout_user
import os
from werkzeug.utils import secure_filename

from app import app,bcrypt,db
from app.forms import RegisterForm, LoginForm, PasswordResetRequestForm, ResetPasswordForm, PostTextForm
from app.forms import *
from app.email import send_reset_password_mail
from app.models import User, Post

# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=["Get","Post"]) #函式的裝飾(Decorator):以函式為基礎，提供附加的功能
@login_required
def index(): #用來回應網站首頁連線的函式；用來回應路徑 / 的處理函式
    form = PostTextForm()
    if form.validate_on_submit():
        body = form.text.data
        post = Post(body=body)
        current_user.posts.append(post)
        db.session.commit()
        flash('You have posted a new message.', category='success')

    n_followers = len(current_user.followers)
    n_followed = len(current_user.followed)

    # posts = Post.query.order_by(Post.timestamp.desc()).all()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page, 5, False)

    return render_template("bootstrap.html", form=form, posts=posts,
                           n_followers=n_followers, n_followed=n_followed)  # 回傳網站首頁內容

@app.route('/user_page/<username>')
@login_required
def user_page(username):
    user = User.query.filter_by(username=username).first()
    if user:
        page = request.args.get('page', 1, type=int)
        posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestamp.desc()).paginate(page, 5, False)
        return render_template('user_page.html', user=user, posts=posts)
    else:
        return '404'

@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user:
        current_user.follow(user)
        db.session.commit()
        page = request.args.get('page', 1, type=int)
        posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestamp.desc()).paginate(page, 5, False)
        return render_template('user_page.html', user=user, posts=posts)
    else:
        return '404'

@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user:
        current_user.unfollow(user)
        db.session.commit()
        page = request.args.get('page', 1, type=int)
        posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestamp.desc()).paginate(page, 5, False)
        return render_template('user_page.html', user=user, posts=posts)
    else:
        return '404'


@app.route('/edit_profile', methods=["Get","Post"])
def edit_profile():
    form = UploadPhotoForm()
    if form.validate_on_submit():
        f = form.photo.data
        if f.filename == '': #若文件名是空值 → 代表未選擇文件
            flash('No selected file', category='danger')
            return render_template('edit_profile.html', form=form)
        if f and allowed_file(f.filename): #若為圖片文件的格式
            #文件存儲操作
            filename = secure_filename(f.filename) #基於數據安全，保障程序安全，避免中病毒
            f.save(os.path.join('app', 'static', 'asset', filename))
            #數據庫存儲位置
            current_user.avatar_img = '/static/asset/' + filename
            db.session.commit()
            return redirect(url_for('user_page', username=current_user.username))
    return render_template('edit_profile.html', form=form)


@app.route('/register',methods=["Get","Post"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
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
        return redirect(url_for('login'))
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
@login_required
def logout():
    logout_user()
    flash('You have logged out.', category='info')
    return redirect(url_for('login'))

@app.route('/Send_Password_Reset_Request',methods=["Get","Post"])
def Send_Password_Reset_Request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = PasswordResetRequestForm(request.form)
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        token = user.generate_reset_password_token()
        if user:
            send_reset_password_mail(user, token)
        flash('Password Reset Request E-mail has been sent out, Please Check Your Mail Box.', category='info')
        return redirect(url_for('login'))
    return render_template('Send_Password_Reset_Request.html', form=form)

@app.route('/reset_password/<token>', methods=["Get","Post"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordForm(request.form)
    if form.validate_on_submit():
        user = User.verify_reset_password_token(token)
        if user:
            user.password = bcrypt.generate_password_hash(form.password.data)
            db.session.commit()
            flash('Your password has been reset. You may login with new password now.', category='info')
        else:
            flash('The user is not existed.', category='info')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)

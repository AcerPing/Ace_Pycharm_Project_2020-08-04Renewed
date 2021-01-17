from threading import Thread
from flask import current_app,render_template
from flask_mail import Message
from app import mail, app

def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)

def send_reset_password_mail(user, token):
    # token = user.get_reset_password_token()
    msg = Message(subject="[Flask APP]Reset Your Password",
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[user.email],
                  body=render_template('reset_password.txt',user=user, token=token),
                  html=render_template('reset_password_mail.html', user=user,token=token))
    # mail.send(msg)
    Thread(target=send_async_mail, args=(app, msg, )).start()


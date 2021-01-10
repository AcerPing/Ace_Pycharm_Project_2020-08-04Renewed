import os
from Mail_Secret import MAIL_USERNAME, MAIL_PASSWORD

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    #Secret Key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-SECRET-KEY'

    # RECAPTCHA PUBLIC KEY
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') or 'A-VERY-LONG-SECRET-KEY'
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY') or 'A-VERY-LONG-SECRET-KEY'

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Gamil Config
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('GMAIL_USERNAME') or MAIL_USERNAME
    # MAIL_USERNAME = os.environ.get('GMAIL_USERNAME') or 'MAIL_USERNAME'
    MAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD') or MAIL_PASSWORD
    # MAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD') or 'MAIL_PASSWORD'
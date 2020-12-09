import os

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
import os

class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.abspath(os.path.join(os.path.dirname(__file__), "instance/superheroes.db"))}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'yusufmim'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
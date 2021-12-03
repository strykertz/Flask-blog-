import os


class Config:
    SECRET_KEY = 'fce6db1c54a10f05eb45cd727455f702'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('DB_USER')
    MAIL_PASSWORD = os.environ.get('DB_PASSWORD')
from exts import db
from datetime import datetime



class UserModel(db.Model):
    '''
    用户表
    '''
    __tablename__ = 'user'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True)
    gender = db.Column(db.String(255), unique=True, nullable=False)




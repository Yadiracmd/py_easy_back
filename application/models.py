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
    email = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    balance = db.Column(db.Integer, nullable=False,default=0)

class ConsumptionModel(db.Model):
    __tablename__ = 'consumption'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=True)
    funcName = db.Column(db.String(255),comment='调用函数名')
    score = db.Column(db.Integer, nullable=False,comment='消费点数')
    create_time = db.Column(db.DateTime, default=datetime.now,comment='调用时间')

    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False, comment='用户编号')
    userId = db.relationship(UserModel, backref='questions')



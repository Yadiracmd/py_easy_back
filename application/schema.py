
# 用于格式化输出库
from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    email = fields.Str()
    gender = fields.Str()
    balance = fields.Int()




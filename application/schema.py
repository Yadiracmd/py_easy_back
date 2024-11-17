
# 用于格式化输出库
from marshmallow import Schema, fields

class NotifySchema(Schema):
    id = fields.Int()
    title = fields.Str()
    content = fields.Str()
    create_time = fields.Str()

class PartySchema(Schema):
    id = fields.Int()
    name = fields.Str()
    gender = fields.Str()
    birthday = fields.Str()
    join_date = fields.Str()
    education = fields.Str()
    major = fields.Str()
    contact_number = fields.Str()
    email = fields.Str()
    address = fields.Str()
    username = fields.Str()
    password = fields.Str()
    score = fields.Int()

class AdminSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()

class ActivitySchema(Schema):
    id = fields.Int()
    name = fields.Str()
    organiser = fields.Str()
    create_time = fields.Str()
    address = fields.Str()
    content = fields.Str()

class CultivateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    organiser = fields.Str()
    time = fields.Str()
    address = fields.Str()
    content = fields.Str()


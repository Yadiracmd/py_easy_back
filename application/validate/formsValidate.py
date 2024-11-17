import wtforms
from wtforms.validators import Length, EqualTo



# 验证登录表单
class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=6, max=20, message='用户名格式错误！')])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message='密码格式错误！')])

# 验证注册表单
class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=6, max=20, message='用户名格式错误！')])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message='密码格式错误！')])
    password_confirm = wtforms.StringField(validators=[EqualTo("password", message='两次密码不一致！')])






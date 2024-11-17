import json
from application.models import UserModel
from application.utils.JWTManager import JWTManager
from application.utils.ResponseEntity import Response
from application.utils.security import check_password_hash, generate_password_hash
from application.validate.formsValidate import LoginForm, RegisterForm
from exts import db
from flask import Blueprint, request


# /auth
bp = Blueprint("auth", __name__, url_prefix='/auth')



# 登录函数
@bp.route('/login', methods=['POST'])
def auth_login():
    decrypted_data = getattr(request, 'decrypted_data', None)
    if decrypted_data:
        data = json.loads(decrypted_data)
        form = LoginForm(data=data)

        if form.validate():
            username = form.username.data
            password = form.password.data
            user = UserModel.query.filter_by(username=username).first()
            if not user:
                return Response.fail("用户名不存在")
            if check_password_hash(user.password, password):
                token_ = JWTManager.generate_token(user.id,user.username)
                return Response.success('登录成功',{'Token': token_})
            else:
                return Response.fail("密码错误")
        else:
            return Response.fail(form.errors)
    else:
        return Response.fail("数据获取失败")




# 注册函数
@bp.route("/register", methods=['POST'])
def auth_register():
    '''
    验证用户提交的邮箱和验证码功能
    :return:
    '''
    decrypted_data = getattr(request, 'decrypted_data', None)
    if decrypted_data:
        data = json.loads(decrypted_data)
        form = RegisterForm(data=data)
        if form.validate():
            username = form.username.data
            password = form.password.data
            print( username, password)
            user = UserModel(username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return Response.success('注册成功')
        else:
            return Response.fail(form.errors)
    else:
        return Response.fail("数据获取失败")

# 退出登录函数
@bp.route("/logout", methods=['POST'])
def logout():
    return Response.success("退出登录成功!")
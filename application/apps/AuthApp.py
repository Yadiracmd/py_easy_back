from application.models import UserModel
from application.schema import UserSchema
from application.utils.JWTManager import JWTManager
from application.utils.ResponseEntity import Response
from application.utils.decorators import ResponseBody
from application.utils.security import check_password_hash, generate_password_hash
from application.validate.formsValidate import LoginForm, RegisterForm
from exts import db
from flask import Blueprint, request,g


# /auth
bp = Blueprint("auth", __name__, url_prefix='/auth')



# 登录函数
@bp.route('/login', methods=['POST'])
@ResponseBody
def auth_login(data):

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





# 注册函数
@bp.route("/register", methods=['POST'])
@ResponseBody
def auth_register(data):
    '''
    注册功能
    :return:
    '''
    form = RegisterForm(data=data)
    if form.validate():
        username = form.username.data
        password = form.password.data
        print( username, password)
        user = UserModel(username=username, password=generate_password_hash(password),gender = '男')
        db.session.add(user)
        db.session.commit()
        return Response.success('注册成功')
    else:
        return Response.fail(form.errors)

# 退出登录函数
@bp.route("/logout", methods=['POST'])
def logout():
    return Response.success("退出登录成功!")

# 获取余额
@bp.route("/balance")
def get_balance():
    user_id = getattr(g, "user_id", None)
    user =UserModel.query.with_entities(UserModel.username,UserModel.balance).filter_by(id=user_id).first()
    return Response.success("获取成功",data=UserSchema(many=False).dump(user))


# 获取消费记录表
@bp.route("/consumption_list")
def get_consumption_list():
    pass
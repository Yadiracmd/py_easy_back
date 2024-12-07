'''
针对整个app项目全局路由拦截规则定义
'''
from flask import request,g

from application.models import UserModel
from application.utils.JWTManager import JWTManager
from application.utils.ResponseEntity import Response



def register_filter(app):
    @app.before_request
    def my_before_request():

        # x_t = request.headers.get('x-t')
        # if not x_t:
        #     return Response.fail('缺少必要参数', code=403)
        #
        # # 如果请求方式是 POST 则解析并解密数据
        # if request.method == "POST" and request.is_json:
        #     data = request.get_json()
        #     data_data = data.get('data', None)
        #     if data_data:
        #         try:
        #             decrypted_data = AESDecrypt(data_data, x_t + '900', '0102030405060708')
        #             # 将解密后的数据存入 request 对象
        #             request.decrypted_data = decrypted_data
        #         except Exception as e:
        #             return Response.fail('data参数错误', code=400)
        #     else:
        #         return Response.fail("请求数据格式不正确", code=401)

        if request.endpoint not in ['auth.auth_login', 'auth.get_email_captcha', 'auth.auth_register']:
            token = request.args.get('token')
            print(token)
            # 如果没有 Token，返回鉴权失败
            if not token:
                return Response.fail("鉴权失败", code=403)

            # 解码 Token 获取 payload
            payload = JWTManager.decode_token(token)

            # 如果 token 无效或过期，返回错误
            if not payload:
                return Response.fail("无效或过期的 token", code=403)

            # 使用 payload 中的 user_id 获取用户信息

            user = UserModel.query.get(payload['user_id'])
            # 如果用户不存在，返回失败信息
            if not user:
                return Response.fail("用户不存在", code=404)
            setattr(g, "user", user)
            setattr(g, "user_id", payload['user_id'])

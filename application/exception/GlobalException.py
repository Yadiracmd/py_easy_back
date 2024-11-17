from application.utils.ResponseEntity import Response
from pymysql.err import IntegrityError


def register_error_handlers(app):
    """
    注册全局异常处理器
    """

    @app.errorhandler(Exception)
    def handle_all_exceptions(e):
        # 捕获所有未处理的异常
        error_message = str(e)
        if "user.username" in error_message:
            return Response.fail("用户名已存在！")
        return Response.fail("服务器内部错误: " + str(e))




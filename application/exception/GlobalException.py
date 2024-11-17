from application.utils.ResponseEntity import Response



def register_error_handlers(app):
    """
    注册全局异常处理器
    """

    @app.errorhandler(Exception)
    def handle_all_exceptions(e):
        # 捕获所有未处理的异常
        return Response.fail("服务器内部错误: " + str(e))

    # @app.errorhandler(SQLAlchemyError)
    def handle_sqlalchemy_error(e):
        # 捕获 SQLAlchemy 异常
        return Response.fail("用户名重复")

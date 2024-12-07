from flask import Flask

from application.exception.GlobalException import register_error_handlers
from application.filter.requestFilter import register_filter
from exts import db
from flask_migrate import Migrate
from application import blueprints
from application import settings


app = Flask(__name__)
# 绑定配置文件
app.config.from_object(settings)

# 初始化数据库连接
db.init_app(app)

# 注册连接
migrate = Migrate(app, db)


# 统一注册所有蓝图
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# 注册异常处理器
register_filter(app)

# 注册异常处理器
register_error_handlers(app)





if __name__ == '__main__':
    app.run(port=9999,host='0.0.0.0',threaded=True)

from .apps.AuthApp import bp as auth_bp
from .apps.YiDunApp import bp as yi_bp
from .apps.JdApp import bp as jd_bp

# 将蓝图存储在一个列表中
blueprints = [auth_bp,yi_bp,jd_bp]

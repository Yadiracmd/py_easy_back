# mysql主机名
HOSTNAME = '192.168.181.128'
# mysql端口
PORT = 3306
# 用户名
USERNAME = 'root'
# 密码
PASSWORD = '123456'
# 数据库名
DATABASE = "py_easy"


# 选择mysql还是 sqlite
DBTYPE = "sqlite"
# 配置数据库URI
# mysql
if DBTYPE == "mysql":
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DATABASE}?charset=utf8'
else:
    # sqlite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///easy.db'


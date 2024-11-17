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

# 配置数据库URI
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DATABASE}?charset=utf8'


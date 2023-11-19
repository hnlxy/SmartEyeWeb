class BaseConfig(object):
    # MySQL数据库服务器的主机名
    HOSTNAME = "127.0.0.1"
    # MySQL数据库服务器的端口号，默认为 3306
    PORT = 3306
    # 用于连接MySQL数据库的用户名
    USERNAME = "root"
    # 用于连接MySQL数据库的密码
    PASSWORD = "lxy000000"
    # 要连接的数据库名
    DATABASE = "smart_eye"
    # 构造MySQL数据库连接 URL
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"
    # 是否追踪对象的修改并发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 是否启用调试模式
    debug = True
    # 其他通用配置项


class DevelopmentConfig(BaseConfig):
    # 开发环境特有的配置项
    debug = True
    # Flask 应用的密钥，用于会话、cookie 加密等
    secret_key = "SmartEye"
    # 是否打印执行的 SQL 语句
    SQLALCHEMY_ECHO = True
    pass


class TestConfig(BaseConfig):
    # 测试环境特有的配置项
    TESTING = True
    # 测试环境使用的数据库连接 URL
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://test_user:test_password@localhost/test_database"
    pass


class ProductionConfig(BaseConfig):
    # 生产环境特有的配置项
    DEBUG = False
    # 设置 SQLAlchemy 的数据库连接池回收时间
    SQLALCHEMY_POOL_RECYCLE = 280
    # 生产环境的其他配置，可能包括日志、安全设置、HTTPS 支持等

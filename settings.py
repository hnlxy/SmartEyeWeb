# TODO 配置

class BaseConfig(object):
    # TODO 基础配置
    # MySQL所在主机名
    HOSTNAME = "127.0.0.1"
    # MySQL监听的端口号，默认3306
    PORT = 3306
    # 连接MySQL的用户名
    USERNAME = "root"
    # 连接MySQL的密码
    PASSWORD = "root"
    # MySQL上创建的数据库名称
    DATABASE = "smart_eye"
    # URL配置
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
    # 是否追踪对象的修改并发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    debug = True
    # 密钥设置
    serect_key = "SmartEye"
    pass


class DevelopmentConfig(BaseConfig):
    # TODO 开发环境配置
    debug = True
    serect_key = "SmartEye"
    SQLALCHEMY_ECHO = True  # 显示详细的 SQL 查询日志
    pass


class TestConfig(BaseConfig):
    # TODO 测试环境配置
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://test_user:test_password@localhost/test_database"
    pass


class ProductionConfig(BaseConfig):
    # TODO 生产环境配置
    DEBUG = False
    SQLALCHEMY_POOL_RECYCLE = 280  # 设置 SQLAlchemy 的连接回收时间
    # 可以考虑添加更多的安全措施，比如 HTTPS 配置等

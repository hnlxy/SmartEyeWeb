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
    pass


class DevelopmentConfig(BaseConfig):
    # TODO 开发环境配置
    pass


class TestConfig(BaseConfig):
    # TODO 测试环境配置
    pass


class ProductionConfig(BaseConfig):
    # TODO 生产环境配置
    pass

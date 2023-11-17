# TODO ����

class BaseConfig(object):
    # TODO ��������
    # MySQL����������
    HOSTNAME = "127.0.0.1"
    # MySQL�����Ķ˿ںţ�Ĭ��3306
    PORT = 3306
    # ����MySQL���û���
    USERNAME = "root"
    # ����MySQL������
    PASSWORD = "lxy000000"
    # MySQL�ϴ��������ݿ�����
    DATABASE = "smart_eye"
    # URL����
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"
    # �Ƿ�׷�ٶ�����޸Ĳ������ź�
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    debug = True
    # ��Կ����
    serect_key = "SmartEye"


class DevelopmentConfig(BaseConfig):
    # TODO ������������
    debug = True
    serect_key = "SmartEye"
    SQLALCHEMY_ECHO = True  # ��ʾ��ϸ�� SQL ��ѯ��־
    pass


class TestConfig(BaseConfig):
    # TODO ���Ի�������
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://test_user:test_password@localhost/test_database"
    pass


class ProductionConfig(BaseConfig):
    # TODO ������������
    DEBUG = False
    SQLALCHEMY_POOL_RECYCLE = 280  # ���� SQLAlchemy �����ӻ���ʱ��
    # ���Կ�����Ӹ���İ�ȫ��ʩ������ HTTPS ���õ�

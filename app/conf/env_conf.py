# coding=utf-8
import os


class Config:
    """
    基本配置
    """
    # flask
    SECRET_KEY = "$%^&*a!@#29$%^#2#$%^&*(b#!!@%c!@#4$%^&d"

    # mysql
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = '3306'
    MYSQL_DB_NAME = 'auth'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456abc'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 静态资源目录
    STATIC_PATH = 'static'
    ROOT_DIR = '/web/app'

    def __init__(self):
        for key in os.environ:
            setattr(self, key, os.environ.get(key))

        self.SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:{}/{}' \
            .format(self.MYSQL_USER, self.MYSQL_PASSWORD, self.MYSQL_HOST, self.MYSQL_PORT, self.MYSQL_DB_NAME)


ENV_CONF = Config()

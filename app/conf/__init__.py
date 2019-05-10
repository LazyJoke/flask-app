from app.conf.default import *


class Config:
    """
    基本配置 (默认配置请请修改 app.conf.default)
    """
    # flask
    SECRET_KEY = "$%^&*a!@#29$%^#2#$%^&*(b#!!@%c!@#4$%^&d"
    # db
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:{}/{}' \
        .format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB_NAME)

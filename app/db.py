import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import init, migrate, upgrade


db = SQLAlchemy()


def update_models():
    """
    初始化数据表，如果有数据表变动，则更新
    :return:
    """
    if not os.path.exists('migrations'):
        init()
    migrate()
    upgrade()

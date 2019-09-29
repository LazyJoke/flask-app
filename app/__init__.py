# coding=utf-8
import connexion
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from swagger_ui_bundle import swagger_ui_3_path

from app.core.logger import logger
from app.db import db, update_models
from app.conf import Config
from app.models import *


def create_app():
    options = {'swagger_path': swagger_ui_3_path}
    _app = connexion.App(__name__, options=options)
    _app.add_api('openapi.yaml')
    application = _app.app

    # 注册 config 配置
    application.config.from_object(Config)

    # 数据迁移
    Migrate(application, db)

    # 添加 flask_script
    manager = Manager(application)
    manager.add_command('db', MigrateCommand)

    # 初始化数据库
    db.init_app(application)

    application.app_context().push()

    # 初始化表或更新表
    update_models()

    return manager, db

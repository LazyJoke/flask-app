from flasgger import Swagger
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app.core.validation_error import validation_error_inform_error
from app.db import db
from app.conf import Config
from app.blueprint import register_blueprint
from app.resources import add_resources


def create_app():
    app = Flask(__name__)

    # 注册 config 配置
    app.config.from_object(Config)

    # 数据迁移
    migrate = Migrate(app, db)

    # 添加 flask_script
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    # 初始化数据库
    db.init_app(app)

    # 注册蓝图
    register_blueprint(app)

    # 添加 Swagger
    swag = Swagger(app, validation_error_handler=validation_error_inform_error)

    app.app_context().push()

    return manager, db

from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app.db import db
from app.blueprint import register_blueprint
from app.resources import add_resources
from app.swagger import init_swagger


def create_app():
    app = Flask(__name__)
    # TODO config 配置
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/demo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # 添加 Swagger
    init_swagger(app)
    # 数据迁移
    migrate = Migrate(app, db)
    # 添加 flask_script
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    # 初始化数据库
    db.init_app(app)
    # 注册蓝图
    register_blueprint(app)
    app.app_context().push()
    return manager, db

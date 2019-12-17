# coding=utf-8
import argparse
import os

import connexion
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from swagger_ui_bundle import swagger_ui_3_path

from app.core.logger import logger
from app.core.db import db, update_models
from app.conf.env_conf import ENV_CONF
from app.core.openapi import yaml_load
from app.models import *


def create_app():
    # 配置 swagger_ui
    options = {'swagger_path': swagger_ui_3_path}
    # 初始化 APP
    _app = connexion.App(
        __name__,
        options=options,
    )
    # 动态读取 api 目录下所有的 *.yaml
    api_json = yaml_load(os.path.join(ENV_CONF.ROOT_DIR, '**/*.yaml'))
    # 注册 API
    _app.add_api(
        api_json,
        strict_validation=True,  # 请求参数校验
        validate_responses=True  # 接口返回数据格式校验
    )
    application = _app.app

    # 注册 config 配置
    application.config.from_object(ENV_CONF)

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

    return _app, manager, db


def get_start_mode():
    # 默认值
    port = 10001
    host = '0.0.0.0'
    is_prod = False
    # 创建解析对象
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-M",
        "--mode",
        default='dev',
        nargs='?',
        help="开发模式，可选值：'dev'(默认)、'prod'",
        dest="mode")  # 启动模式
    parser.add_argument(
        "-H", "--host", default=host, nargs='?', help="host",
        dest="host")  # 启动模式
    parser.add_argument(
        "-P", "--port", default=port, nargs='?', help="服务端口",
        dest="port")  # 启动模式
    # 解析命令行
    args = parser.parse_args()
    if args.mode == 'prod':
        is_prod = True
    return is_prod, args.host, int(args.port)


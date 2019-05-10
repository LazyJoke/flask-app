from flasgger import Swagger
from flask import Blueprint
from flask_restful import Api

from app.resources import add_resources


def register_blueprint(app):
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)

    # 注册资源
    add_resources(api)

    # 注册蓝图
    app.register_blueprint(api_bp)

# coding=utf-8
from app.common.utils import get_environment

# flask
SECRET_KEY = "$%^&*a!@#29$%^#2#$%^&*(b#!!@%c!@#4$%^&d"
# mysql
MYSQL_HOST = get_environment("MYSQL_HOST", 'localhost')
MYSQL_PORT = get_environment("MYSQL_PORT", '3306')
MYSQL_DB_NAME = get_environment("MYSQL_DB_NAME", 'auth')
MYSQL_USER = get_environment("MYSQL_USER", 'root')
MYSQL_PASSWORD = get_environment("MYSQL_PASSWORD", '123456abc')
# 静态资源目录
STATIC_PATH = get_environment("STATIC_PATH", 'static')

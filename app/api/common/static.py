# coding=utf-8
from flask import send_from_directory

from app.conf.env_conf import ENV_CONF


def get_static(filename):

    return send_from_directory(ENV_CONF.STATIC_PATH, filename)

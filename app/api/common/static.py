from flask import send_from_directory

from app.conf import STATIC_PATH


def get_static(filename):

    return send_from_directory(STATIC_PATH, filename)

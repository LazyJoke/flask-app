from flask import send_from_directory

from app.core.resource import BaseResource


class Static(BaseResource):

    def get(self, filename):
        return send_from_directory(UPLOAD_PATH, filename)

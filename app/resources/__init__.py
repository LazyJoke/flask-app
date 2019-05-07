from app.resources.demo import Demo
from app.resources.static import Static


def add_resources(api):
    """
    添加资源
    :param api:
    :return:
    """
    api.add_resource(Static, '/upload/<filename>')
    api.add_resource(Demo, '/demo', '/demo/<int:id>')

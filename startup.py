# coding=utf-8
from app import create_app, get_start_mode

app, manager, db = create_app()

if __name__ == '__main__':
    # 获取启动参数
    is_prod, host, port = get_start_mode()
    # 生产模式启用 gevent, 开发模式启用 debug 模式
    if is_prod:
        server = 'gevent'
        debug = False
    else:
        server = None
        debug = True
    # 启动 app
    app.run(server=server, debug=debug, host=host, port=port)

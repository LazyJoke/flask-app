import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('flask.logger')
# 设置日志基础级别
logger.setLevel(logging.DEBUG)
# 日志格式
formatter = '%(asctime)s: %(levelname)s %(filename)s-%(module)s-%(funcName)s-%(lineno)d %(message)s'
log_formatter = logging.Formatter(formatter)
# info日志处理器
info_handler = TimedRotatingFileHandler(filename='logs/info.log', when='D', interval=1, backupCount=7, encoding='utf-8')
info_handler.setFormatter(log_formatter)
# 错误日志处理器
err_handler = TimedRotatingFileHandler(filename='logs/error.log', when='D', interval=1, backupCount=7, encoding='utf-8')
err_handler.setFormatter(log_formatter)
# 添加日志处理器
logger.addHandler(info_handler)
logger.addHandler(err_handler)

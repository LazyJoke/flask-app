from app.common.utils import get_environment

MYSQL_HOST = get_environment("MYSQL_HOST", 'localhost')
MYSQL_PORT = get_environment("MYSQL_PORT", '3306')
MYSQL_DB_NAME = get_environment("MYSQL_DB_NAME", 'demo')
MYSQL_USER = get_environment("MYSQL_USER", 'root')
MYSQL_PASSWORD = get_environment("MYSQL_PASSWORD", 'root')

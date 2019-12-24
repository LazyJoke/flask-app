# coding=utf-8
import six
import time
from jose import JWTError, jwt
from werkzeug.exceptions import Unauthorized

from app.conf.env_conf import ENV_CONF

JWT_ISSUER = 'com.email.name'
JWT_SECRET = ENV_CONF.SECRET_KEY
JWT_LIFETIME_SECONDS = 60 * 60 * 6
JWT_ALGORITHM = 'HS256'


def generate_token(user_id):
    timestamp = current_timestamp()
    payload = {
        "iss": JWT_ISSUER,
        "iat": int(timestamp),
        "exp": int(timestamp + JWT_LIFETIME_SECONDS),
        "sub": str(user_id),
    }

    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        six.raise_from(Unauthorized, e)


def current_timestamp() -> int:
    return int(time.time())

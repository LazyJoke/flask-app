import time
import six
from werkzeug.exceptions import Unauthorized

from jose import JWTError, jwt

from app.conf import SECRET_KEY

JWT_ISSUER = 'com.email.name'
JWT_SECRET = SECRET_KEY
JWT_LIFETIME_SECONDS = 60 * 60 * 6
JWT_ALGORITHM = 'HS256'


def generate_token(user_id):
    timestamp = _current_timestamp()
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


def get_secret(user, token_info) -> str:
    return '''
    You are user_id {user} and the secret is 'abc'.
    Decoded token claims: {token_info}.
    '''.format(user=user, token_info=token_info)


def _current_timestamp() -> int:
    return int(time.time())

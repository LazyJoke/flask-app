from app import session
from app.core.jwt import generate_token
from app.models.user import UserModel


def login(body):
    user = session.query(UserModel).filter(UserModel.username == body.get('username')).first()
    if not user:
        return "用户名或密码错误", 400
    # 返回 Token
    return generate_token(user.id), 200

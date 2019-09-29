# coding=utf-8
from hashlib import sha1

SALT_KEY = 'flaskCliSalt@'


def secret(password):
    """
`   密码加密函数
    :param password:
    :return:
    """
    # 加盐
    mix = []
    for_obj = SALT_KEY if len(SALT_KEY) > len(password) else password
    add_obj = password if len(SALT_KEY) > len(password) else SALT_KEY
    for i, s in enumerate(for_obj):
        mix.append(s)
        if i < len(add_obj):
            mix.append(add_obj[i])
    salt_password = "".join(mix).encode()
    # 加密
    sha1_obj = sha1()
    sha1_obj.update(salt_password)
    return sha1_obj.hexdigest()

from app import UserModel
from app.core.test import session, BaseTest


class AuthTest(BaseTest):

    def test_login(self):
        # 新增用户
        user = UserModel(username='张三', password='123455')
        session.add(user)
        session.commit()
        # 查询用户
        user_zs = session.query(UserModel).filter(UserModel.username == '张三').first()
        # 查询结果不为空
        self.assertIsNotNone(user_zs, msg="未查询到用户 '张三'")
        # 查询用户的名称为 '张三'
        self.assertEqual(user_zs.username, '张三')
        # 测试登录
        response = self.client.post("/login", json={"username": '张三', "password": '123456'})
        # 返回不为空
        self.assertIsNotNone(response)
        # 状态码等于 200
        self.assertEqual(response.status_code, 200)

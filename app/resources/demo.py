from flask_restful import fields, marshal_with

from app.core.resource import BaseResource
from app.common.parser import params_parser

# 定义返回结果
from app.models.demo import DemoModel

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'user_priority': fields.Integer,
    'custom_greeting': fields.FormattedString('Hey there {username}!'),
    'date_created': fields.DateTime,
    'date_updated': fields.DateTime,
    'links': fields.Nested({
        'friends': fields.Url('user_friends'),
        'posts': fields.Url('user_posts'),
    }),
}


class Demo(BaseResource):

    @marshal_with(user_fields)
    def post(self):
        args = params_parser([dict(name='username', dest='username',
                                   location='form', required=True,
                                   help='The user\'s username', )])
        user = DemoModel(args.username, args.email)
        return user

    def get(self):
        return dict(data='')

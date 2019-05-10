from flasgger import swag_from
from flask_restful import marshal_with

from app.core.resource import BaseResource

from app.models.demo import DemoModel
from app.resources.demo.doc import Doc
from app.resources.demo.fields import user_fields


# TODO 参数解析
class Demo(BaseResource):
    @marshal_with(user_fields)
    @swag_from(Doc.GET, methods=['GET'], validation=True)
    def get(self):
        args = self.params_parser([dict(name='username', dest='username',
                                   location='form', required=True,
                                   help='参数缺失')])
        user = DemoModel(args.username, args.email)
        return 'hello world'

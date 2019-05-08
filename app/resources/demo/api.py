from flasgger import swag_from
from flask_restful import marshal_with

from app.core.resource import BaseResource
from app.common.parser import params_parser

from app.models.demo import DemoModel
from app.resources.demo.doc import Doc
from app.resources.demo.fields import user_fields


class Demo(BaseResource):
    @marshal_with(user_fields)
    @swag_from(Doc.GET, methods=['GET'], validation=True, validation_function=None)
    def get(self):
        args = params_parser([dict(name='username', dest='username',
                                   location='form', required=True,
                                   help='The user\'s username', )])
        user = DemoModel(args.username, args.email)
        return user
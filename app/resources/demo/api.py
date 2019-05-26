import json

import requests
from flasgger import swag_from
from flask import request, jsonify
from flask_restful import marshal_with

from app.core.resource import BaseResource

from app.models.demo import DemoModel
from app.resources.demo.doc import Doc
from app.resources.demo.fields import user_fields


# TODO 参数解析
class Demo(BaseResource):
    # @marshal_with(user_fields)
    # @swag_from(Doc.GET, validation=True)
    def post(self):
        a=request.form.get("comments")
        # args = self.params_parser([dict(name='username', dest='username',
        #                            location='form', required=True,
        #                            help='参数缺失')])
        # user = DemoModel(args.username, args.email)
        data = request.json
        return 'asda'

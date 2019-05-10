from flask_restful import Resource, reqparse


class BaseResource(Resource):
    @staticmethod
    def params_parser(params_rules=None):
        """
        解析参数（params_rules 中的子项数据详细说明请参考 flask_restful => post_parser.add_argument()）
        :param params_rules: [
            {
                :param name: Either a name or a list of option strings, e.g. foo or
            -f, --foo.
                :param default: The value produced if the argument is absent from the
                    request.
                :param dest: The name of the attribute to be added to the object
                    returned by :meth:`~reqparse.RequestParser.parse_args()`.
                :param bool required: Whether or not the argument may be omitted (optionals
                    only).
                :param action: The basic type of action to be taken when this argument
                    is encountered in the request. Valid options are "store" and "append".
                :param ignore: Whether to ignore cases where the argument fails type
                    conversion
                :param type: The type to which the request argument should be
                    converted. If a type raises an exception, the message in the
                    error will be returned in the response. Defaults to :class:`unicode`
                    in python2 and :class:`str` in python3.
                :param location: The attributes of the :class:`flask.Request` object
                    to source the arguments from (ex: headers, args, etc.), can be an
                    iterator. The last item listed takes precedence in the result set.
                :param choices: A container of the allowable values for the argument.
                :param help: A brief description of the argument, returned in the
                    response when the argument is invalid. May optionally contain
                    an "{error_msg}" interpolation token, which will be replaced with
                    the text of the error raised by the type converter.
                :param bool case_sensitive: Whether argument values in the request are
                    case sensitive or not (this will convert all values to lowercase)
                :param bool store_missing: Whether the arguments default value should
                    be stored if the argument is missing from the request.
                :param bool trim: If enabled, trims whitespace around the argument.
                :param bool nullable: If enabled, allows null value in argument.
            }
        ]
        :return:
        """
        if not isinstance(params_rules, list):
            return None
        post_parser = reqparse.RequestParser(bundle_errors=True)
        for rule in params_rules:
            name = rule.pop('name')
            post_parser.add_argument(name, **rule)
        return post_parser.parse_args()

from flasgger import Swagger


def init_swagger(app):
    # TODO config
    app.config['SWAGGER'] = {
        'title': 'Flasgger RESTful',
        'uiversion': 2
    }
    swag = Swagger(app)
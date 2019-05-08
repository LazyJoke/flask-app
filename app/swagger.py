from flasgger import Swagger


def init_swagger(app):
    app.config['SWAGGER'] = {
        'title': 'Flasgger RESTful',
        'uiversion': 2
    }
    swag = Swagger(app)
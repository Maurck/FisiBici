from flask import request
from flask_cors import CORS, cross_origin
'''
config.py: modulo donde se configura la aplicación
'''


def config_app(app):
    app.secret_key = 'clavesecreta'

    # app.config['CORS_HEADERS'] = 'Content-Type'
    # app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'
    # app.config['CORS_HEADERS'] = 'Access-Control-Allow-Credentials'

    app.config.update(
        SERVER_NAME='127.0.0.1:5000',
        SESSION_COOKIE_NAME='127.0.0.1:5000',
        SESSION_COOKIE_DOMAIN='127.0.0.1:5000',
    )

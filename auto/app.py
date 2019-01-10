# coding=utf-8
__author__ = 'fangfang'

from flask import Flask
from .config import config
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auto.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # config[config_name].init_app(app)

    login_manager.init_app(app)


    # 定时器
    # scheduler.init_app(app)
    # scheduler.start()

    # for blueprints
    from .blueprints import at as at_blueprint
    app.register_blueprint(at_blueprint, url_prefix='/')

    from .api import api_bp as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    # if app.config['SSL_REDIRECT']:
    #     from flask_sslify import SSLify
    #     sslify = SSLify(app)

    return app

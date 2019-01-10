# coding=utf-8
# --author='fangfang'

from flask import Blueprint, render_template
from .api import api as api_blueprint
from auto.config import DatabaseConfig

at = Blueprint('auto', __name__)


@at.route('/')
def index():
    return render_template('login.html')


# 配置参数
# app.config.from_object(DatabaseConfig)

# 注册api蓝图到app
# app.register_blueprint(api_blueprint, url_prefix='/')

# 需要创建sql的模型
# from api import models

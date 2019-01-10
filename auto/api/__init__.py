# coding=utf-8
# --author='fangfang'

from flask import Blueprint
from flask_restful import Api
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from auto.config import DatabaseConfig

# 实例化数据库对象

api_bp = Blueprint("api", __name__)
api = Api(api_bp)
engine = create_engine(DatabaseConfig.SQLALCHEMY_DATABASE_URI)
Session_db = sessionmaker(bind=engine)

# 引入Auth到api蓝图
from .auth import Auth
api.add_resource(Auth, '/auth/')



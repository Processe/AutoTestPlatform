# coding=utf-8
__author__ = 'fangfang'
import logging


class DatabaseConfig:
    # 使用mysqlclient
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/test?charset=utf8'
    # 使用pymysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/autotest?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 配置秘钥


class AppConfig:
    # 配置秘钥
    # SECRET_KEY = '*\xff\x93\xc8w\x13\x0e@3\xd6\x82\x0f\x84\x18\xe7\xd9\\|\x04e\xb9(\xfd\xc3'
    SECRET_KEY = 'QWERTYUIOPASDFGHJ'
    # logging level
    LOGGING_LEVEL = logging.INFO


class DevelopmentConfig(AppConfig):
    # 开启debug模式
    DEBUG = True


class ProductionConfig(AppConfig):
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}


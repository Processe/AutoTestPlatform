# coding=utf-8
# --author='fangfang'

# from auto import db   # db是在app/__init__.py生成的关联后的SQLAlchemy实例
from sqlalchemy import create_engine, Column
from sqlalchemy.types import String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from auto.config import DatabaseConfig
import datetime

engine = create_engine(DatabaseConfig.SQLALCHEMY_DATABASE_URI)
Base = declarative_base()   # 创建对象基类


class User(Base):
    '''
    user表数据模型
    '''
    __tablename__ = 'user'   # 创建表，指定表名
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(225), unique=True)
    password = Column(String(32), nullable=True)
    createtime = Column(DateTime(datetime.date), default=None)

    def __repr__(self):
        return '<User %r>' % self.username


class Project(Base):
    '''
    项目模型
    '''
    __tablename__ = 'Project'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(225), unique=True)
    explan = Column(String(225), default=None)
    por_type = Column(Integer, nullable= False)
    star_time = Column(DateTime(datetime.date), default=None)
    end_time = Column(DateTime(datetime.date), default=None)
    create_time = Column(DateTime(datetime.date), default=None)

    def __repr__(self):
        return '<Project %r>' % self.name



class Trade(Base):
    '''
    交易模型
    '''
    __tablename__ = 'Trade'
    id = Column(Integer, primary_key=True, autoincrement=True)
    modle_id = Column()
    name = Column(String(225), unique=True)
    explan = Column(String(225), default=None)


def create_db():
    # 创建所有Base子类数据库对象
    Base.metadata.create_all(engine)


def drop_db():
    # 删除所有Base子类的数据库对象
    Base.metadata.drop_all(engine)


if '__main__' == __name__:
    print('-----开始执行-----')
    create_db()



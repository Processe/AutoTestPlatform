# coding=utf-8
__author__ = 'fangfang'

from flask import session, url_for
from flask_restful import Resource, reqparse
from auto.api import Session_db
from auto.models import User

db = Session_db()


class Auth(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('user', type=str)
        self.parser.add_argument('password', type=str)

    def get(self):
        args = self.parser.parse_args()
        username = args['username']
        if username in session:
            session.pop(username, None)

        return {'status': "success", 'msg': 'logout success', 'url': url_for('routes.index')}, 201

    def post(self):
        args = self.parser.parse_args()
        print(str(args))
        username = args['user']
        password = args['password']
        user = User()
        print(user.username)
        users = db.query(user.username)
        if username in users:
            pwd = db.query.filter(user.username == username)
            if password == pwd:
                session['username'] = username
                return {"status": "success", "msg": "login success", "url": url_for('routes.dashboard')}, 201

        return {"status": "fail", "msg": "login fail", "url": url_for('login.html')}, 201






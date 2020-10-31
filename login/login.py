from flask import request, jsonify
from flask_restful import Resource
from db import app
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from db import database
from db.seveniruby_user11 import SevenirubyUser11
from jenkins.apijenkins import TaskApi

#
# app=Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 36000
# api = Api(app)
jwt = JWTManager(app)


class Login(Resource):
    # 无需验证
    @jwt_required
    def get(self):
        return {'hello': 'word'}

    # 用户登录
    def post(self):
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        user = database.User.query.filter_by(username=username, password=password).first()
        if user:
            return jsonify(
                errcode=0,
                errmsg='ok',
                username=user.username,
                mail=user.email,
                access_token=create_access_token(identity=username)

            )
        else:
            return jsonify(
                errcode=1,
                errmsg='用户名或者密码不对'
            )

    # 注册
    def put(self):

        username = request.json.get('username', None)
        password = request.json.get('password', None)
        email = request.json.get('email', None)

        seven = SevenirubyUser11()
        register_user = seven.add_users(username, password, email)
        if register_user['msk'] == 'ok':
            return jsonify(
                errcode=0,
                errmsg='ok',
            )

    # 注销
    def delete(self):
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        email = request.json.get('email', None)

        seven = SevenirubyUser11()
        delete_user = seven.delete_users(username, password, email)
        if delete_user['errcode'] == 0:
            return delete_user
        else:
            return delete_user


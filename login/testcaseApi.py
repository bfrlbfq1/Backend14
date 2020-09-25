from flask import request, jsonify
from flask_restful import Api, Resource
from db import app
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from db import database
from db.seveniruby_testcase import SevenirubyTestcase
from jenkins.apijenkins import TaskApi

#
# app=Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'
api = Api(app)
jwt = JWTManager(app)


class TestCaseApi(Resource):
    # 无需验证
    @jwt_required
    def get(self):
        return {'hello': 'word'}

    # 新增测试用例
    def post(self):
        casename = request.json.get('casename', None)
        description = request.json.get('description', None)
        data = request.json.get('data', None)

        seven = SevenirubyTestcase()
        register_testcase = seven.add_testcase(casename, description, data)
        if register_testcase['msk'] == 'ok':
            return jsonify(
                errcode=0,
                errmsg='ok',
            )
    # 注册
    def put(self):

        casename = request.json.get('casename', None)
        description = request.json.get('description', None)
        data = request.json.get('data', None)

        seven = SevenirubyTestcase()
        register_user = seven.put_testcase(casename, description, data)
        if register_user['msk'] == 'ok':
            return register_user
        else:
            return register_user

    # 注销
    def delete(self):
        casename = request.json.get('casename', None)
        description = request.json.get('description', None)
        data = request.json.get('data', None)

        seven = SevenirubyTestcase()
        delete_testcase = seven.delete_testcase(casename, description, data)
        if delete_testcase['errcode'] == 0:
            return delete_testcase
        else:
            return delete_testcase



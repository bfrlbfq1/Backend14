from flask import request, jsonify
from flask_restful import Api, Resource
from db import app
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from db import database
from db.seveniruby_testreport import SevenirubyTestreport
from jenkins.apijenkins import TaskApi

#
# app=Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'
api = Api(app)
jwt = JWTManager(app)


class TestReportApi(Resource):
    # 无需验证
    @jwt_required
    def get(self):
        return {'hello': 'word'}

    # 新增测试用例
    def post(self):
        reportname = request.json.get('reportname', None)
        description = request.json.get('description', None)
        data = request.json.get('data', None)

        seven = SevenirubyTestreport()
        register_roport = seven.add_report(reportname, description, data)
        if register_roport['msk'] == 'ok':
            return register_roport
        else:
            return register_roport
    # 注册
    def put(self):

        reportname = request.json.get('reportname', None)
        description = request.json.get('description', None)
        data = request.json.get('data', None)

        seven = SevenirubyTestreport()
        register_user = seven.put_report(reportname, description, data)
        if register_user['msk'] == 'ok':
            return register_user
        else:
            return register_user

    # 注销
    def delete(self):
        reportname = request.json.get('reportname', None)
        description = request.json.get('description', None)
        data = request.json.get('data', None)

        seven = SevenirubyTestreport()
        delete_testcase = seven.delete_report(reportname, description, data)
        if delete_testcase['errcode'] == 0:
            return delete_testcase
        else:
            return delete_testcase



from flask import request,jsonify
from flask_restful import Api,Resource
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
api =Api(app)
jwt =JWTManager(app)

class Login(Resource):
    # 无需验证
    @jwt_required
    def get(self):
        return {'hello':'word'}
    # 用户登录
    def post(self):
        username=request.json.get('username',None)
        password=request.json.get('password',None)
        user=database.User.query.filter_by(username=username,password=password).first()
        if user:
            return jsonify(
                errcode=0,
                errmsg='ok',
                username=user.username,
                access_token=create_access_token(identity=username)

            )
        else:
            return jsonify(
                errcode=1,
                errmsg='用户名或者密码不对'
            )
    # 注册
    def put(self):
        pass
    #注销
    def delete(self):
        pass

api.add_resource(Login,'/login')
api.add_resource(SevenirubyUser11,'/db')
api.add_resource(TaskApi,'/task')
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,request
from flask_restful import Api,Resource
import testsqlalchemy
#
# app=Flask(__name__)
api =Api(testsqlalchemy.app)

class TestCase(Resource):
    def get(self):
        r=[]
        for t in testsqlalchemy.User.query.all():
            res = {}
            res['id']=t.id
            res['username'] = t.username
            res['password'] = t.password
            res['email'] = t.email
            r.append(res)
        return r
        # return {'hello':'word'}
    def post(self):
        t=testsqlalchemy.User(
            username=request.json['username'],
            password=request.json['password'],
            email=request.json['email'],

        )
        testsqlalchemy.db.session.add(t)
        testsqlalchemy.db.session.commit(t)

        return {"msk":'ok'}
class Login(Resource):
    def get(self):
        return {'hello':'word'}
api.add_resource(TestCase,'/testcase')
api.add_resource(Login,'/login')
if __name__ == '__main__':
    testsqlalchemy.app.run(debug=True)
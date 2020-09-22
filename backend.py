from flask import Flask
from flask_restful import Api,Resource

app=Flask(__name__)
api =Api(app)

class TestCase(Resource):
    def get(self):
        return {'hello':'word'}
class Login(Resource):
    def get(self):
        return {'hello':'word'}
api.add_resource(TestCase,'/testcase')
api.add_resource(Login,'/login')
if __name__ == '__main__':
    app.run(debug=True)
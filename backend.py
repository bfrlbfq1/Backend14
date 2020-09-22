from flask import Flask
from flask_restful import Api,Resource

app=Flask(__name__)
api =Api(app)

class HelloWord(Resource):
    def get(self):
        return {'hello':'word'}
api.add_resource(HelloWord,'/')
if __name__ == '__main__':
    app.run(debug=True)
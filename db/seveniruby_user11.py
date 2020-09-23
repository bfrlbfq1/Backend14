from db import app
from flask_restful import Api,Resource
from db import database
from flask import request

#
# app=Flask(__name__)
api =Api(app)
class SevenirubyUser11(Resource):
    def get(self):
        r=[]
        for t in database.User.query.all():
            res = {}
            res['id']=t.id
            res['username'] = t.username
            res['password'] = t.password
            res['email'] = t.email
            r.append(res)
        return r
        # return {'hello':'word'}
    def post(self):
        t= database.User(
            username=request.json['username'],
            password=request.json['password'],
            email=request.json['email'],

        )
        database.db.session.add(t)
        database.db.session.commit(t)

        return {"msk":'ok'}
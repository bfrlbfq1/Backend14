from flask import request, jsonify
from flask_restful import Api, Resource
from db import app
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from db import database
from db.seveniruby_status import SevenirubyAssertStatus


#
# app=Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'
api = Api(app)
jwt = JWTManager(app)


class AssertStatus(Resource):
    # 无需验证
    @jwt_required
    def get(self):
        seveniruby_assert_status=SevenirubyAssertStatus()
        return seveniruby_assert_status.get_status()
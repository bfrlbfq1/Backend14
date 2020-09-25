from jenkinsapi.jenkins import Jenkins
from flask_restful import Resource
from flask import request
from db import app
# 使用jenkins做任务分发
jenkins=Jenkins(
    'http://129.211.167.92:8020/',
    username='manager',
    password='11e25651ef39f57100d35173b9e85edb49'
)
# 用例调度
class TaskApi(Resource):
    # todo: 查询所有的任务
    def get(self):
        pass
    def post(self):
        # todo: 用例获取
        testcases=request.json.get('testcases',None)
        testcaseJob=request.json.get('job',None)
        # todo: 调度jenkins，驱动job执行
        jenkins[f'{testcaseJob}'].invoke(
            securitytoken='testcases',
            build_params={
                'testcases': testcases
            }
        )
        return {
            'errcode': 0,
            'errmsg': 'ok'
        }


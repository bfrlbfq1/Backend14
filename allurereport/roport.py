from flask_restful import Resource
from jenkins.apijenkins import jenkins
# 数据获取与数据展示
class Report(Resource):
    def get(self):
        # 展示报告数据和曲线图
        pass
    def post(self):
        # todo: pull模式 主动从jenkins中拉取数据
        jenkins['testcase'].get_last_build().get_resultset()
        # todo: push模式 让jenkins node主动push到服务器
        # todo: 把测试报告数据与测试报告文件保存
        pass

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
from jenkins.apijenkins import TaskApi
from login.login import Login
from flask_restful import Api
from db import app
from login.report import TestReportApi
from login.testcaseApi import TestCaseApi
from flask_cors import CORS
from flask_restful import Resource
api = Api(app)
CORS(app)

api.add_resource(Login, '/login')
# api.add_resource(SevenirubyUser11,'/db')
api.add_resource(TaskApi, '/task')
api.add_resource(TestCaseApi,'/tesecase')
api.add_resource(TestReportApi,'/report')
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

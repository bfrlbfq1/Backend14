from db import app
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1qaz!QAZ@129.211.167.92/SQLAlchemy'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://python14:python14@stuq.ceshiren.com:23306/python14'
db = SQLAlchemy(app)

#用户
class User(db.Model):
    __tablename__ = 'seveniruby_user11'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

# 用例
class TestCase(db.Model):
    __tablename__ = 'seveniruby_testcase'
    id = db.Column(db.Integer, primary_key=True)
    casename  = db.Column(db.String(80), unique=True, nullable=True)
    description  = db.Column(db.String(1024), unique=False, nullable=False)
    data  = db.Column(db.String(1024), unique=False, nullable=False)

    def __init__(self, casename, description, data):
        self.casename = casename
        self.description = description
        self.data = data

    def __repr__(self):
        return '<User %r>' % self.casename

#报告
class TestReport(db.Model):
    __tablename__ = 'seveniruby_testreport'
    id = db.Column(db.Integer, primary_key=True)
    reportname  = db.Column(db.String(80), unique=True, nullable=True)
    description  = db.Column(db.String(1024), unique=False, nullable=False)
    data  = db.Column(db.String(1024), unique=False, nullable=False)

    def __init__(self, reportname, description, data):
        self.reportname = reportname
        self.description = description
        self.data = data

    def __repr__(self):
        return '<User %r>' % self.reportname
# 相应状态
class AssertStatus(db.Model):
    __tablename__ = 'seveniruby_status'
    id = db.Column(db.Integer, primary_key=True)
    errmsg  = db.Column(db.String(80), unique=True, nullable=True)
    errcode  = db.Column(db.String(1024), unique=False, nullable=False)

    def __init__(self, errmsg, errcode):
        self.errmsg = errmsg
        self.errcode = errcode

    def __repr__(self):
        return '<AssertStatus %r>' % self.errmsg

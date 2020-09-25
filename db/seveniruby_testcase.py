from db.database import db, TestCase


class SevenirubyTestcase:
    def get_testcase(self):
        r = []
        for t in TestCase.query.all():
            res = {}
            res['id'] = t.id
            res['casename'] = t.casename
            res['description'] = t.description
            res['data'] = t.data
            r.append(res)
        return r
        # return {'hello':'word'}

    def add_testcase(self, casename, description,data):
        user = TestCase.query.filter_by(casename=casename).first()
        if user:
            return {
                'errcode': 1,
                'errmsg': '数据存在'
            }
        else:
            try:
                print(description)
                t = TestCase(
                    # casename=request.json['casename'],
                    # description=request.json['description'],
                    # data=request.json['data'],
                    casename=casename,
                    description=description,
                    data=data,

                )
                # print(data)
            except Exception as e:
                print(e)
            db.session.add(t)
            db.session.commit()

            return {"msk": 'ok'}

    def put_testcase(self, casename, description, data):
        user = TestCase.query.filter_by(casename=casename).first()
        # user = database.TestCase.query.filter_by(casename=casename, description=description).first()
        if user:
            if description is None and data is not None:
                user.data = data
                db.session.commit()
            elif description is not None and data is None:
                user.description = description
                db.session.commit()
            elif description is not None and data is not None:
                user.description = description
                user.data = data
                db.session.commit()
        else:
            return {
                'errcode': 1,
                'errmsg': '数据更新错误'
            }
        return {
            'errcode': 0,
            'errmsg': 'ok'
        }

    def delete_testcase(self, casename, description, data):
        print(casename, description, data)
        user = TestCase.query.filter_by(casename=casename).first()
        print(user)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {
                'errcode': 0,
                'errmsg': f'{casename}已删除'
            }
        else:
            return {
                'errcode': 1,
                'errmsg': f'{casename}不存在'
            }
